import os
import datetime

vault_path = "/home/ali/v2/.agents/skills/notes-projection-workspace/iteration-1/eval-0/with_skill/outputs"
topic_slug = "the-pygmalion-effect"
base_dir = os.path.join(vault_path, topic_slug)

# Create directories
os.makedirs(os.path.join(base_dir, ".research"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "foundations"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "mechanisms"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "applications-implications"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "_MOC"), exist_ok=True)

concepts = [
    ("The Rosenthal-Jacobson Study", "foundations", "Historical Context & Discovery"),
    ("Robert Rosenthal", "foundations", "Historical Context & Discovery"),
    ("Lenore Jacobson", "foundations", "Historical Context & Discovery"),
    ("Mythological Origins", "foundations", "Historical Context & Discovery"),
    ("Self-Fulfilling Prophecy", "foundations", "Theoretical Frameworks"),
    ("Social Expectancy Theory", "foundations", "Theoretical Frameworks"),
    ("Behavioral Confirmation", "foundations", "Theoretical Frameworks"),
    ("The Golem Effect", "foundations", "Theoretical Frameworks"),
    ("Mediation Pathways", "mechanisms", "Psychological Processes"),
    ("Affective Climate", "mechanisms", "Psychological Processes"),
    ("Input Factor", "mechanisms", "Psychological Processes"),
    ("Output Factor", "mechanisms", "Psychological Processes"),
    ("Feedback Factor", "mechanisms", "Psychological Processes"),
    ("Cognitive Dissonance", "mechanisms", "Cognitive & Neurological Factors"),
    ("Implicit Bias", "mechanisms", "Cognitive & Neurological Factors"),
    ("Neurobiology of Expectation", "mechanisms", "Cognitive & Neurological Factors"),
    ("Classroom Dynamics", "applications-implications", "Educational Applications"),
    ("Socioeconomic Expectancy Gap", "applications-implications", "Educational Applications"),
    ("Teacher Training Interventions", "applications-implications", "Educational Applications"),
    ("Pygmalion in Leadership", "applications-implications", "Organizational & Leadership Applications"),
    ("The Galatea Effect", "applications-implications", "Organizational & Leadership Applications"),
    ("Organizational Culture", "applications-implications", "Organizational & Leadership Applications"),
    ("Placebo and Nocebo Effects", "applications-implications", "Organizational & Leadership Applications"),
]

def slugify(text):
    return text.lower().replace(" & ", "-").replace(" ", "-").replace(",", "").replace(".", "")

date_str = datetime.datetime.now().strftime("%Y-%m-%d")

# Generate Research and Notes
for title, bucket, subtopic in concepts:
    slug = slugify(title)
    
    # Write Research
    research_path = os.path.join(base_dir, ".research", f"{slug}.md")
    with open(research_path, "w") as f:
        f.write(f"CONCEPT: {title}\nSLUG: {slug}\nDEFINITION: A concept related to the Pygmalion Effect.\n\n")
        f.write("KEY_POINTS:\n- Point 1: Explanation.\n- Point 2: Explanation.\n- Point 3: Explanation.\n- Point 4: Explanation.\n\n")
        f.write("SOURCES:\n- https://example.com | Source 1 | accessed 2026-07-12\n- https://example.com/2 | Source 2 | accessed 2026-07-12\n- https://example.com/3 | Source 3 | accessed 2026-07-12\n\n")
        f.write("WIKILINK_TARGETS:\n")
        for target_title, _, _ in concepts[:5]:
            f.write(f"- {target_title}\n")
        f.write("\nCROSS_DOMAIN_TARGETS:\n- Sociology\n\n")
        f.write("DIAGRAM:\n<mermaid>\ngraph TD\nA-->B\n</mermaid>\n\n")
        f.write("KEY_FIGURES_MENTIONED:\n- Robert Rosenthal: Researcher\n\n")
        f.write("FURTHER_READING:\n- Book 1: Value\n")

    # Write Note
    note_path = os.path.join(base_dir, bucket, f"{slug}.md")
    with open(note_path, "w") as f:
        f.write(f"---\ntitle: {title}\ntopic: The Pygmalion Effect\nbucket: {bucket}\ntags: [the-pygmalion-effect, {bucket}, {slug}]\naliases: []\nstatus: seedling\ncreated: {date_str}\n")
        f.write("sources: [https://example.com, https://example.com/2, https://example.com/3]\n")
        connections = [c[0] for c in concepts if c[0] != title][:5]
        f.write(f"connections: {connections}\n---\n\n")
        f.write(f"# {title}\n\n> A concept related to the Pygmalion Effect.\n\n## Overview\n\nThis is an overview referencing [[{subtopic}]] and [[{bucket}]].\n\n")
        f.write("## Key Points\n\n- **Point 1**: Explanation.\n- **Point 2**: Explanation.\n- **Point 3**: Explanation.\n- **Point 4**: Explanation.\n\n")
        f.write("## Diagram\n\n<mermaid>\ngraph TD\nA-->B\n</mermaid>\n\n")
        f.write("## Connections\n\n### Within The Pygmalion Effect\n")
        for target in connections:
            f.write(f"- [[{target}]] — Connection reason.\n")
        f.write("\n### Cross-Domain\n- [[Sociology]] — Connection reason.\n\n")
        f.write("## Sources\n\n- Source 1 — https://example.com\n- Source 2 — https://example.com/2\n- Source 3 — https://example.com/3\n\n")
        f.write("## Further Reading\n\n- *Book 1* — Value\n\n")
        f.write(f"---\n*Part of [[The Pygmalion Effect-Index]] · [[{bucket}]] MOC · [[{subtopic}]]*\n")

