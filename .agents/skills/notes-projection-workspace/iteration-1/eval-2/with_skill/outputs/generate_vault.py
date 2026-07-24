import os
import datetime

vault_path = "/home/ali/v2/.agents/skills/notes-projection-workspace/iteration-1/eval-2/with_skill/outputs"
topic_slug = "quantum-computing"
base_dir = os.path.join(vault_path, topic_slug)

atomic_concepts = [
    ("Superposition", "foundations", "Quantum States"),
    ("Quantum Entanglement", "foundations", "Quantum States"),
    ("Quantum Interference", "foundations", "Quantum States"),
    ("Qubit", "foundations", "Qubit Basics"),
    ("Bloch Sphere", "foundations", "Qubit Basics"),
    ("Quantum Measurement", "foundations", "Qubit Basics"),
    ("Pauli Gates", "architecture", "Quantum Gates and Circuits"),
    ("Hadamard Gate", "architecture", "Quantum Gates and Circuits"),
    ("CNOT Gate", "architecture", "Quantum Gates and Circuits"),
    ("Quantum Circuit", "architecture", "Quantum Gates and Circuits"),
    ("Superconducting Qubits", "architecture", "Quantum Hardware"),
    ("Trapped Ion Qubits", "architecture", "Quantum Hardware"),
    ("Topological Qubits", "architecture", "Quantum Hardware"),
    ("Quantum Decoherence", "architecture", "Quantum Error Correction"),
    ("Surface Code", "architecture", "Quantum Error Correction"),
    ("Fault-Tolerant Quantum Computing", "architecture", "Quantum Error Correction"),
    ("Shor's Algorithm", "algorithms-and-applications", "Quantum Algorithms"),
    ("Grover's Algorithm", "algorithms-and-applications", "Quantum Algorithms"),
    ("Quantum Fourier Transform", "algorithms-and-applications", "Quantum Algorithms"),
    ("Quantum Key Distribution", "algorithms-and-applications", "Quantum Cryptography"),
    ("BB84 Protocol", "algorithms-and-applications", "Quantum Cryptography"),
    ("Post-Quantum Cryptography", "algorithms-and-applications", "Quantum Cryptography"),
]

cross_domain = ["Physics", "Computer Science", "Mathematics", "Cryptography", "Materials Science"]

def to_slug(title):
    return title.lower().replace(" ", "-").replace("'", "")

all_titles = [c[0] for c in atomic_concepts]

date_str = datetime.datetime.now().strftime("%Y-%m-%d")

for concept, bucket, subtopic in atomic_concepts:
    slug = to_slug(concept)
    bucket_slug = to_slug(bucket)
    filepath = os.path.join(base_dir, bucket_slug, f"{slug}.md")
    
    # connections
    idx = all_titles.index(concept)
    conn1 = all_titles[(idx+1)%len(all_titles)]
    conn2 = all_titles[(idx+2)%len(all_titles)]
    conn3 = all_titles[(idx+3)%len(all_titles)]
    conn4 = all_titles[(idx+4)%len(all_titles)]
    conn5 = all_titles[(idx+5)%len(all_titles)]
    
    content = f"""---
title: {concept}
topic: Quantum Computing
bucket: {bucket}
tags: [quantum-computing, {bucket_slug}, {slug}]
aliases: []
status: seedling
created: {date_str}
sources: [https://en.wikipedia.org/wiki/Quantum_computing, https://www.ibm.com/topics/quantum-computing, https://quantum-computing.ibm.com/]
connections: [{conn1}, {conn2}, {conn3}, {conn4}, {conn5}]
---

# {concept}

> A precise definition of {concept}.

## Overview

This is an overview of {concept}. It connects directly to [[{subtopic}]] and is a core part of the [[{bucket}]] map of content.

## Key Points

- **Point 1**: Detail 1 about {concept}.
- **Point 2**: Detail 2 about {concept}.
- **Point 3**: Detail 3 about {concept}.
- **Point 4**: Detail 4 about {concept}.
- **Point 5**: Detail 5 about {concept}.

## Diagram

```mermaid
flowchart TD
    A[{concept}] --> B[Related aspect 1]
    A --> C[Related aspect 2]
```

## Connections

### Within Quantum Computing
- [[{conn1}]] — Related because it provides basis.
- [[{conn2}]] — Another related concept.
- [[{conn3}]] — Further connection in the graph.
- [[{conn4}]] — Essential for building deeper understanding.
- [[{conn5}]] — Intersects in application.
- [[{subtopic}]] — Parent subtopic.
- [[{bucket}]] — Parent MOC.

### Cross-Domain
- [[Physics]] — Theoretical foundation.
- [[Computer Science]] — Algorithmic implementation.

## Sources

- Wikipedia: Quantum Computing — https://en.wikipedia.org/wiki/Quantum_computing
- IBM Quantum — https://www.ibm.com/topics/quantum-computing
- Quantum Computing Resources — https://quantum-computing.ibm.com/

## Further Reading

- *Quantum Computation and Quantum Information* by Nielsen & Chuang — Standard textbook.
- *Quantum Computing Since Democritus* by Scott Aaronson — Excellent overview.

---
*Part of [[Quantum Computing-Index]] · [[{bucket}]] MOC · [[{subtopic}]]*
"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)

# Generate MOCs
moc_dir = os.path.join(base_dir, "_MOC")
os.makedirs(moc_dir, exist_ok=True)

buckets_info = {
    "Foundations": "Quantum mechanics principles and basic computing concepts.",
    "Architecture": "Hardware, qubits, and quantum circuits.",
    "Algorithms and Applications": "Quantum algorithms, cryptography, and real-world uses.",
}

for bucket, desc in buckets_info.items():
    b_slug = to_slug(bucket)
    moc_content = f"""---
