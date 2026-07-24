#!/usr/bin/env python3
import os
import sys
import yaml
import json

def parse_frontmatter(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {"error": str(e)}

    if not content.startswith("---"):
        return {"error": "No frontmatter found"}

    parts = content.split("---")
    if len(parts) < 3:
        return {"error": "Invalid frontmatter block"}

    try:
        data = yaml.safe_load(parts[1])
        return {"success": True, "data": data}
    except Exception as e:
        return {"error": f"YAML parsing error: {str(e)}"}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_frontmatter.py <file_path>")
        sys.exit(1)
    
    result = parse_frontmatter(sys.argv[1])
    print(json.dumps(result, indent=2))
