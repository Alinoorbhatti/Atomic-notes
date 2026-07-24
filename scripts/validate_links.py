#!/usr/bin/env python3
import os
import re
import sys
import json
import yaml

def validate_links(vault_path):
    if not os.path.exists(vault_path):
        print(json.dumps({"error": f"Path {vault_path} does not exist."}))
        sys.exit(1)

    valid_targets_map = {}
    file_contents = {}
    
    for root, dirs, files in os.walk(vault_path):
        # Exclude internal directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith(".md"):
                file_path = os.path.join(root, f)
                canonical_id = f[:-3]
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as md_file:
                        content = md_file.read()
                        file_contents[f] = content
                        
                        valid_targets_map[canonical_id.lower()] = canonical_id
                        
                        if content.startswith("---"):
                            parts = content.split("---")
                            if len(parts) >= 3:
                                data = yaml.safe_load(parts[1])
                                if data:
                                    if 'title' in data and data['title']:
                                        valid_targets_map[str(data['title']).lower()] = canonical_id
                                    if 'aliases' in data and data['aliases']:
                                        aliases = data['aliases']
                                        if isinstance(aliases, list):
                                            for alias in aliases:
                                                valid_targets_map[str(alias).lower()] = canonical_id
                                        elif isinstance(aliases, str):
                                            valid_targets_map[aliases.lower()] = canonical_id
                except Exception:
                    pass

    links = []
    broken = []
    incoming_links = {canon: 0 for canon in set(valid_targets_map.values())}
    link_pattern = re.compile(r'\[\[(.*?)\]\]')
    
    for f, content in file_contents.items():
        matches = link_pattern.findall(content)
        for match in matches:
            target = match.split('|')[0]
            target = target.split('#')[0]
            target = target.split('^')[0]
            target = target.strip().lower()
            
            if not target:
                continue
            
            links.append({
                "source": f,
                "target": target
            })
            
            if target in valid_targets_map:
                incoming_links[valid_targets_map[target]] += 1
            else:
                broken.append({
                    "source": f,
                    "target": target
                })

    orphan_notes = [canon for canon, count in incoming_links.items() if count == 0]

    result = {
        "scanned_files": len(file_contents),
        "total_links": len(links),
        "broken_links": len(broken),
        "broken_details": broken,
        "orphan_notes": sorted(orphan_notes),
        "orphan_count": len(orphan_notes)
    }
    
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_links.py <vault_path>")
        sys.exit(1)
    validate_links(sys.argv[1])
