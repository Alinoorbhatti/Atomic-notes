#!/usr/bin/env python3
import os
import sys
import yaml
try:
    import chromadb
except ImportError:
    print("Please install chromadb: pip install chromadb")
    sys.exit(1)

def build_index(vault_path):
    if not os.path.exists(vault_path):
        print(f"Error: {vault_path} does not exist.")
        return

    # Use a persistent client stored in the vault's .obsidian or root hidden dir
    db_path = os.path.join(vault_path, ".rag_db")
    client = chromadb.PersistentClient(path=db_path)
    
    # We use a single collection for the vault
    collection = client.get_or_create_collection(name="vault_notes")
    
    print(f"Scanning {vault_path} for markdown files...")
    
    docs = []
    ids = []
    metadatas = []
    
    for root, _, files in os.walk(vault_path):
        for f in files:
            if f.endswith(".md") and not f.startswith("_") and not ".rag_db" in root:
                file_path = os.path.join(root, f)
                title = f[:-3]
                
                with open(file_path, 'r', encoding='utf-8') as md_file:
                    content = md_file.read()
                    
                # Store the filename as ID, content as the document
                # In a robust system, we would chunk the content, but for atomic notes 
                # (which are short), full-file indexing is acceptable.
                ids.append(f)
                docs.append(content)
                metadatas.append({"title": title, "path": file_path})
                
    if docs:
        print(f"Indexing {len(docs)} notes... This may take a moment.")
        # Upsert automatically overwrites existing IDs if they changed
        collection.upsert(
            documents=docs,
            metadatas=metadatas,
            ids=ids
        )
        print("Indexing complete!")
    else:
        print("No markdown files found to index.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rag_indexer.py <vault_path>")
        sys.exit(1)
    build_index(sys.argv[1])
