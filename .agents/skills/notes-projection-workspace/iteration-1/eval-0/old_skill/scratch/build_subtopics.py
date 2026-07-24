import os

vault_path = "/home/ali/v2/.agents/skills/notes-projection-workspace/iteration-1/eval-0/old_skill/outputs"
topic_slug = "the-pygmalion-effect"
topic_dir = os.path.join(vault_path, topic_slug)
mocs_dir = os.path.join(topic_dir, "_MOC")
subtopics_dir = os.path.join(topic_dir, "subtopics")

os.makedirs(mocs_dir, exist_ok=True)
os.makedirs(subtopics_dir, exist_ok=True)

subtopics_data = [
    {
        "title": "Historical Context",
        "bucket": "Foundations",
        "bucket_slug": "foundations",
        "desc": "The mythological, biographical, and pre-experimental background of expectancy research.",
        "concepts": ["Ovid's Metamorphoses Myth", "Robert Rosenthal", "Lenore Jacobson"]
    },
    {
        "title": "The Landmark Experiment",
        "bucket": "Foundations",
        "bucket_slug": "foundations",
        "desc": "The details, design, and initial findings of the classic 1968 classroom study.",
        "concepts": ["Oak School Study", "Intellectual Bloomers Label", "Pygmalion in the Classroom"]
    },
    {
        "title": "Fundamental Theory",
        "bucket": "Foundations",
        "bucket_slug": "foundations",
        "desc": "The broader sociological and psychological frameworks that encompass the effect.",
        "concepts": ["Self-Fulfilling Prophecy", "Interpersonal Expectancy Effects"]
    },
    {
        "title": "The Four-Factor Model",
        "bucket": "Mechanisms",
        "bucket_slug": "mechanisms",
        "desc": "The communication channels identified by Rosenthal through which expectations are transmitted.",
        "concepts": ["Climate Factor", "Input Factor", "Output Factor", "Feedback Factor"]
    },
    {
        "title": "Psychological and Cognitive Cycles",
        "bucket": "Mechanisms",
        "bucket_slug": "mechanisms",
        "desc": "The cognitive loops and mental frameworks that sustain expectancy effects.",
        "concepts": ["The Pygmalion Cycle", "Expectancy Bias", "Social Identity Theory Connection"]
    },
    {
        "title": "Organizational and Educational Domains",
        "bucket": "Applications and Critiques",
        "bucket_slug": "applications-and-critiques",
        "desc": "How the Pygmalion Effect manifests and is utilized in schools, businesses, and coaching.",
        "concepts": ["Pygmalion in Management", "Sports and Coaching Expectations", "Medical and Nursing Care"]
    },
    {
        "title": "Counterparts and Related Phenomena",
        "bucket": "Applications and Critiques",
        "bucket_slug": "applications-and-critiques",
        "desc": "Psychological effects that mirror, oppose, or interact with Pygmalion dynamics.",
        "concepts": ["The Galatea Effect", "The Golem Effect", "Halo and Horns Effects"]
    },
    {
        "title": "Scientific Evaluation and Ethics",
        "bucket": "Applications and Critiques",
        "bucket_slug": "applications-and-critiques",
        "desc": "The controversies, replication history, and ethical challenges surrounding expectancy studies.",
        "concepts": ["Replication and Methodological Critiques", "Labeling and Ethical Implications", "Pygmalion Effect Mitigation"]
    }
]

# Write subtopic files
for st in subtopics_data:
    st_slug = st['title'].lower().replace(" ", "-").replace("'", "")
    st_file = os.path.join(subtopics_dir, f"{st_slug}.md")
    
    lines = []
    lines.append("---")
    lines.append(f"title: \"{st['title']}\"")
    lines.append("topic: \"The Pygmalion Effect\"")
    lines.append(f"bucket: \"{st['bucket']}\"")
    lines.append(f"tags: [the-pygmalion-effect, {st['bucket_slug']}, subtopic]")
    lines.append("status: seedling")
    lines.append("created: 2026-07-12")
    lines.append("---")
    lines.append("")
    lines.append(f"# {st['title']}")
    lines.append("")
    lines.append(f"> {st['desc']}")
    lines.append("")
    lines.append("## Concepts")
    lines.append("")
    for c in st['concepts']:
        lines.append(f"- [[{c}]]")
    lines.append("")
    lines.append("---")
    lines.append(f"*Part of [[The Pygmalion Effect-Index]] · [[{st['bucket']}]] MOC*")
    
    with open(st_file, "w") as f:
        f.write("\n".join(lines))

print(f"Successfully generated {len(subtopics_data)} subtopic notes.")