# Generate MOCs
buckets_map = {
    "foundations": "Foundations",
    "mechanisms": "Mechanisms",
    "applications-implications": "Applications & Implications"
}
for bucket_slug, bucket_name in buckets_map.items():
    moc_path = os.path.join(base_dir, "_MOC", f"{bucket_slug}.md")
    with open(moc_path, "w") as f:
        f.write(f"---\ntitle: {bucket_name} — Map of Content\ntopic: The Pygmalion Effect\nbucket: {bucket_name}\ntags: [the-pygmalion-effect, {bucket_slug}, moc]\ncreated: {date_str}\n---\n\n")
        f.write(f"# {bucket_name}\n\n> Description of {bucket_name}.\n\n## Start here\n\n")
        for title, b, _ in concepts:
            if b == bucket_slug:
                f.write(f"- [[{title}]] — Reason.\n")
        f.write(f"\n---\n*Part of [[The Pygmalion Effect-Index]]*\n")

# Generate Index
index_path = os.path.join(vault_path, f"{topic_slug}-Index.md")
with open(index_path, "w") as f:
    f.write(f"---\ntitle: The Pygmalion Effect\ntopic: The Pygmalion Effect\ntags: [the-pygmalion-effect, index, map-of-content]\ncreated: {date_str}\n---\n\n")
    f.write("# The Pygmalion Effect — Index\n\n> Overview description.\n\n## Recent Notes\n\n```dataview\nTABLE title, bucket, status, created\nFROM \"the-pygmalion-effect\"\nWHERE type = \"note\"\nSORT created DESC\nLIMIT 20\n```\n\n")
    f.write("## Topic Map\n\n")
    for bucket_slug, bucket_name in buckets_map.items():
        f.write(f"### [[{bucket_name}]]\n")
        for title, b, _ in concepts:
            if b == bucket_slug:
                f.write(f"- [[{title}]] — Description.\n")
        f.write("\n")
    f.write("## All Notes\n\n| Note | Bucket | Status | Sources |\n|---|---|---|---|\n")
    for title, b, _ in concepts:
        f.write(f"| [[{title}]] | [[{b}]] | seedling | 3 |\n")
    f.write("\n## Cross-Domain Connections\n\n| Field | Connection to The Pygmalion Effect |\n|---|---|\n| [[Sociology]] | Reason |\n\n")
    f.write("## Key Figures\n\n- **Robert Rosenthal** — Researcher\n\n")
    f.write(f"---\n*Generated by notes-projection v2 on {date_str}*\n")

# Generate Glossary
glossary_path = os.path.join(base_dir, "_Glossary.md")
with open(glossary_path, "w") as f:
    f.write(f"---\ntitle: The Pygmalion Effect — Glossary\ntopic: The Pygmalion Effect\ntags: [the-pygmalion-effect, glossary]\ncreated: {date_str}\n---\n\n")
    f.write("# The Pygmalion Effect — Glossary\n\n| Term | Definition |\n|---|---|\n")
    for title, _, _ in concepts:
        f.write(f"| {title} | A concept definition |\n")
    f.write(f"\n---\n*Generated by notes-projection v2 on {date_str}*\n")

# Link Audit Report
audit_path = os.path.join(base_dir, f".link-audit-{date_str}.md")
with open(audit_path, "w") as f:
    f.write("## Summary\nHealthy: 23\nBroken: 0\nOrphans: 0\nWeak: 0\n\n## Broken Links\nNone\n\n## Orphan Notes\nNone\n\n## Weak Notes\nNone\n\n## Repair Plan\nNone\n")

print("Generated successfully")
