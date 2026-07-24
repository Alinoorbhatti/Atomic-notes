import re
import os
import json

plan_path = "/home/ali/v2/.agents/skills/notes-projection-workspace/iteration-1/eval-0/old_skill/outputs/the-pygmalion-effect/.plan"

with open(plan_path, 'r') as f:
    content = f.read()

# Get the sections
subtopics_section = re.search(r'SUBTOPICS:\n(.*)\nCROSS_DOMAIN_FIELDS:', content, re.DOTALL)
subtopics_text = subtopics_section.group(1) if subtopics_section else ""

subtopic_blocks = re.findall(r'(\d+\.\s+.*?)(?=\n\d+\.\s+|$)', subtopics_text, re.DOTALL)

subtopics = []
for block in subtopic_blocks:
    lines = block.strip().split('\n')
    title = re.sub(r'^\d+\.\s*', '', lines[0]).strip()
    bucket = ""
    desc = ""
    concepts = []
    
    in_concepts = False
    for line in lines[1:]:
        if 'BUCKET:' in line:
            bucket = line.split('BUCKET:')[1].strip()
        elif 'DESCRIPTION:' in line:
            desc = line.split('DESCRIPTION:')[1].strip()
        elif 'ATOMIC_CONCEPTS:' in line:
            in_concepts = True
        elif in_concepts and line.strip().startswith('-'):
            m = re.match(r'\s*-\s*(.*?)\s*—\s*(.*)', line)
            if m:
                concepts.append({"title": m.group(1).strip(), "desc": m.group(2).strip()})
    subtopics.append({
        "title": title,
        "bucket": bucket,
        "description": desc,
        "concepts": concepts
    })

# Extract all concepts in order
all_concepts = []
for s in subtopics:
    for c in s['concepts']:
        # compute slug and paths
        slug = c['title'].lower().replace(" ", "-").replace("'", "").replace(",", "").replace(".", "").replace(":", "")
        # let's simplify slug rules: lowercase, spaces->dashes, strip punctuation
        # Let's clean punctuation
        slug = re.sub(r'[^\w\s-]', '', c['title'].lower()).replace(' ', '-')
        # double dashes to single dash
        slug = re.sub(r'-+', '-', slug)
        
        bucket_slug = re.sub(r'[^\w\s-]', '', s['bucket'].lower()).replace(' ', '-')
        bucket_slug = re.sub(r'-+', '-', bucket_slug)
        
        all_concepts.append({
            "title": c['title'],
            "subtopic": s['title'],
            "bucket": s['bucket'],
            "bucket_slug": bucket_slug,
            "slug": slug,
            "desc": c['desc']
        })

print(json.dumps(all_concepts, indent=2))
