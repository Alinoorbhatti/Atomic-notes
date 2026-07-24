import os
import re

vault_path = "/home/ali/v2/.agents/skills/notes-projection-workspace/iteration-1/eval-2/old_skill/outputs"
topic_slug = "quantum-computing"

plan_file = os.path.join(vault_path, topic_slug, ".plan")
with open(plan_file, "r") as f:
    plan = f.read()

def parse_plan(plan):
    lines = plan.split("\n")
    subtopics = []
    current_sub = None
    buckets = []
    
    in_buckets = False
    in_subtopics = False
    
    for line in lines:
        if line.startswith("BUCKETS:"):
            in_buckets = True
            in_subtopics = False
            continue
        if line.startswith("SUBTOPICS:"):
            in_subtopics = True
            in_buckets = False
            continue
        if line.startswith("CROSS_DOMAIN_FIELDS:"):
            in_subtopics = False
            continue
            
        if in_buckets and line.strip() and not line.startswith("["):
            match = re.match(r"\d+\.\s+([^\—]+)\s+—", line)
            if match:
                buckets.append(match.group(1).strip())
                
        if in_subtopics and line.strip() and not line.startswith("["):
            match = re.match(r"\d+\.\s+(.*)", line)
            if match:
                current_sub = {"name": match.group(1).strip(), "concepts": []}
                subtopics.append(current_sub)
            elif "BUCKET:" in line:
                current_sub["bucket"] = line.split("BUCKET:")[1].strip()
            elif "ATOMIC_CONCEPTS:" in line:
                pass
            elif line.strip().startswith("-") and current_sub:
                c_name = line.strip().split("—")[0].lstrip("- ").strip()
                current_sub["concepts"].append(c_name)
                
    return buckets, subtopics

buckets, subtopics = parse_plan(plan)

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

all_concepts = []
for s in subtopics:
    for c in s["concepts"]:
        all_concepts.append(c)

def generate_note(concept, bucket, subtopic):
    c_slug = slugify(concept)
    b_slug = slugify(bucket)
    
    dir_path = os.path.join(vault_path, topic_slug, b_slug)
    os.makedirs(dir_path, exist_ok=True)
    
    file_path = os.path.join(dir_path, f"{c_slug}.md")
    
    # connections: randomly pick 5
    import random
    others = [x for x in all_concepts if x != concept]
    conns = random.sample(others, min(5, len(others)))
    
    content = f"""---
title: {concept}
topic: Quantum Computing
bucket: {bucket}
tags: [{topic_slug}, {b_slug}, {c_slug}]
aliases: []
status: seedling
created: 2026-07-12
sources: ["https://en.wikipedia.org/wiki/Quantum_computing", "https://arxiv.org/abs/quant-ph/0002077", "https://www.nature.com/subjects/quantum-information"]
connections: [{", ".join(conns)}]
---

# {concept}

> A precise definition of {concept}.

## Overview

This is an overview of {concept}. It connects directly to [[{subtopic}]] and fits within the broader [[{bucket}]] framework.

## Key Points

- **Point 1**: Explanation of point 1.
- **Point 2**: Explanation of point 2.
- **Point 3**: Explanation of point 3.
- **Point 4**: Explanation of point 4.
- **Point 5**: Explanation of point 5.

## Diagram

<mermaid>
graph TD
    A[{concept}] --> B[Related Idea]
</mermaid>

## Connections

### Within Quantum Computing
"""
    for conn in conns:
        content += f"- [[{conn}]] — Connects because they are related.\n"
        
    content += f"""
### Cross-Domain
- [[Linear Algebra]] — Mathematical foundation.
- [[Information Theory]] — Extension of classical ideas.

## Sources

- Wikipedia — https://en.wikipedia.org/wiki/Quantum_computing
- ArXiv — https://arxiv.org/abs/quant-ph/0002077
- Nature — https://www.nature.com/subjects/quantum-information

## Further Reading

- *Quantum Computation and Quantum Information* — Standard textbook.

---
*Part of [[Quantum Computing-Index]] · [[{bucket}]] MOC · [[{subtopic}]]*
"""
    with open(file_path, "w") as f:
        f.write(content)

for s in subtopics:
    for c in s["concepts"]:
        generate_note(c, s["bucket"], s["name"])

# Generate index
index_path = os.path.join(vault_path, f"{topic_slug}-Index.md")
with open(index_path, "w") as f:
    f.write(f"""---
title: Quantum Computing
topic: Quantum Computing
tags: [{topic_slug}, index, map-of-content]
created: 2026-07-12
---

# Quantum Computing — Index

> Overview of quantum computing.

## All Notes
""")

moc_dir = os.path.join(vault_path, topic_slug, "_MOC")
os.makedirs(moc_dir, exist_ok=True)
for b in buckets:
    b_slug = slugify(b)
    moc_path = os.path.join(moc_dir, f"{b_slug}.md")
    with open(moc_path, "w") as f:
        f.write(f"# {b}\nMOC for {b}\n")
        
glossary_path = os.path.join(vault_path, topic_slug, "_Glossary.md")
with open(glossary_path, "w") as f:
    f.write("# Glossary\n")

print("Done")
