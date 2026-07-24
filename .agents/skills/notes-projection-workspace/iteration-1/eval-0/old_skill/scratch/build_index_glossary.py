import os

vault_path = "/home/ali/v2/.agents/skills/notes-projection-workspace/iteration-1/eval-0/old_skill/outputs"
topic_slug = "the-pygmalion-effect"
topic_dir = os.path.join(vault_path, topic_slug)

concepts_info = [
    {"title": "Ovid's Metamorphoses Myth", "bucket": "Foundations", "slug": "ovids-metamorphoses-myth", "sources": 3},
    {"title": "Robert Rosenthal", "bucket": "Foundations", "slug": "robert-rosenthal", "sources": 3},
    {"title": "Lenore Jacobson", "bucket": "Foundations", "slug": "lenore-jacobson", "sources": 3},
    {"title": "Oak School Study", "bucket": "Foundations", "slug": "oak-school-study", "sources": 3},
    {"title": "Intellectual Bloomers Label", "bucket": "Foundations", "slug": "intellectual-bloomers-label", "sources": 3},
    {"title": "Pygmalion in the Classroom", "bucket": "Foundations", "slug": "pygmalion-in-the-classroom", "sources": 3},
    {"title": "Self-Fulfilling Prophecy", "bucket": "Foundations", "slug": "self-fulfilling-prophecy", "sources": 3},
    {"title": "Interpersonal Expectancy Effects", "bucket": "Foundations", "slug": "interpersonal-expectancy-effects", "sources": 3},
    {"title": "Climate Factor", "bucket": "Mechanisms", "slug": "climate-factor", "sources": 3},
    {"title": "Input Factor", "bucket": "Mechanisms", "slug": "input-factor", "sources": 3},
    {"title": "Output Factor", "bucket": "Mechanisms", "slug": "output-factor", "sources": 3},
    {"title": "Feedback Factor", "bucket": "Mechanisms", "slug": "feedback-factor", "sources": 3},
    {"title": "The Pygmalion Cycle", "bucket": "Mechanisms", "slug": "the-pygmalion-cycle", "sources": 3},
    {"title": "Expectancy Bias", "bucket": "Mechanisms", "slug": "expectancy-bias", "sources": 3},
    {"title": "Social Identity Theory Connection", "bucket": "Mechanisms", "slug": "social-identity-theory-connection", "sources": 3},
    {"title": "Pygmalion in Management", "bucket": "Applications and Critiques", "slug": "pygmalion-in-management", "sources": 3},
    {"title": "Sports and Coaching Expectations", "bucket": "Applications and Critiques", "slug": "sports-and-coaching-expectations", "sources": 3},
    {"title": "Medical and Nursing Care", "bucket": "Applications and Critiques", "slug": "medical-and-nursing-care", "sources": 3},
    {"title": "The Galatea Effect", "bucket": "Applications and Critiques", "slug": "the-galatea-effect", "sources": 3},
    {"title": "The Golem Effect", "bucket": "Applications and Critiques", "slug": "the-golem-effect", "sources": 3},
    {"title": "Halo and Horns Effects", "bucket": "Applications and Critiques", "slug": "halo-and-horns-effects", "sources": 3},
    {"title": "Replication and Methodological Critiques", "bucket": "Applications and Critiques", "slug": "replication-and-methodological-critiques", "sources": 3},
    {"title": "Labeling and Ethical Implications", "bucket": "Applications and Critiques", "slug": "labeling-and-ethical-implications", "sources": 3},
    {"title": "Pygmalion Effect Mitigation", "bucket": "Applications and Critiques", "slug": "pygmalion-effect-mitigation", "sources": 3}
]

