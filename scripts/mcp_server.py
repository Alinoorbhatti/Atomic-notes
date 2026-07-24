#!/usr/bin/env python3
import os
import re
import yaml
import json
from mcp.server.fastmcp import FastMCP

try:
    import chromadb
except ImportError:
    chromadb = None

# Create the MCP Server
mcp = FastMCP("Atomic Notes Server")

@mcp.tool()
def scan_vault(vault_path: str) -> str:
    """
    Scans an existing Obsidian vault and returns a list of existing concepts.
    Useful for incremental mapping to avoid proposing duplicate concepts.
    
    Args:
        vault_path: Absolute path to the Obsidian vault directory.
    """
    if not os.path.exists(vault_path):
        return json.dumps({"error": f"Path {vault_path} does not exist.", "existing_concepts": []})

    existing_concepts = []
    
    for root, _, files in os.walk(vault_path):
        for f in files:
            if f.endswith(".md") and not f.startswith("_"):
                file_path = os.path.join(root, f)
                title = f[:-3]
                
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
                    pass
                
                existing_concepts.append({
                    "title": title,
                    "slug": f[:-3],
                    "path": file_path
                })
                
    return json.dumps({
        "total_files": len(existing_concepts),
        "existing_concepts": existing_concepts
    }, indent=2)


@mcp.tool()
def validate_links(vault_path: str) -> str:
    """
    Audits the markdown files in a vault for broken wikilinks.
    
    Args:
        vault_path: Absolute path to the Obsidian vault directory.
    """
    if not os.path.exists(vault_path):
        return json.dumps({"error": f"Path {vault_path} does not exist."})

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

    return json.dumps({
        "scanned_files": len(file_contents),
        "total_links": len(links),
        "broken_links": len(broken),
        "broken_details": broken,
        "orphan_notes": sorted(orphan_notes),
        "orphan_count": len(orphan_notes)
    }, indent=2)


@mcp.tool()
def parse_frontmatter(file_path: str) -> str:
    """
    Parses the YAML frontmatter from a markdown file.
    
    Args:
        file_path: Absolute path to the markdown file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return json.dumps({"error": str(e)})

    if not content.startswith("---"):
        return json.dumps({"error": "No frontmatter found"})

    parts = content.split("---")
    if len(parts) < 3:
        return json.dumps({"error": "Invalid frontmatter block"})

    try:
        data = yaml.safe_load(parts[1])
        return json.dumps({"success": True, "data": data}, indent=2)
    except Exception as e:
        return json.dumps({"error": f"YAML parsing error: {str(e)}"})


@mcp.tool()
def rag_search(query: str, vault_path: str, limit: int = 3) -> str:
    """
    Performs a semantic (RAG) search across the user's existing vault to find relevant notes.
    Useful for discovering historical concepts to interlink with newly generated notes.
    
    Args:
        query: The semantic concept or topic to search for.
        vault_path: Absolute path to the Obsidian vault directory.
        limit: Number of results to return (default 3).
    """
    if not chromadb:
        return json.dumps({"error": "chromadb is not installed. Please pip install chromadb."})
        
    db_path = os.path.join(vault_path, ".rag_db")
    if not os.path.exists(db_path):
        return json.dumps({"error": f"No RAG index found at {db_path}. Please run rag_indexer.py first."})
        
    try:
        client = chromadb.PersistentClient(path=db_path)
        collection = client.get_collection(name="vault_notes")
        
        results = collection.query(
            query_texts=[query],
            n_results=limit
        )
        
        matches = []
        for idx in range(len(results['ids'][0])):
            matches.append({
                "title": results['metadatas'][0][idx]['title'],
                "filename": results['ids'][0][idx],
                "distance": results['distances'][0][idx]
            })
            
        return json.dumps({"query": query, "matches": matches}, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


if __name__ == "__main__":
    mcp.run()
