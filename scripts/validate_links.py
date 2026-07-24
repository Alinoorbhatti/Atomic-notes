#!/usr/bin/env python3
import os
import re
import sys
import json

def validate_links(vault_path):
    if not os.path.exists(vault_path):
        print(json.dumps({"error": f"Path {vault_path} does not exist."}))
        sys.exit(1)

    all_titles = set()
    links = []
    
    # regex for [[Wikilink]] or [[Wikilink|Alias]]
    link_pattern = re.compile(r'\[\[(.*?)\]\]')

    # 1. Inventory files
    for root, _, files in os.walk(vault_path):
        for f in files:
            if f.endswith(".md"):
                file_path = os.path.join(root, f)
                # Naive title extraction (basename without extension)
                # In production, parse frontmatter 'title'
                title = f[:-3]
                all_titles.add(title.lower())

                with open(file_path, 'r', encoding='utf-8') as md_file:
                    content = md_file.read()
                    matches = link_pattern.findall(content)
                    for match in matches:
                        target = match.split('|')[0].strip().lower()
                        links.append({
                            "source": f,
                            "target": target
                        })

    # 2. Analyze
    broken = []
    for link in links:
        if link['target'] not in all_titles:
            broken.append(link)

    result = {
        "scanned_files": len(all_titles),
        "total_links": len(links),
        "broken_links": len(broken),
        "broken_details": broken
    }
    
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_links.py <vault_path>")
        sys.exit(1)
    validate_links(sys.argv[1])
