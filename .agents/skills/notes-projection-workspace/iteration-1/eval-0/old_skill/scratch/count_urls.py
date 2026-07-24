import os
import glob
import re

vault_path = "/home/ali/v2/.agents/skills/notes-projection-workspace/iteration-1/eval-0/old_skill/outputs"
topic_slug = "the-pygmalion-effect"
topic_dir = os.path.join(vault_path, topic_slug)

all_md_files = glob.glob(os.path.join(topic_dir, "**/*.md"), recursive=True)

urls = set()
for filepath in all_md_files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract URLs from frontmatter or body
    # Find all urls matching http/https
    found_urls = re.findall(r'https?://[^\s,\"\']+', content)
    for url in found_urls:
        # Strip trailing parentheses, brackets, periods
        url = url.rstrip(').]')
        urls.add(url)

print(f"Unique source URLs count: {len(urls)}")