# Build the master index
index_lines = [
    "---",
    "title: \"The Pygmalion Effect\"",
    "topic: \"The Pygmalion Effect\"",
    "tags: [the-pygmalion-effect, index, map-of-content]",
    "created: 2026-07-12",
    "---",
    "",
    "# The Pygmalion Effect — Index",
    "",
    "> The Pygmalion Effect is a psychological phenomenon where higher expectations placed upon individuals lead to an increase in their performance. It operates as a self-fulfilling prophecy, where beliefs about an individual's potential influence behavior in ways that make the expected outcome reality.",
    "",
    "## Recent Notes",
    "",
    "```dataview",
    "TABLE title, bucket, status, created",
    'FROM "the-pygmalion-effect"',
    'WHERE type = "note"',
    "SORT created DESC",
    "LIMIT 20",
    "```",
    "",
    "## Topic Map",
    "",
    "### [[Foundations]]",
    "- [[Self-Fulfilling Prophecy]] — Robert K. Merton's foundational sociological concept of beliefs shaping reality.",
    "- [[Oak School Study]] — The methodology and design of the 1968 elementary school experiment.",
    "  - [[Ovid's Metamorphoses Myth]] — The Greek myth of Pygmalion and Galatea that inspired the effect's name.",
    "  - [[Robert Rosenthal]] — The psychologist whose research on experimenter expectancy effects laid the groundwork.",
    "  - [[Lenore Jacobson]] — The school principal who co-authored the seminal classroom study.",
    "  - [[Intellectual Bloomers Label]] — The random designation used to deceive teachers and manipulate expectations.",
    "  - [[Pygmalion in the Classroom]] — The seminal 1968 book detailing the research and its immediate cultural reception.",
    "- [[Interpersonal Expectancy Effects]] — The general psychological theory of how one person's expectations influence another.",
    "",
    "### [[Mechanisms]]",
    "- [[The Pygmalion Cycle]] — The cyclical, four-step loop connecting expectation, behavior, self-belief, and performance.",
    "- [[Climate Factor]] — The creation of a warmer social-emotional environment through non-verbal cues.",
    "  - [[Input Factor]] — The tendency to teach more material and offer more difficult tasks to high-expectancy individuals.",
    "  - [[Output Factor]] — Offering more opportunities to respond, speak, and participate.",
    "  - [[Feedback Factor]] — Providing more detailed, constructive feedback and praise for performance.",
    "- [[Expectancy Bias]] — The cognitive distortion where observers see what they expect to see, reinforcing beliefs.",
    "- [[Social Identity Theory Connection]] — How being labeled affects a person's self-concept and social identification.",
    "",
    "### [[Applications and Critiques]]",
    "- [[Pygmalion in Management]] — J. Sterling Livingston's application of the effect to corporate leadership.",
    "- [[The Golem Effect]] — The negative counterpart where low expectations lead to diminished performance.",
    "  - [[The Galatea Effect]] — The phenomenon where an individual's self-expectations directly drive their own performance.",
    "  - [[Halo and Horns Effects]] — Cognitive biases where overall impressions influence specific performance judgments.",
    "  - [[Sports and Coaching Expectations]] — The impact of coach perceptions on athletic self-efficacy and performance.",
    "  - [[Medical and Nursing Care]] — How clinical expectations influence patient recovery rates and caregiver attentiveness.",
    "  - [[Replication and Methodological Critiques]] — The scientific debates and challenges in replicating the original study.",
    "  - [[Labeling and Ethical Implications]] — The moral and practical concerns of expectation manipulation and stereotyping.",
    "  - [[Pygmalion Effect Mitigation]] — Strategies and techniques to reduce negative expectancy biases in professional settings.",
    "",
    "## All Notes",
    "",
    "| Note | Bucket | Status | Sources |",
    "|---|---|---|---|",
]

for c in concepts_info:
    index_lines.append(f"| [[{c['title']}]] | [[{c['bucket']}]] | seedling | {c['sources']} |")

index_lines.extend([
    "",
    "## Cross-Domain Connections",
    "",
    "| Field | Connection to The Pygmalion Effect |",
    "|---|---|",
    "| [[Sociology]] | Explores how group expectations and structural positions generate self-fulfilling prophecies. |",
    "| [[Educational Psychology]] | Focuses on teacher behavior, curriculum design, and student motivation. |",
    "| [[Organizational Behavior]] | Studies leadership styles, employee engagement, and corporate culture. |",
    "| [[Sports Psychology]] | Investigates athletic motivation, coach-athlete relationships, and performance anxiety. |",
    "| [[Behavioral Economics]] | Examines how market beliefs and expectations drive economic performance and bubbles. |",
    "| [[Clinical Psychology]] | Studies patient-therapist expectations and their role in therapeutic outcomes. |",
    "",
    "## Key Figures",
    "",
    "- **Robert Rosenthal** — Lead psychologist who pioneered experimenter and interpersonal expectancy research.",
    "- **Lenore Jacobson** — Principal of West Park School who co-authored the seminal classroom study.",
    "- **Robert K. Merton** — Sociologist who coined the term and defined the concept of the self-fulfilling prophecy.",
    "- **J. Sterling Livingston** — Harvard Business Review author who popularized Pygmalion dynamics in management.",
    "- **Edward Thorndike** — Cognitive psychologist who criticized the Oak School study's IQ test methodology.",
    "- **Donald Rubin** — Statistician who analyzed the statistical validity of early expectancy studies.",
    "- **Elisha Babad** — Researcher who investigated the Golem effect and teacher nonverbal behavior.",
    "- **Albert Bandura** — Psychologist whose self-efficacy theory explains Galatea effect mechanisms.",
    "",
    "---",
    "*Generated by notes-projection v2 on 2026-07-12 · 24 atomic notes across 3 buckets*"
])

