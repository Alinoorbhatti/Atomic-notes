#!/usr/bin/env python3
import os
import sys
import json
import yaml

def scan_vault(vault_path):
    if not os.path.exists(vault_path):
        print(json.dumps({"error": f"Path {vault_path} does not exist.", "existing_concepts": []}))
        return

    existing_concepts = []
    
    for root, _, files in os.walk(vault_path):
        for f in files:
            if f.endswith(".md") and not f.startswith("_"):
                file_path = os.path.join(root, f)
                title = f[:-3] # Default to filename
                
                # Try to extract title from frontmatter
                try:
                    with open(file_path, 'r', encoding='utf-8') as md_file:
                        content = md_file.read()
                        if content.startswith("---"):
                            parts = content.split("---")
                            if len(parts) >= 3:
                                data = yaml.safe_load(parts[1])
                                if data and 'title' in data:
                                    title = data['title']
                except Exception:
                    pass # Fallback to filename if parsing fails
                
                existing_concepts.append({
                    "title": title,
                    "slug": f[:-3],
                    "path": file_path
                })
                
    result = {
        "total_files": len(existing_concepts),
        "existing_concepts": existing_concepts
    }
    
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scan_vault.py <vault_path>")
        sys.exit(1)
    scan_vault(sys.argv[1])
