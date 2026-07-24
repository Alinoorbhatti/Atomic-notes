import os

vault_path = "/home/ali/v2/.agents/skills/notes-projection-workspace/iteration-1/eval-0/old_skill/outputs"
topic_slug = "the-pygmalion-effect"
topic_dir = os.path.join(vault_path, topic_slug)
mocs_dir = os.path.join(topic_dir, "_MOC")

# MOC 1: Foundations
moc1_content = """---
title: Foundations — Map of Content
topic: The Pygmalion Effect
bucket: Foundations
tags: [the-pygmalion-effect, foundations, moc]
created: 2026-07-12
---

# Foundations

> The history, seminal studies, and theoretical origins of the phenomenon.

## Start here

- [[Self-Fulfilling Prophecy]] — The foundational sociological concept that underpins all interpersonal expectation effects.
- [[Oak School Study]] — The landmark 1968 classroom experiment that empirically demonstrated the phenomenon.

## Foundational concepts

- [[Ovid's Metamorphoses Myth]] — The classical Roman myth of a sculptor's desire bringing a statue to life, which gave the Pygmalion Effect its name.
- [[Robert Rosenthal]] — The Harvard psychologist who pioneered expectancy research and co-directed the classroom study.
- [[Lenore Jacobson]] — The elementary school principal who co-authored the book and facilitated the experiment in her school.

## Mechanisms / deeper dives

- [[Interpersonal Expectancy Effects]] — The broader psychological class of expectancy and experimenter bias.
- [[Intellectual Bloomers Label]] — The cognitive trigger used to manipulate teacher expectancies in the study.
- [[Pygmalion in the Classroom]] — The published book that detailed the study and sparked national debate on educational equity.

---
*Part of [[The Pygmalion Effect-Index]]*"""

# MOC 2: Mechanisms
moc2_content = """---
title: Mechanisms — Map of Content
topic: The Pygmalion Effect
bucket: Mechanisms
tags: [the-pygmalion-effect, mechanisms, moc]
created: 2026-07-12
---

# Mechanisms

> The behavioral, cognitive, and communicative processes that drive the effect.

## Start here

- [[The Pygmalion Cycle]] — The four-stage cyclical feedback loop showing how expectations shape performance.
- [[Climate Factor]] — The critical emotional warmth factor that forms the base of the communication channel.

## Foundational concepts

- [[Expectancy Bias]] — The cognitive bias where observers selectively interpret performance to match expectations.
- [[Social Identity Theory Connection]] — The theoretical intersection showing how group labels alter self-concept.

## Mechanisms / deeper dives

- [[Input Factor]] — The tendency to teach more material and offer harder assignments to high-expectancy subjects.
- [[Output Factor]] — The practice of giving high-expectancy individuals more participation opportunities.
- [[Feedback Factor]] — The qualitative difference in corrections and praise offered to individuals.

---
*Part of [[The Pygmalion Effect-Index]]*"""

# MOC 3: Applications and Critiques
moc3_content = """---
title: Applications and Critiques — Map of Content
topic: The Pygmalion Effect
bucket: Applications and Critiques
tags: [the-pygmalion-effect, applications-and-critiques, moc]
created: 2026-07-12
---

# Applications and Critiques

> Real-world implementations, negative counterparts, replication status, and ethical limits.

## Start here

- [[Pygmalion in Management]] — J. Sterling Livingston's classic business application of expectancy theory in HBR.
- [[The Golem Effect]] — The negative counterpart where low expectations lead to performance drops.

## Foundational concepts

- [[The Galatea Effect]] — The phenomenon where an individual's self-expectations drive performance.
- [[Halo and Horns Effects]] — The cognitive biases that initially skew manager and teacher impressions.

## Mechanisms / deeper dives

- [[Replication and Methodological Critiques]] — The scientific controversies and challenges in reproducing Oak School findings.
- [[Labeling and Ethical Implications]] — The moral concerns regarding expectation manipulation and stereotype threat.

## Applications / case studies

- [[Sports and Coaching Expectations]] — How athletic coaches unconsciously influence player development and self-efficacy.
- [[Medical and Nursing Care]] — How doctor/nurse beliefs and bedside manner affect patient recovery outcomes.
- [[Pygmalion Effect Mitigation]] — Practical strategies and rubrics to neutralize expectancy biases in organizations.

---
*Part of [[The Pygmalion Effect-Index]]*"""

with open(os.path.join(mocs_dir, "foundations.md"), "w") as f:
    f.write(moc1_content)

with open(os.path.join(mocs_dir, "mechanisms.md"), "w") as f:
    f.write(moc2_content)

with open(os.path.join(mocs_dir, "applications-and-critiques.md"), "w") as f:
    f.write(moc3_content)

print("MOCs written successfully.")
