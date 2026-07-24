import os
import glob
import re

vault_path = "/home/ali/v2/.agents/skills/notes-projection-workspace/iteration-1/eval-0/old_skill/outputs"
topic_slug = "the-pygmalion-effect"
topic_dir = os.path.join(vault_path, topic_slug)

all_md_files = glob.glob(os.path.join(topic_dir, "**/*.md"), recursive=True)
index_path = os.path.join(vault_path, f"{topic_slug}-Index.md")
if os.path.exists(index_path):
    all_md_files.append(index_path)

existing_titles = set()
for filepath in all_md_files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Try frontmatter title
    title_match = re.search(r'^title:\s*"(.*?)"', content, re.MULTILINE)
    if not title_match:
        title_match = re.search(r'^title:\s*(.*)', content, re.MULTILINE)
    
    # Try H1
    h1_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
    
    title = None
    if title_match:
        title = title_match.group(1).strip().strip('"')
    elif h1_match:
        title = h1_match.group(1).strip()
    
    if title:
        existing_titles.add(title)
        print(f"File: {os.path.basename(filepath)} -> Title: '{title}'")

print(f"Total existing titles: {len(existing_titles)}")

# Print first 10 broken links
count = 0
for filepath in all_md_files:
    with open(filepath, 'r') as f:
        lines = f.readlines()
    for line_num, line in enumerate(lines, 1):
        matches = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', line)
        for match in matches:
            target = match.strip()
            if target not in existing_titles:
                print(f"Broken: in {os.path.basename(filepath)}: L{line_num} -> '{target}'")
                count += 1
                if count >= 20:
                    break
        if count >= 20:
            break
    if count >= 20:
        break
