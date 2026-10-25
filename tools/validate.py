#!/usr/bin/env python3
"""Validate the curated repository; never access vendor services or credentials."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'FILE-HASHES.json'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def project_files():
    """Use the actual Git candidate set, or a portable non-Git fallback."""
    try:
        probe = subprocess.run(['git', '-C', str(ROOT), 'rev-parse', '--show-toplevel'],
                               capture_output=True, text=True)
        if probe.returncode == 0 and Path(probe.stdout.strip()).resolve() == ROOT:
            result = subprocess.run(['git', '-C', str(ROOT), 'ls-files', '--cached',
                                     '--others', '--exclude-standard', '-z'],
                                    capture_output=True, check=True)
            paths = {ROOT / os.fsdecode(p) for p in result.stdout.split(b'\0') if p}
            require(all(p.is_file() and not p.is_symlink() for p in paths),
                    'Candidate includes a missing file or symlink; review the index')
            return sorted(paths)
    except FileNotFoundError:
        pass
    ignored = {'.git', '__pycache__', '.venv', 'venv', '.pytest_cache', 'local',
               'private', 'work', 'raw-captures', 'credentials', 'secrets', 'dist', 'build'}
    paths = []
    for folder, directories, filenames in os.walk(ROOT):
        directories[:] = [d for d in directories if d not in ignored]
        for name in filenames:
            p = Path(folder) / name
            if name == '.DS_Store' or name.startswith('.env') or p.suffix in {
                    '.pyc', '.db', '.sqlite', '.sqlite3', '.log', '.zip'}:
                continue
            require(not p.is_symlink(), 'Review symlink before including it: ' + str(p))
            paths.append(p)
    return sorted(paths)


def run_reference():
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    commands = [
        [sys.executable, '-m', 'unittest', 'discover', '-s', 'reference', '-p', 'test_*.py', '-v'],
        [sys.executable, 'reference/demo.py'],
    ]
    count = None
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True)
        require(result.returncode == 0, 'Reference failed:\n' + result.stdout + result.stderr)
        if 'unittest' in command:
            match = re.search(r'Ran (\d+) tests?', result.stderr)
            require(match is not None and int(match.group(1)) > 0, 'No reference tests ran')
            count = int(match.group(1))
    return count


def schema_root(tool):
    schema = tool['inputSchema']
    require(schema.get('type') == 'object', 'Non-object schema: ' + tool['name'])
    properties = schema.get('properties', {})
    require(isinstance(properties, dict), 'Invalid property map: ' + tool['name'])
    require(not set(schema.get('required', [])) - set(properties),
            'Required field absent: ' + tool['name'])


def check_evidence():
    muse = read_json(ROOT / 'config/muse-tools.normalized.json')
    require(muse['namespace_count'] == 33 and len(muse['tools']) == 193, 'Muse tool count changed')
    for tool in muse['tools']:
        schema_root(tool)
    export = ROOT / 'evidence/muse/runtime-export'
    audit = read_json(export / 'EXPORT-AUDIT.json')
    for entry in audit['files']:
        require(digest(export / entry['path']) == entry['sha256'],
                'Muse import changed: ' + entry['path'])
    require(len(audit['files']) == audit['copied_files'], 'Muse audit count mismatch')
    public = {}
    for date, expected, variants, runtime in [('2026-10-24', 43, 8, 6), ('2026-08-21', 51, 10, 0)]:
        evidence = ROOT / 'evidence/grok' / ('public-prompt-' + date)
        prompts = ROOT / 'prompts' / ('grok-public-' + date)
        source_path = evidence / 'grok-bot.md'
        source = source_path.read_text(encoding='utf-8')
        provenance = read_json(evidence / 'PROVENANCE.json')
        require(digest(source_path) == provenance['source_sha256'], 'Grok source hash: ' + date)
        require((prompts / 'system.md').read_text().strip() ==
                source.split('# 2.', 1)[0].split('\n', 1)[1].strip(), 'Main split changed: ' + date)
        require(len(provenance['variants']) == variants and
                len(provenance['runtime_templates']) == runtime, 'Grok section count: ' + date)
        for entry in provenance['variants'] + provenance['runtime_templates']:
            start = source.index(entry['source_heading']) + len(entry['source_heading'])
            following = re.search(r'^#{1,2} ', source[start:], re.M)
            body = source[start:start + following.start()] if following else source[start:]
            require((prompts / entry['file']).read_text().strip() == body.strip(),
                    'Prompt split changed: ' + entry['file'])
        tools = read_json(ROOT / 'config' / ('grok-tools.public-' + date + '.json'))
        require(len(tools['tools']) == expected, 'Public tool count: ' + date)
        for tool in tools['tools']:
            schema_root(tool)
        public[date] = {'tools': expected, 'variants': variants, 'runtime_templates': runtime}
    skills = len(list((ROOT / 'evidence/grok/public-prompt-2026-10-24/skills').glob('*.md')))
    require(skills == 54, 'Grok skill count changed')
    historical = ROOT / 'evidence/manus-historical-2025-07-20'
    for entry in read_json(historical / 'PROVENANCE.json')['files']:
        require(digest(historical / entry['file']) == entry['sha256'], 'Historical source changed')
    require(len(read_json(historical / '2025-07-20_tools.json')) == 29, 'Historical tool count changed')
    return {'muse_tools': 193, 'muse_import_files_verified': len(audit['files']),
            'public_grok': public, 'grok_skills': skills, 'historical_manus_tools': 29}


def check_links(paths):
    count = 0
    for path in paths:
        if path.suffix != '.md':
            continue
        relative = path.relative_to(ROOT)
        source = 'evidence' in relative.parts or any(p.startswith('grok-public-') for p in relative.parts)
        if source and path.name != 'README.md':
            continue  # Verbatim source bodies retain vendor/VM links.
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            target = target.strip('<>')
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            local = (path.parent / unquote(target.split('#', 1)[0])).resolve()
            require(local == ROOT or ROOT in local.parents, 'Link escapes repository: ' + str(relative))
            require(local.exists(), 'Broken link in ' + str(relative) + ': ' + target)
            count += 1
    return count


def check_credentials(paths):
    patterns = [r'-----BEGIN (?:OPENSSH |RSA |EC )?PRIVATE KEY-----',
                r'\bAKIA[A-Z0-9]{16}\b', r'\b(?:ghp_|gho_|xoxb-|xoxp-)[A-Za-z0-9_-]{15,}',
                r'\bgithub_pat_[A-Za-z0-9_]{30,}', r'\bya29\.[A-Za-z0-9_-]{20,}']
    for path in paths:
        text = path.read_text(encoding='utf-8')
        require(not any(re.search(pattern, text) for pattern in patterns),
                'Review possible credential in ' + str(path.relative_to(ROOT)))


def inventory(paths):
    return {'algorithm': 'SHA-256', 'excludes': ['FILE-HASHES.json'], 'files': [
        {'path': p.relative_to(ROOT).as_posix(), 'bytes': p.stat().st_size, 'sha256': digest(p)}
        for p in paths if p != MANIFEST]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh-manifest', action='store_true',
                        help='refresh FILE-HASHES.json after content checks pass')
    args = parser.parse_args()
    paths = project_files()
    results = {'reference_tests': run_reference(), 'demo': 'passed'}
    json_paths = [p for p in paths if p.suffix == '.json']
    for path in json_paths:
        read_json(path)
    results['json_files_parsed'] = len(json_paths)
    results['evidence_integrity'] = check_evidence()
    results['authored_links_checked'] = check_links(paths)
    check_credentials(paths)
    results['scoped_credential_format_scan'] = 'passed (not a universal sensitive-data detector)'
    current = inventory(paths)
    if args.refresh_manifest:
        MANIFEST.write_text(json.dumps(current, indent=2) + '\n', encoding='utf-8')
    require(read_json(MANIFEST) == current,
            'Inventory changed; review edits, then use --refresh-manifest')
    results['file_inventory'] = {'files': len(current['files']), 'status': 'passed'}
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, subprocess.SubprocessError) as error:
        print('Validation failed: ' + str(error), file=sys.stderr)
        sys.exit(1)