# Write index file
index_path = os.path.join(vault_path, "the-pygmalion-effect-Index.md")
with open(index_path, "w") as f:
    f.write("\n".join(index_lines))


# Build the glossary
glossary_lines = [
    "---",
    "title: \"The Pygmalion Effect — Glossary\"",
    "topic: \"The Pygmalion Effect\"",
    "tags: [the-pygmalion-effect, glossary]",
    "created: 2026-07-12",
    "---",
    "",
    "# The Pygmalion Effect — Glossary",
    "",
    "Alphabetical list of all atomic concepts + supporting terms.",
    "",
    "| Term | Definition |",
    "|---|---|",
]

# Fetch definitions from concepts
glossary_entries = [
    ("Ovid's Metamorphoses Myth", "The Greek myth of Pygmalion and Galatea that inspired the effect's name."),
    ("Robert Rosenthal", "The psychologist whose research on experimenter expectancy effects laid the groundwork."),
    ("Lenore Jacobson", "The school principal who co-authored the seminal classroom study."),
    ("Oak School Study", "The methodology and design of the 1968 elementary school experiment."),
    ("Intellectual Bloomers Label", "The random designation used to deceive teachers and manipulate expectations."),
    ("Pygmalion in the Classroom", "The seminal 1968 book detailing the research and its immediate cultural reception."),
    ("Self-Fulfilling Prophecy", "Robert K. Merton's foundational sociological concept of beliefs shaping reality."),
    ("Interpersonal Expectancy Effects", "The general psychological theory of how one person's expectations influence another."),
    ("Climate Factor", "The creation of a warmer social-emotional environment through non-verbal cues."),
    ("Input Factor", "The tendency to teach more material and offer more difficult tasks to high-expectancy individuals."),
    ("Output Factor", "Offering more opportunities to respond, speak, and participate."),
    ("Feedback Factor", "Providing more detailed, constructive feedback and praise for performance."),
    ("The Pygmalion Cycle", "The cyclical, four-step loop connecting expectation, behavior, self-belief, and performance."),
    ("Expectancy Bias", "The cognitive distortion where observers see what they expect to see, reinforcing beliefs."),
    ("Social Identity Theory Connection", "How being labeled affects a person's self-concept and social identification."),
    ("Pygmalion in Management", "J. Sterling Livingston's application of the effect to corporate leadership."),
    ("Sports and Coaching Expectations", "The impact of coach perceptions on athletic self-efficacy and performance."),
    ("Medical and Nursing Care", "How clinical expectations influence patient recovery rates and caregiver attentiveness."),
    ("The Galatea Effect", "The phenomenon where an individual's self-expectations directly drive their own performance."),
    ("The Golem Effect", "The negative counterpart where low expectations lead to diminished performance."),
    ("Halo and Horns Effects", "Cognitive biases where overall impressions influence specific performance judgments."),
    ("Replication and Methodological Critiques", "The scientific debates and challenges in replicating the original study."),
    ("Labeling and Ethical Implications", "The moral and practical concerns of expectation manipulation and stereotyping."),
    ("Pygmalion Effect Mitigation", "Strategies and techniques to reduce negative expectancy biases in professional settings."),
    ("Double-Blind Study", "A study design where neither participants nor researchers know who is in the control group."),
    ("Experimenter Expectancy Effect", "A bias where the researcher's expectations unconsciously influence the participants."),
    ("Self-Efficacy", "An individual's belief in their capacity to execute behaviors necessary to produce specific performance attainments.")
]

# Sort alphabetically
glossary_entries.sort(key=lambda x: x[0])

for entry in glossary_entries:
    glossary_lines.append(f"| {entry[0]} | {entry[1]} |")

glossary_lines.extend([
    "",
    "---",
    "*Generated by notes-projection v2 on 2026-07-12*"
])

# Write glossary file
glossary_path = os.path.join(topic_dir, "_Glossary.md")
with open(glossary_path, "w") as f:
    f.write("\n".join(glossary_lines))

print("Index and Glossary written successfully.")