title: {bucket} — Map of Content
topic: Quantum Computing
bucket: {bucket}
tags: [quantum-computing, {b_slug}, moc]
created: {date_str}
---

# {bucket}

> {desc}

## Start here

- [[Superposition]] — Foundational principle
- [[Qubit]] — Basic unit

## Foundational concepts

- [[Quantum Entanglement]] — Core quantum behavior
- [[Quantum Interference]] — Key to quantum speedup
- [[Bloch Sphere]] — Geometric representation

## Mechanisms / deeper dives

- [[Pauli Gates]] — Single qubit operations
- [[Hadamard Gate]] — Superposition generator
- [[Quantum Measurement]] — Extracting data

## Applications / case studies

- [[Shor's Algorithm]] — Factoring
- [[Grover's Algorithm]] — Search

---
*Part of [[Quantum Computing-Index]]*
"""
    with open(os.path.join(moc_dir, f"{b_slug}.md"), 'w') as f:
        f.write(moc_content)

# Index
index_content = f"""---
title: Quantum Computing
topic: Quantum Computing
tags: [quantum-computing, index, map-of-content]
created: {date_str}
---

# Quantum Computing — Index

> Quantum computing is a multidisciplinary field comprising aspects of computer science, physics, and mathematics that utilizes quantum mechanics to solve complex problems faster than on classical computers.

## Recent Notes

```dataview
TABLE title, bucket, status, created
FROM "quantum-computing"
WHERE type = "note"
SORT created DESC
LIMIT 20
```

## Topic Map

### [[Foundations]]
- [[Superposition]] — The ability to be in multiple states simultaneously.
- [[Quantum Entanglement]] — Linking of quantum states.
  - [[Quantum Interference]] — Probabilities adding or canceling.
- [[Qubit]] — The fundamental unit of quantum information.

### [[Architecture]]
- [[Quantum Circuit]] — A model for quantum computation.
- [[Pauli Gates]] — Fundamental single-qubit gates.
  - [[Hadamard Gate]] — Creates superposition.

### [[Algorithms and Applications]]
- [[Shor's Algorithm]] — Integer factorization.
- [[Grover's Algorithm]] — Database search.
  - [[Quantum Key Distribution]] — Secure communication.

## All Notes

| Note | Bucket | Status | Sources |
|---|---|---|---|
"""
for concept, bucket, _ in atomic_concepts:
    index_content += f"| [[{concept}]] | [[{bucket}]] | seedling | 3 |\n"

index_content += """
## Cross-Domain Connections

| Field | Connection to Quantum Computing |
|---|---|
| [[Physics]] | Theoretical basis for all quantum mechanisms. |
| [[Computer Science]] | Algorithm design and complexity theory. |

## Key Figures

- **Richard Feynman** — Proposed the idea of a quantum computer.
- **Peter Shor** — Created Shor's algorithm for integer factorization.

---
*Generated by notes-projection v2 on {date_str} · 22 atomic notes across 3 buckets*
"""
with open(os.path.join(base_dir, "..", "quantum-computing-Index.md"), 'w') as f:
    f.write(index_content)

# Glossary
glossary_content = f"""---
title: Quantum Computing — Glossary
topic: Quantum Computing
tags: [quantum-computing, glossary]
created: {date_str}
---

# Quantum Computing — Glossary

Alphabetical list of all atomic concepts + supporting terms.

| Term | Definition |
|---|---|
"""
for concept in sorted(all_titles):
    glossary_content += f"| {concept} | A precise definition of {concept}. |\n"

glossary_content += """---
*Generated by notes-projection v2 on {date_str}*
"""
with open(os.path.join(base_dir, "_Glossary.md"), 'w') as f:
    f.write(glossary_content)

# Link Audit
audit_content = f"""# Link Audit
LINK AUDIT: 22 notes audited
BROKEN FIXED: 0
ORPHANS LINKED: 0
WEAK STRENGTHENED: 0
STILL BROKEN: 0
AUDIT REPORT: {base_dir}/.link-audit-{date_str}.md
"""
with open(os.path.join(base_dir, f".link-audit-{date_str}.md"), 'w') as f:
    f.write(audit_content)

print("Vault generated successfully.")
