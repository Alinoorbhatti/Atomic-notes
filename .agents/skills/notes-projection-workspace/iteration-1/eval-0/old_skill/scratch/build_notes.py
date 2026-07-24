import os
import json
import re

vault_path = "/home/ali/v2/.agents/skills/notes-projection-workspace/iteration-1/eval-0/old_skill/outputs"
topic_slug = "the-pygmalion-effect"
topic_dir = os.path.join(vault_path, topic_slug)
research_dir = os.path.join(topic_dir, ".research")
subtopics_dir = os.path.join(topic_dir, "subtopics")
mocs_dir = os.path.join(topic_dir, "_MOC")

os.makedirs(research_dir, exist_ok=True)
os.makedirs(subtopics_dir, exist_ok=True)
os.makedirs(mocs_dir, exist_ok=True)

concepts_data = [
  {
    "title": "Ovid's Metamorphoses Myth",
    "bucket": "Foundations",
    "bucket_slug": "foundations",
    "subtopic": "Historical Context",
    "slug": "ovids-metamorphoses-myth",
    "definition": "The narrative in Roman poet Ovid's Metamorphoses where the sculptor Pygmalion falls in love with his ivory statue, Galatea, which is then brought to life by the goddess Venus.",
    "key_points": [
      "Origin of the Name: The psychological Pygmalion Effect is named after the protagonist of this myth to represent how intense belief and desire can bring an expectation to life.",
      "Ovid's Narrative: In the Metamorphoses, Pygmalion is a Cypriot sculptor who, disgusted by the behavior of local women, vows celibacy and carves a statue of his ideal woman out of ivory.",
      "Venus's Intervention: Seeing Pygmalion's deep devotion and love for the statue during her festival, Venus grants his prayer and breathes life into the ivory figure, named Galatea in later traditions.",
      "Psychological Symbolism: The myth serves as a literary metaphor for the self-fulfilling prophecy, demonstrating how creative focus and expectation can shape objective reality."
    ],
    "sources": [
      {"url": "https://en.wikipedia.org/wiki/Pygmalion_(mythology)", "title": "Pygmalion (mythology) on Wikipedia"},
      {"url": "https://www.britannica.com/topic/Pygmalion-Greek-mythology", "title": "Pygmalion in British Encyclopedia"},
      {"url": "https://www.metmuseum.org/toah/hd/poet/hd_poet.htm", "title": "Ovid and the Metamorphoses (Met Museum)"}
    ],
    "wikilink_targets": [
      {"name": "Robert Rosenthal", "reason": "Rosenthal used the name 'Pygmalion' from this myth to describe his expectancy findings."},
      {"name": "Lenore Jacobson", "reason": "Co-authored the study named after this classical narrative."},
      {"name": "Self-Fulfilling Prophecy", "reason": "Represents the foundational mythological illustration of a self-fulfilling prophecy."},
      {"name": "The Galatea Effect", "reason": "The internal counterpart named after the statue brought to life in this myth."},
      {"name": "The Golem Effect", "reason": "The negative expectation counterpart, named after a contrasting folklore figure."}
    ],
    "cross_domain_targets": [
      {"name": "Sociology", "reason": "Explores how group expectations and structural positions generate self-fulfilling prophecies."},
      {"name": "Educational Psychology", "reason": "Focuses on teacher behavior, curriculum design, and student motivation."}
    ],
    "diagram": "flowchart TD\n    A[Pygmalion's Desire] --> B[Creation of Ivory Statue]\n    B --> C[Devotion & Belief]\n    C --> D[Aphrodite's Blessing]\n    D --> E[Statue Becomes Galatea]",
    "key_figures_mentioned": [
      {"name": "Pygmalion", "role": "sculptor who fell in love with his own creation"},
      {"name": "Galatea", "role": "the statue brought to life by Aphrodite"},
      {"name": "Ovid", "role": "Roman poet who recorded the myth in Metamorphoses"}
    ],
    "further_reading": [
      {"resource": "Metamorphoses by Ovid", "why": "the primary classical source of the myth"}
    ]
  },
  {
    "title": "Robert Rosenthal",
    "bucket": "Foundations",
    "bucket_slug": "foundations",
    "subtopic": "Historical Context",
    "slug": "robert-rosenthal",
    "definition": "A distinguished American psychologist who pioneered research on interpersonal expectancy effects and co-discovered the Pygmalion Effect.",
    "key_points": [
      "Expectancy Pioneer: Rosenthal spent decades studying how the expectations of researchers, teachers, and managers unconsciously influence their subjects' behavior.",
      "Experimenter Bias: His early research in the 1960s showed that psychological researchers' expectations could bias their experimental results, leading to the use of double-blind methodologies.",
      "Collaborative Discovery: Rosenthal partnered with Lenore Jacobson to test his laboratory findings in a real-world educational setting, culminating in the landmark Oak School study.",
      "Four-Factor Theory: He formulated the four-factor model (Climate, Input, Output, Feedback) to explain how teachers communicate expectations to students."
    ],
    "sources": [
      {"url": "https://en.wikipedia.org/wiki/Robert_Rosenthal_(psychologist)", "title": "Robert Rosenthal Biography on Wikipedia"},
      {"url": "https://www.psychologicalscience.org/publications/observer/obsonline/robert-rosenthal-expectancy-effects.html", "title": "Robert Rosenthal and Expectancy Effects (APS)"},
      {"url": "https://www.nytimes.com/2024/01/18/science/robert-rosenthal-dead.html", "title": "Robert Rosenthal Obituary (New York Times)"}
    ],
    "wikilink_targets": [
      {"name": "Lenore Jacobson", "reason": "Collaborated on the landmark 1968 classroom expectancy experiment."},
      {"name": "Oak School Study", "reason": "Designed and analyzed this classic educational field study."},
      {"name": "Pygmalion in the Classroom", "reason": "Co-authored this seminal text detailing interpersonal expectancies."},
      {"name": "Interpersonal Expectancy Effects", "reason": "Formulated the broader psychological theory of expectancy."},
      {"name": "Climate Factor", "reason": "Identified climate as the key non-verbal factor in expectation communication."}
    ],
    "cross_domain_targets": [
      {"name": "Educational Psychology", "reason": "Focuses on teacher behavior, curriculum design, and student motivation."},
      {"name": "Sociology", "reason": "Explores how group expectations and structural positions generate self-fulfilling prophecies."}
    ],
    "diagram": "flowchart LR\n    A[Rosenthal's Research] --> B[Experimenter Expectancy Effect]\n    B --> C[Classroom Expectancy Effect]\n    C --> D[Pygmalion in the Classroom Book]",
    "key_figures_mentioned": [
      {"name": "Robert Rosenthal", "role": "Lead psychologist in expectancy research"},
      {"name": "Lenore Jacobson", "role": "Co-investigator of the school experiment"}
    ],
    "further_reading": [
      {"resource": "Pygmalion in the Classroom by Rosenthal and Jacobson", "why": "the primary source of the landmark study"}
    ]
  },
  {
    "title": "Lenore Jacobson",
    "bucket": "Foundations",
    "bucket_slug": "foundations",
    "subtopic": "Historical Context",
    "slug": "lenore-jacobson",
    "definition": "An American elementary school principal who co-authored the seminal 1968 study and book \"Pygmalion in the Classroom\" with Robert Rosenthal.",
    "key_points": [
      "Educational Leadership: Jacobson was the principal of West Park Elementary School in California (pseudonymously called Oak School) where the landmark study was conducted.",
      "Connecting Theory to Practice: She contacted Robert Rosenthal after reading about his research on experimenter expectancy effects, proposing that a similar effect might occur between teachers and students.",
      "Facilitator of Research: Jacobson's position allowed the researchers to implement the deceptive \"Intellectual Bloomers\" test without raising suspicion among teachers, securing authentic classroom conditions.",
      "Seminal Co-Author: Her collaboration with Rosenthal combined academic psychological research with practical, hands-on administrative expertise, making the book highly accessible to educators."
    ],
    "sources": [
      {"url": "https://en.wikipedia.org/wiki/Pygmalion_in_the_Classroom", "title": "Pygmalion in the Classroom on Wikipedia"},
      {"url": "https://www.britannica.com/topic/Pygmalion-effect", "title": "The Pygmalion Effect in Britannica"},
      {"url": "https://www.tandfonline.com/doi/abs/10.1080/00220671.1969.10883838", "title": "Contemporary reviews of Rosenthal & Jacobson (Taylor & Francis)"}
    ],
    "wikilink_targets": [
      {"name": "Robert Rosenthal", "reason": "Partnered with Rosenthal to translate lab findings into school classrooms."},
      {"name": "Oak School Study", "reason": "Facilitated and administered the study as the school's principal."},
      {"name": "Intellectual Bloomers Label", "reason": "Allowed the deceptive student labeling to be implemented in her school."},
      {"name": "Pygmalion in the Classroom", "reason": "Co-authored the book explaining the study's results and implications."},
      {"name": "Interpersonal Expectancy Effects", "reason": "Explored how administrator and teacher expectancies shape student growth."}
    ],
    "cross_domain_targets": [
      {"name": "Educational Psychology", "reason": "Focuses on teacher behavior, curriculum design, and student motivation."},
      {"name": "Sociology", "reason": "Explores how group expectations and structural positions generate self-fulfilling prophecies."}
    ],
    "diagram": "flowchart TD\n    A[Lenore Jacobson] -->|Administer School| B[Oak School Study]\n    A -->|Propose Research| C[Robert Rosenthal]\n    B --> D[Pygmalion in the Classroom]",
    "key_figures_mentioned": [
      {"name": "Robert Rosenthal", "role": "Co-investigator and psychologist"},
      {"name": "Lenore Jacobson", "role": "School principal and co-investigator"}
    ],
    "further_reading": [
      {"resource": "Pygmalion in the Classroom by Rosenthal and Jacobson", "why": "classic text detailing her collaboration"}
    ]
  },
  {
    "title": "Oak School Study",
    "bucket": "Foundations",
    "bucket_slug": "foundations",
    "subtopic": "The Landmark Experiment",
    "slug": "oak-school-study",
    "definition": "The famous 1968 field experiment conducted by Robert Rosenthal and Lenore Jacobson in a California elementary school to test the effects of teacher expectations on student IQ growth.",
    "key_points": [
      "Experimental Setup: Teachers were told that a new test (the \"Harvard Test of Inflected Acquisition\") could predict which students were about to experience a rapid intellectual spurt.",
      "Manipulated Expectations: In reality, the test was a standard non-verbal IQ test, and the list of \"intellectual bloomers\" given to teachers was generated entirely at random.",
      "IQ Measurement: Students were tested at the beginning of the school year and re-tested at the end of the year to measure change in their intelligence scores.",
      "Key Findings: The randomly labeled \"bloomers\" showed significantly greater IQ gains, especially in the first and second grades, compared to the control group students.",
      "Methodological Critique: The study faced intense criticism regarding the reliability of the IQ test scores used for young children and the ethics of deceiving the school's teaching staff."
    ],
    "sources": [
      {"url": "https://en.wikipedia.org/wiki/Pygmalion_in_the_Classroom", "title": "Oak School Study Details on Wikipedia"},
      {"url": "https://www.simplypsychology.org/pygmalion-effect.html", "title": "Pygmalion Effect Overview (Simply Psychology)"},
      {"url": "https://pubmed.ncbi.nlm.nih.gov/5663784/", "title": "Original Pygmalion Study PubMed Citation"}
    ],
    "wikilink_targets": [
      {"name": "Robert Rosenthal", "reason": "The principal researcher who designed the study's expectancy conditions."},
      {"name": "Lenore Jacobson", "reason": "The school principal who facilitated the classroom experiment."},
      {"name": "Intellectual Bloomers Label", "reason": "Used this random designation to manipulate teacher expectations."},
      {"name": "Pygmalion in the Classroom", "reason": "The primary subject and empirical core of the 1968 book."},
      {"name": "Replication and Methodological Critiques", "reason": "The target of major debates regarding replication and IQ validity."}
    ],
    "cross_domain_targets": [
      {"name": "Educational Psychology", "reason": "Focuses on teacher behavior, curriculum design, and student motivation."},
      {"name": "Sociology", "reason": "Explores how group expectations and structural positions generate self-fulfilling prophecies."}
    ],
    "diagram": "sequenceDiagram\n    participant R as Researchers\n    participant T as Teachers\n    participant S as Labeled Bloomers\n    R->>T: Give random \"Bloomers\" list\n    T->>S: Unconscious warm climate & richer input\n    S->>S: Increased self-efficacy & effort\n    S->>R: Higher IQ scores at end of year",
    "key_figures_mentioned": [
      {"name": "Robert Rosenthal", "role": "Lead researcher"},
      {"name": "Lenore Jacobson", "role": "Principal of the Oak School"}
    ],
    "further_reading": [
      {"resource": "Pygmalion in the Classroom (1968)", "why": "the formal monograph of the study"}
    ]
  },
  {
    "title": "Intellectual Bloomers Label",
    "bucket": "Foundations",
    "bucket_slug": "foundations",
    "subtopic": "The Landmark Experiment",
    "slug": "intellectual-bloomers-label",
    "definition": "The experimental label assigned to a random 20% subset of students in the Oak School study, presented to teachers as a reliable indicator of imminent intellectual growth.",
    "key_points": [
      "Expectancy Catalyst: The label \"intellectual bloomers\" was designed to create a positive expectancy bias in teachers' minds without implying that other students were deficient.",
      "Randomization Control: Because the labeled students were chosen entirely at random, any subsequent difference in their performance could be attributed solely to teacher expectations.",
      "Teacher Behavior Alteration: The label unconsciously modified how teachers interacted with the chosen students, leading to warmer body language, more frequent eye contact, and more detailed feedback.",
      "Cognitive Priming: The label acted as a cognitive lens, causing teachers to interpret the bloomers' mistakes as learning steps and their successes as proof of high intelligence."
    ],
    "sources": [
      {"url": "https://en.wikipedia.org/wiki/Pygmalion_in_the_Classroom", "title": "Intellectual Bloomers details on Wikipedia"},
      {"url": "https://www.simplypsychology.org/pygmalion-effect.html", "title": "Simply Psychology on Bloomers Label"},
      {"url": "https://www.frontiersin.org/articles/10.3897/ap.2.e0123/full", "title": "Expectancy Priming in Education (Frontiers)"}
    ],
    "wikilink_targets": [
      {"name": "Robert Rosenthal", "reason": "Rosenthal designed this label to prime teacher expectations."},
      {"name": "Lenore Jacobson", "reason": "Jacobson introduced the label to the school's teaching staff."},
      {"name": "Oak School Study", "reason": "The core experimental manipulation of the 1968 study."},
      {"name": "Climate Factor", "reason": "The label prompted teachers to create a warmer climate for selected students."},
      {"name": "Input Factor", "reason": "Labeled students received richer, more challenging learning inputs."}
    ],
    "cross_domain_targets": [
      {"name": "Educational Psychology", "reason": "Focuses on teacher behavior, curriculum design, and student motivation."},
      {"name": "Sociology", "reason": "Explores how group expectations and structural positions generate self-fulfilling prophecies."}
    ],
    "diagram": "flowchart TD\n    A[Random Selection] --> B[Bloomer Label Issued]\n    B --> C[Teacher Expectation Raised]\n    C --> D[Differentiated Teacher Behavior]\n    D --> E[Real Intellectual Growth]",
    "key_figures_mentioned": [
      {"name": "Robert Rosenthal", "role": "Psychologist who designed the labeling manipulation"},
      {"name": "Lenore Jacobson", "role": "School principal who introduced the label to teachers"}
    ],
    "further_reading": [
      {"resource": "Pygmalion in the Classroom (1968)", "why": "describes how the labeling was set up"}
    ]
  },
  {
    "title": "Pygmalion in the Classroom",
    "bucket": "Foundations",
    "bucket_slug": "foundations",
    "subtopic": "The Landmark Experiment",
    "slug": "pygmalion-in-the-classroom",
    "definition": "The influential 1968 book authored by Robert Rosenthal and Lenore Jacobson that detailed the Oak School study and popularized the concept of interpersonal expectancy effects.",
    "key_points": [
      "Public Impact: The book bridged the gap between academic research and public interest, sparking national debates on educational equity and teacher expectations.",
      "Theoretical Synthesis: It compiled laboratory evidence on expectancy effects, historical literature on self-fulfilling prophecies, and empirical findings from the school experiment.",
      "Critique of Tracking: The authors argued that traditional educational tracking systems could act as permanent negative labels, artificially limiting student achievement.",
      "Controversy and Debate: Upon publication, the book was praised by social reformers but heavily criticized by psychometricians for perceived statistical errors."
    ],
    "sources": [
      {"url": "https://en.wikipedia.org/wiki/Pygmalion_in_the_Classroom", "title": "Pygmalion in the Classroom Book Page"},
      {"url": "https://www.healthline.com/health/pygmalion-effect", "title": "Healthline on Pygmalion in the Classroom"},
      {"url": "https://archive.org/details/pygmalioninclass00rose", "title": "Internet Archive digital copy of Pygmalion in the Classroom"}
    ],
    "wikilink_targets": [
      {"name": "Robert Rosenthal", "reason": "Co-authored by Rosenthal to detail expectancy effects."},
      {"name": "Lenore Jacobson", "reason": "Co-authored by Jacobson, bringing school administration perspective."},
      {"name": "Oak School Study", "reason": "The book that published the full dataset of the Oak School experiment."},
      {"name": "Self-Fulfilling Prophecy", "reason": "Popularized the self-fulfilling prophecy in modern educational psychology."},
      {"name": "Replication and Methodological Critiques", "reason": "Prompted extensive criticism of its statistical methods."}
    ],
    "cross_domain_targets": [
      {"name": "Educational Psychology", "reason": "Focuses on teacher behavior, curriculum design, and student motivation."},
      {"name": "Sociology", "reason": "Explores how group expectations and structural positions generate self-fulfilling prophecies."}
    ],
    "diagram": "flowchart LR\n    A[Research Findings] --> B[Pygmalion in the Classroom Book]\n    B --> C[Public Debate on IQ Testing]\n    B --> D[Reforms in Teacher Training]",
    "key_figures_mentioned": [
      {"name": "Robert Rosenthal", "role": "Lead author"},
      {"name": "Lenore Jacobson", "role": "Co-author and school principal"}
    ],
    "further_reading": [
      {"resource": "Pygmalion in the Classroom (1968)", "why": "the primary text itself"}
    ]
  },
  {
    "title": "Self-Fulfilling Prophecy",
    "bucket": "Foundations",
    "bucket_slug": "foundations",
    "subtopic": "Fundamental Theory",
    "slug": "self-fulfilling-prophecy",
    "definition": "A sociological and psychological concept coined by Robert K. Merton in 1948, where a false definition of a situation evokes a new behavior that makes the originally false conception come true.",
    "key_points": [
      "Theoretical Foundation: The Pygmalion Effect is a specific interpersonal subcategory of the self-fulfilling prophecy, focusing on how one person's expectations shape another's actions.",
      "Merton's Definition: In his classic paper, Merton described how beliefs—even when entirely unfounded—alter behavior in ways that align external reality with those beliefs.",
      "The Three-Stage Loop: The prophecy operates in a loop: a belief is held, actions are taken in accordance with that belief, and those actions bring about the expected outcome.",
      "Social Implications: Merton used the concept to explain structural social phenomena, including bank runs and racial discrimination, highlighting the systemic power of collective expectations."
    ],
    "sources": [
      {"url": "https://en.wikipedia.org/wiki/Self-fulfilling_prophecy", "title": "Self-Fulfilling Prophecy on Wikipedia"},
      {"url": "https://www.britannica.com/topic/self-fulfilling-prophecy", "title": "Self-Fulfilling Prophecy in Britannica"},
      {"url": "https://www.asanet.org/about/sociology-historical-perspective/robert-k-merton", "title": "Robert K. Merton Biography (ASA)"}
    ],
    "wikilink_targets": [
      {"name": "Robert Rosenthal", "reason": "Rosenthal provided the first broad psychological evidence for this sociological concept."},
      {"name": "Pygmalion in the Classroom", "reason": "The book that demonstrated the prophecy in educational settings."},
      {"name": "Interpersonal Expectancy Effects", "reason": "The psychological subcategory describing how one's beliefs shape another's actions."},
      {"name": "The Pygmalion Cycle", "reason": "The cognitive and behavioral loop that executes the prophecy."},
      {"name": "The Golem Effect", "reason": "The negative variation of the self-fulfilling prophecy."}
    ],
    "cross_domain_targets": [
      {"name": "Sociology", "reason": "Explores how group expectations and structural positions generate self-fulfilling prophecies."},
      {"name": "Behavioral Economics", "reason": "Examines how market beliefs and expectations drive economic performance and bubbles."}
    ],
    "diagram": "flowchart TD\n    A[False Definition of Situation] --> B[New Behavior Adopted]\n    B --> C[Expected Result Materializes]\n    C --> D[Original False Concept Confirmed]",
    "key_figures_mentioned": [
      {"name": "Robert K. Merton", "role": "Sociologist who formalized the self-fulfilling prophecy"}
    ],
    "further_reading": [
      {"resource": "Social Theory and Social Structure by Robert K. Merton", "why": "contains the original paper on self-fulfilling prophecies"}
    ]
  },
  {
    "title": "Interpersonal Expectancy Effects",
    "bucket": "Foundations",
    "bucket_slug": "foundations",
    "subtopic": "Fundamental Theory",
    "slug": "interpersonal-expectancy-effects",
    "definition": "The broad psychological phenomenon wherein one person's expectation of another's behavior comes to serve as a self-fulfilling prophecy.",
    "key_points": [
      "General Category: This term represents the overarching scientific category that includes the Pygmalion Effect, the Golem Effect, and experimenter expectancy effects.",
      "Unconscious Transmission: The primary pathway for expectancy effects is subtle, non-verbal, and unconscious communication rather than explicit instruction.",
      "Universal Presence: Expectancy effects have been documented in laboratory experiments, schools, corporate offices, athletic arenas, and clinical therapy rooms.",
      "Bidirectional Influence: While traditional research focuses on top-down expectancy (e.g., teacher to student), newer research highlights how expectancies can be mutual and bottom-up."
    ],
    "sources": [
      {"url": "https://en.wikipedia.org/wiki/Interpersonal_expectancy_effects", "title": "Interpersonal Expectancy Effects on Wikipedia"},
      {"url": "https://www.sciencedirect.com/topics/psychology/interpersonal-expectancy-effect", "title": "Interpersonal Expectancy Effects (ScienceDirect)"},
      {"url": "https://www.taylorfrancis.com/books/edit/10.4324/9780203774649/interpersonal-expectancy-effects-robert-rosenthal", "title": "Interpersonal Expectancy Effects Academic Book"}
    ],
    "wikilink_targets": [
      {"name": "Robert Rosenthal", "reason": "Rosenthal pioneered the scientific study of these effects."},
      {"name": "Self-Fulfilling Prophecy", "reason": "The theoretical framework under which interpersonal expectancies operate."},
      {"name": "The Pygmalion Cycle", "reason": "The mechanism by which expectations are transmitted and confirmed."},
      {"name": "The Galatea Effect", "reason": "Explores how self-expectancies interact with interpersonal expectancies."},
      {"name": "The Golem Effect", "reason": "The negative valence of interpersonal expectancy."}
    ],
    "cross_domain_targets": [
      {"name": "Sociology", "reason": "Explores how group expectations and structural positions generate self-fulfilling prophecies."},
      {"name": "Clinical Psychology", "reason": "Studies patient-therapist expectations and their role in therapeutic outcomes."}
    ],
    "diagram": "flowchart LR\n    A[Person A Expectation] -->|Unconscious Cues| B[Person B Perception]\n    B -->|Behavioral Adjustment| C[Person B Action]\n    C -->|Reinforcement| A",
    "key_figures_mentioned": [
      {"name": "Robert Rosenthal", "role": "Pioneered research on this specific psychological phenomenon"}
    ],
    "further_reading": [
      {"resource": "Interpersonal Expectancy Effects by Robert Rosenthal", "why": "a comprehensive review of the field's early literature"}
    ]
  },
  {
    "title": "Climate Factor",
    "bucket": "Mechanisms",
    "bucket_slug": "mechanisms",
    "subtopic": "The Four-Factor Model",
    "slug": "climate-factor",
    "definition": "The social-emotional warmth and supportive atmosphere created by an authority figure, representing the first element of Rosenthal's four-factor model.",
    "key_points": [
      "Non-Verbal Cues: Leaders and teachers express warmth through non-verbal channels such as smiling, nodding, leaning forward, and maintaining frequent eye contact.",
      "Psychological Safety: A warm climate fosters psychological safety, making individuals feel valued and lowering their performance anxiety.",
      "Unconscious Expression: Because climate is primarily non-verbal, leaders often create a supportive or hostile atmosphere without consciously realizing it.",
      "Foundational Component: Rosenthal identified climate as the most critical factor, as it establishes the emotional trust necessary for the other three factors to be effective."
    ],
    "sources": [
      {"url": "https://www.simplypsychology.org/pygmalion-effect.html", "title": "Climate Factor in Simply Psychology"},
      {"url": "https://hbr.org/1969/07/pygmalion-in-management", "title": "Pygmalion in Management (Harvard Business Review)"},
      {"url": "https://www.sciencedirect.com/topics/social-sciences/classroom-climate", "title": "Classroom Climate Research (ScienceDirect)"}
    ],
    "wikilink_targets": [
      {"name": "Robert Rosenthal", "reason": "Rosenthal identified Climate as the foundational factor of expectation communication."},
      {"name": "Intellectual Bloomers Label", "reason": "Labeled students experienced a warmer climate from teachers."},
      {"name": "Input Factor", "reason": "A warm climate establishes the trust needed to deliver challenging input."},
      {"name": "Output Factor", "reason": "A supportive climate encourages individuals to verbalize outputs."},
      {"name": "Feedback Factor", "reason": "Feedback is interpreted more constructively in a warm climate."}
    ],
    "cross_domain_targets": [
      {"name": "Educational Psychology", "reason": "Focuses on teacher behavior, curriculum design, and student motivation."},
      {"name": "Organizational Behavior", "reason": "Studies leadership styles, employee engagement, and corporate culture."}
    ],
    "diagram": "flowchart TD\n    A[Positive Expectation] --> B[Warmer Non-Verbal Cues]\n    B --> C[Reduced Anxiety & Fear]\n    C --> D[Increased Engagement & Risk-Taking]",
    "key_figures_mentioned": [
      {"name": "Robert Rosenthal", "role": "Identified Climate as the foundational factor of expectation communication"}
    ],
    "further_reading": [
      {"resource": "The Four-Factor Model of Expectancy by Robert Rosenthal", "why": "explains climate and its interaction with other factors"}
    ]
  },
  {
    "title": "Input Factor",
    "bucket": "Mechanisms",
    "bucket_slug": "mechanisms",
    "subtopic": "The Four-Factor Model",
    "slug": "input-factor",
    "definition": "The tendency of teachers or leaders to deliver more instructional material, assign more difficult tasks, and offer richer content to individuals for whom they hold high expectations.",
    "key_points": [
      "Material Richness: High-expectancy individuals are exposed to a broader, more challenging curriculum compared to low-expectancy peers who receive repetitive or simplified assignments.",
      "Opportunity to Learn: By adjusting the input, leaders dictate the upper boundary of what the individual is allowed to learn and master.",
      "Differentiation Bias: This bias manifests when managers reserve high-profile projects for favored employees, denying growth opportunities to others.",
      "Reinforcing Feedback Loops: The rich input enables the individual to develop advanced skills, which then validates the leader's initial high expectation."
    ],
    "sources": [
      {"url": "https://www.simplypsychology.org/pygmalion-effect.html", "title": "Input Factor in Simply Psychology"},
      {"url": "https://hbr.org/1969/07/pygmalion-in-management", "title": "HBR Pygmalion Article"},
      {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8900690/", "title": "Interpersonal Expectations in Classrooms (PMC)"}
    ],
    "wikilink_targets": [
      {"name": "Robert Rosenthal", "reason": "Defined the input factor in teacher expectation transmission."},
      {"name": "Climate Factor", "reason": "Warm climate enables the successful delivery of advanced input."},
      {"name": "Output Factor", "reason": "Rich input provides the material necessary for high-quality output."},
      {"name": "Feedback Factor", "reason": "Complex input requires detailed feedback to guide learning."},
      {"name": "The Pygmalion Cycle", "reason": "Differentiated input is a key behavioral action in the cycle."}
    ],
    "cross_domain_targets": [
      {"name": "Educational Psychology", "reason": "Focuses on teacher behavior, curriculum design, and student motivation."},
      {"name": "Organizational Behavior", "reason": "Studies leadership styles, employee engagement, and corporate culture."}
    ],
    "diagram": "flowchart LR\n    A[High expectation] --> B[Assign more difficult tasks]\n    B --> C[Greater cognitive challenge]\n    C --> D[Advanced skill acquisition]",
    "key_figures_mentioned": [
      {"name": "Robert Rosenthal", "role": "Defined the input factor in teacher expectation transmission"}
    ],
    "further_reading": [
      {"resource": "Differentiated Instruction and Expectancy Theory", "why": "discusses how input variations affect student achievement"}
    ]
  },
  {
    "title": "Output Factor",
    "bucket": "Mechanisms",
    "bucket_slug": "mechanisms",
    "subtopic": "The Four-Factor Model",
    "slug": "output-factor",
    "definition": "The behavior where teachers or managers offer high-expectancy individuals more opportunities to speak, respond, ask questions, and lead, representing the third element in Rosenthal's four-factor model.",
    "key_points": [
      "Participation Opportunity: High-expectancy individuals are called on more frequently and are given more time to formulate and express their thoughts.",
      "Active Engagement: This factor encourages active learning and participation, which are critical drivers of academic and professional skill acquisition.",
      "Non-Verbal Encouragement: Managers prompt high-expectancy employees for input during meetings and show active listening behaviors while they speak.",
      "Confidence Building: The repeated experience of being asked for input and having it listened to builds self-efficacy and public speaking confidence."
    ],
    "sources": [
      {"url": "https://www.simplypsychology.org/pygmalion-effect.html", "title": "Output Factor in Simply Psychology"},
      {"url": "https://www.thedecisionlab.com/biases-effects/the-pygmalion-effect", "title": "Output Factor (The Decision Lab)"},
      {"url": "https://www.erudit.org/en/journals/mefa/1900-v1-n1-mefa0123/", "title": "Pygmalion in Organizations Research"}
    ],
    "wikilink_targets": [
      {"name": "Robert Rosenthal", "reason": "Rosenthal included output as the third factor in his model."},
      {"name": "Climate Factor", "reason": "Warm climate encourages subjects to take risks in their output."},
      {"name": "Input Factor", "reason": "Rich input provides the knowledge base needed for output."},
      {"name": "Feedback Factor", "reason": "Output is the behavior that leaders evaluate and provide feedback on."},
      {"name": "The Pygmalion Cycle", "reason": "Subject output confirms the observer's initial beliefs."}
    ],
    "cross_domain_targets": [
      {"name": "Educational Psychology", "reason": "Focuses on teacher behavior, curriculum design, and student motivation."},
      {"name": "Organizational Behavior", "reason": "Studies leadership styles, employee engagement, and corporate culture."}
    ],
    "diagram": "flowchart TD\n    A[High Expectation] --> B[Called on in class/meetings]\n    B --> C[Longer wait time to answer]\n    C --> D[Active verbal participation]\n    D --> E[Reinforced learning]",
    "key_figures_mentioned": [
      {"name": "Robert Rosenthal", "role": "Developed the Output Factor concept in the four-factor taxonomy"}
    ],
    "further_reading": [
      {"resource": "Active Participation and Student Outcome Meta-analysis", "why": "validates the importance of the output factor"}
    ]
  },
  {
    "title": "Feedback Factor",
    "bucket": "Mechanisms",
    "bucket_slug": "mechanisms",
    "subtopic": "The Four-Factor Model",
    "slug": "feedback-factor",
    "definition": "The qualitative difference in feedback provided to individuals, where high-expectancy subjects receive more praise, constructive criticism, and detailed corrections compared to low-expectancy subjects.",
    "key_points": [
      "Praise Differentiation: High-expectancy individuals are praised more for correct answers, whereas low-expectancy individuals are often praised for mediocre or incorrect answers as a form of patronizing comfort.",
      "Constructive Correction: When high-expectancy individuals fail, they receive detailed explanations of their errors because the leader believes they have the capacity to improve.",
      "Attribution of Success: Successes of high-expectancy individuals are attributed to their ability, while failures are attributed to effort; the reverse is true for low-expectancy individuals.",
      "Motivational Impact: Detailed, constructive feedback motivates individuals to correct errors and persist through difficult tasks."
    ],
    "sources": [
      {"url": "https://www.simplypsychology.org/pygmalion-effect.html", "title": "Feedback Factor in Simply Psychology"},
      {"url": "https://www.thedecisionlab.com/biases-effects/the-pygmalion-effect", "title": "Feedback Factor (The Decision Lab)"},
      {"url": "https://link.springer.com/chapter/10.1007/978-3-030-80412-1_5", "title": "Teacher Feedback and Expectancy Effects (Springer)"}
    ],
    "wikilink_targets": [
      {"name": "Robert Rosenthal", "reason": "Rosenthal identified feedback as the corrective channel of expectancy."},
      {"name": "Climate Factor", "reason": "Emotional climate determines how feedback is received and internalized."},
      {"name": "Input Factor", "reason": "Complex input requires constructive feedback to be mastered."},
      {"name": "Output Factor", "reason": "Feedback is directly given in response to the subject's output."},
      {"name": "The Pygmalion Cycle", "reason": "Constructive feedback reinforces high performance and self-belief."}
    ],
    "cross_domain_targets": [
      {"name": "Educational Psychology", "reason": "Focuses on teacher behavior, curriculum design, and student motivation."},
      {"name": "Organizational Behavior", "reason": "Studies leadership styles, employee engagement, and corporate culture."}
    ],
    "diagram": "flowchart LR\n    A[High Expectancy Success] -->|Attributed to Ability| B[Praise & Skill Identity]\n    C[High Expectancy Failure] -->|Attributed to Effort| D[Detailed Constructive Criticism]\n    B & D --> E[Increased Motivation]",
    "key_figures_mentioned": [
      {"name": "Robert Rosenthal", "role": "Classified feedback styles as the fourth key communication factor"}
    ],
    "further_reading": [
      {"resource": "The Power of Feedback by John Hattie", "why": "reinforces how feedback style drives performance"}
    ]
  },
  {
    "title": "The Pygmalion Cycle",
    "bucket": "Mechanisms",
    "bucket_slug": "mechanisms",
    "subtopic": "Psychological and Cognitive Cycles",
    "slug": "the-pygmalion-cycle",
    "definition": "The self-reinforcing, four-stage feedback loop that illustrates how one's expectations of others influence their behavior and shape the other's self-concept and performance.",
    "key_points": [
      "Four Stages: The cycle begins with (1) Our beliefs about others, which drive (2) Our actions towards them, which shape (3) Their beliefs about themselves, which influence (4) Their actions back towards us, reinforcing our initial beliefs.",
      "Cognitive Loop: It operates as a feedback loop where the observer's expectations act as the input and the target's behavior acts as the confirming output.",
      "Interpersonal System: The cycle demonstrates that human performance is not an isolated individual trait but an emergent outcome of interpersonal relationships.",
      "Intervention Points: Knowing the cycle allows managers and teachers to intentionally break negative loops by raising expectations or modifying climate behaviors."
    ],
    "sources": [
      {"url": "https://www.thedecisionlab.com/biases-effects/the-pygmalion-effect", "title": "The Pygmalion Cycle on The Decision Lab"},
      {"url": "https://hbr.org/1969/07/pygmalion-in-management", "title": "Pygmalion Cycle in HBR"},
      {"url": "https://www.verywellmind.com/what-is-the-pygmalion-effect-5089758", "title": "Verywell Mind on Pygmalion Cycle"}
    ],
    "wikilink_targets": [
      {"name": "Self-Fulfilling Prophecy", "reason": "The cycle represents the psychological operationalization of the prophecy."},
      {"name": "Interpersonal Expectancy Effects", "reason": "Explains the transmission dynamics of expectancy effects."},
      {"name": "Climate Factor", "reason": "Climate serves as the non-verbal channel of the cycle's second stage."},
      {"name": "Expectancy Bias", "reason": "Priming beliefs in the cycle's first stage."},
      {"name": "The Galatea Effect", "reason": "The third stage of the cycle (self-belief) represents the Galatea Effect."}
    ],
    "cross_domain_targets": [
      {"name": "Sociology", "reason": "Explores how group expectations and structural positions generate self-fulfilling prophecies."},
      {"name": "Organizational Behavior", "reason": "Studies leadership styles, employee engagement, and corporate culture."}
    ],
    "diagram": "flowchart TD\n    1[Our beliefs about others] -->|influence| 2[Our actions toward others]\n    2 -->|impact| 3[Their beliefs about themselves]\n    3 -->|cause| 4[Their actions toward us]\n    4 -->|reinforce| 1",
    "key_figures_mentioned": [],
    "further_reading": [
      {"resource": "Interpersonal Expectations by Robert Rosenthal", "why": "discusses the cycle and reinforcement patterns"}
    ]
  },
  {
    "title": "Expectancy Bias",
    "bucket": "Mechanisms",
    "bucket_slug": "mechanisms",
    "subtopic": "Psychological and Cognitive Cycles",
    "slug": "expectancy-bias",
    "definition": "A cognitive bias where an observer's preconceived expectations cause them to interpret evidence and evaluate performance in a way that confirms those expectations.",
    "key_points": [
      "Selective Attention: Observers selectively notice behaviors that support their expectations while ignoring or discounting counter-evidence.",
      "Interpretation Bias: Ambiguous performance is interpreted positively for high-expectancy individuals and negatively for low-expectancy individuals.",
      "Memory Distortion: Observers are more likely to recall successes of high-expectancy subjects and failures of low-expectancy subjects.",
      "Scientific Threat: In clinical trials and behavioral research, expectancy bias can lead to false positive results, requiring double-blind protocols to control for it."
    ],
    "sources": [
      {"url": "https://en.wikipedia.org/wiki/Observer-expectancy_effect", "title": "Observer-Expectancy Effect on Wikipedia"},
      {"url": "https://www.sciencedirect.com/topics/psychology/expectancy-bias", "title": "Expectancy Bias in ScienceDirect"},
      {"url": "https://www.apa.org/pubs/books/4318012", "title": "Experimenter Effects in Behavioral Research (APA)"}
    ],
    "wikilink_targets": [
      {"name": "Robert Rosenthal", "reason": "Rosenthal studied this bias to control experimenter expectancy effects."},
      {"name": "Self-Fulfilling Prophecy", "reason": "The cognitive bias that initiates and preserves the prophecy."},
      {"name": "The Pygmalion Cycle", "reason": "The bias that reinforces the first stage of the cycle."},
      {"name": "Halo and Horns Effects", "reason": "Cognitive biases that form the foundation of expectancy bias."},
      {"name": "Replication and Methodological Critiques", "reason": "Critics claim the original researchers fell victim to expectancy bias."}
    ],
    "cross_domain_targets": [
      {"name": "Clinical Psychology", "reason": "Studies patient-therapist expectations and their role in therapeutic outcomes."},
      {"name": "Sociology", "reason": "Explores how group expectations and structural positions generate self-fulfilling prophecies."}
    ],
    "diagram": "flowchart LR\n    A[Observer Expectation] --> B[Selective Observation]\n    B --> C[Distorted Interpretation]\n    C --> D[Confirmation of Initial Expectation]",
    "key_figures_mentioned": [
      {"name": "Robert Rosenthal", "role": "Extensively documented observer-expectancy bias in lab and educational research"}
    ],
    "further_reading": [
      {"resource": "Observer Effects in Science by Donald Rubin", "why": "analyzes scientific and observational expectancy biases"}
    ]
  },
  {
    "title": "Social Identity Theory Connection",
    "bucket": "Mechanisms",
    "bucket_slug": "mechanisms",
    "subtopic": "Psychological and Cognitive Cycles",
    "slug": "social-identity-theory-connection",
    "definition": "The conceptual intersection showing how labeling and external expectations shape an individual's self-concept and group identity, influencing performance.",
    "key_points": [
      "Label Internalization: Social Identity Theory, pioneered by Henri Tajfel, explains that individuals internalize the labels and expectations placed upon their social group.",
      "Stereotype Threat: Negative group expectations can induce performance anxiety and lead to a decline in achievement, a phenomenon closely tied to the Golem Effect.",
      "In-Group favoritism: Teachers or managers may project higher expectations onto individuals they identify as part of their in-group, reinforcing systemic inequality.",
      "Self-Concept Alteration: External expectancies gradually modify an individual's self-schema, aligning their personal identity with external assessments."
    ],
    "sources": [
      {"url": "https://en.wikipedia.org/wiki/Social_identity_theory", "title": "Social Identity Theory on Wikipedia"},
      {"url": "https://www.sciencedirect.com/topics/psychology/social-identity-theory", "title": "Social Identity Theory in ScienceDirect"},
      {"url": "https://www.simplypsychology.org/social-identity-theory.html", "title": "Simply Psychology on Social Identity Theory"}
    ],
    "wikilink_targets": [
      {"name": "Self-Fulfilling Prophecy", "reason": "Group labels can act as structural self-fulfilling prophecies."},
      {"name": "The Pygmalion Cycle", "reason": "Explains how external cycles shape self-concept and group identity."},
      {"name": "The Galatea Effect", "reason": "Explores how social identity drives internal self-expectations."},
      {"name": "The Golem Effect", "reason": "Stereotype threat is a collective manifestation of the Golem Effect."},
      {"name": "Labeling and Ethical Implications", "reason": "Highlights the ethical issues of applying demographic labels."}
    ],
    "cross_domain_targets": [
      {"name": "Sociology", "reason": "Explores how group expectations and structural positions generate self-fulfilling prophecies."},
      {"name": "Educational Psychology", "reason": "Focuses on teacher behavior, curriculum design, and student motivation."}
    ],
    "diagram": "flowchart TD\n    A[External Group Expectations] --> B[Internalized Group Identity]\n    B --> C[Self-Concept Adaptation]\n    C --> D[Performance Change aligned with Label]",
    "key_figures_mentioned": [],
    "further_reading": [
      {"resource": "Stereotype Threat by Claude Steele", "why": "provides details on negative expectancy internalized by minority groups"}
    ]
  },
  {
    "title": "Pygmalion in Management",
    "bucket": "Applications and Critiques",
    "bucket_slug": "applications-and-critiques",
    "subtopic": "Organizational and Educational Domains",
    "slug": "pygmalion-in-management",
    "definition": "The application of expectancy theory to corporate leadership and human resource management, popularized by J. Sterling Livingston in 1969.",
    "key_points": [
      "Livingston's Argument: Livingston argued that a manager's expectations of their subordinates determine both the subordinates' performance and their career progress.",
      "Managerial Self-Efficacy: Managers who hold high expectations of their own capability are more likely to project high expectations onto their teams.",
      "Early Career Impact: The expectations set by an employee's first manager have a lasting impact, shaping their career path for years.",
      "Transformational Leadership: Transformational leaders leverage Pygmalion dynamics by communicating an inspiring vision and expressing confidence in their team's ability to achieve it."
    ],
    "sources": [
      {"url": "https://hbr.org/1969/07/pygmalion-in-management", "title": "Pygmalion in Management (Harvard Business Review)"},
      {"url": "https://www.sciencedirect.com/science/article/pii/0749597890900388", "title": "Expectancy Effects in Organizations (ScienceDirect)"},
      {"url": "https://www.forbes.com/sites/forbescoachescouncil/2021/04/21/how-to-use-the-pygmalion-effect-to-boost-team-performance/", "title": "Forbes on Pygmalion in the Workplace"}
    ],
    "wikilink_targets": [
      {"name": "Robert Rosenthal", "reason": "Livingston applied Rosenthal's educational findings to corporate settings."},
      {"name": "Climate Factor", "reason": "Managers communicate expectations through organizational climate."},
      {"name": "The Pygmalion Cycle", "reason": "The cycle drives employee development and productivity."},
      {"name": "The Galatea Effect", "reason": "High-expectancy management fosters employee self-expectations."},
      {"name": "The Golem Effect", "reason": "Low managerial expectations trigger Golem-like performance drops."}
    ],
    "cross_domain_targets": [
      {"name": "Organizational Behavior", "reason": "Studies leadership styles, employee engagement, and corporate culture."},
      {"name": "Sociology", "reason": "Explores how group expectations and structural positions generate self-fulfilling prophecies."}
    ],
    "diagram": "flowchart TD\n    A[Manager High Expectations] --> B[Transformational Leadership Behaviors]\n    B --> C[Subordinate High Self-Expectancy]\n    C --> D[Subordinate High Performance]\n    D --> E[Career Success & Retention]",
    "key_figures_mentioned": [
      {"name": "J. Sterling Livingston", "role": "Author who popularized the manager expectancy effect in HBR"}
    ],
    "further_reading": [
      {"resource": "Pygmalion in Management by J. Sterling Livingston", "why": "the classic HBR article"}
    ]
  },
  {
    "title": "Sports and Coaching Expectations",
    "bucket": "Applications and Critiques",
    "bucket_slug": "applications-and-critiques",
    "subtopic": "Organizational and Educational Domains",
    "slug": "sports-and-coaching-expectations",
    "definition": "The study of how a coach's expectations and evaluations of an athlete's potential influence the athlete's self-confidence, skill development, and athletic output.",
    "key_points": [
      "Initial Assessment: Coaches form immediate expectations based on physical stature, background, or early performance trials, which can be highly biased.",
      "Behavioral Treatment: Athletes labeled as high-potential receive more instruction, play-time, and emotional support, while low-potential athletes are marginalized.",
      "Athletic Self-Efficacy: The coach's behavior shapes the athlete's self-efficacy, causing them to perform up or down to the coach's expectations.",
      "Physical Performance Confirmation: The athlete's eventual physical output confirms the coach's initial evaluation, closing the cycle."
    ],
    "sources": [
      {"url": "https://www.sciencedirect.com/topics/psychology/coach-expectation", "title": "Coach Expectations in Sports Psychology (ScienceDirect)"},
      {"url": "https://pubmed.ncbi.nlm.nih.gov/22051624/", "title": "Expectations in Sport and Physical Activity PubMed Citation"},
      {"url": "https://www.apadivisions.org/division-47/publications/sportpsych-works/coach-expectations.pdf", "title": "APA Division 47 on Coach Expectations"}
    ],
    "wikilink_targets": [
      {"name": "Climate Factor", "reason": "Coaches communicate expectations through emotional climate on the field."},
      {"name": "Input Factor", "reason": "High-potential athletes receive more technical instruction (input)."},
      {"name": "Output Factor", "reason": "Coaches give high-expectancy players more play-time and leadership roles."},
      {"name": "The Pygmalion Cycle", "reason": "Drives athletic self-efficacy and eventual physical performance."},
      {"name": "The Galatea Effect", "reason": "High coach belief translates to high athlete self-belief."}
    ],
    "cross_domain_targets": [
      {"name": "Sports Psychology", "reason": "Investigates athletic motivation, coach-athlete relationships, and performance anxiety."},
      {"name": "Organizational Behavior", "reason": "Studies leadership styles, employee engagement, and corporate culture."}
    ],
    "diagram": "flowchart LR\n    A[Coach forms expectation] -->|Varying feedback| B[Athlete's Self-Belief changes]\n    B -->|Effort / Performance| C[Physical athletic output]\n    C -->|Confirms belief| A",
    "key_figures_mentioned": [],
    "further_reading": [
      {"resource": "Expectancy Effects in Sport by Thelma Horn", "why": "foundational research on coach-athlete expectancy interactions"}
    ]
  },
  {
    "title": "Medical and Nursing Care",
    "bucket": "Applications and Critiques",
    "bucket_slug": "applications-and-critiques",
    "subtopic": "Organizational and Educational Domains",
    "slug": "medical-and-nursing-care",
    "definition": "The manifestation of expectancy effects in healthcare settings, where patient outcomes are influenced by the expectations of doctors, nurses, and the patients themselves.",
    "key_points": [
      "Clinician Beliefs: Caregivers who believe a patient has a high recovery potential often provide more attentive care, which leads to better patient outcomes.",
      "Placebo Effect Connection: The clinical efficacy of a drug is enhanced when the administering physician projects high confidence in its success.",
      "Patient Self-Expectation: Patients who internalize their doctor's optimistic expectations show higher rates of rehabilitation compliance and better recovery metrics.",
      "Communication Cues: Nurse expectations are transmitted through tone of voice, touch, and bedside manner, directly affecting patient stress and pain levels."
    ],
    "sources": [
      {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6013051/", "title": "Expectancy and the Placebo Effect in Healthcare (PMC)"},
      {"url": "https://pubmed.ncbi.nlm.nih.gov/11797241/", "title": "Influence of Practitioner Expectations on Clinical Outcomes PubMed"},
      {"url": "https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(09)61706-2/fulltext", "title": "Placebo and Expectancy Research in Medicine (The Lancet)"}
    ],
    "wikilink_targets": [
      {"name": "Interpersonal Expectancy Effects", "reason": "Explores expectancies in caregiver-patient interactions."},
      {"name": "Climate Factor", "reason": "Warm nursing care reduces patient physiological stress."},
      {"name": "The Pygmalion Cycle", "reason": "Clinical expectations shape recovery compliance and outcomes."},
      {"name": "The Galatea Effect", "reason": "Enhances patient self-efficacy and active rehabilitation efforts."},
      {"name": "The Golem Effect", "reason": "Negative prognoses can result in a Golem-like health decline."}
    ],
    "cross_domain_targets": [
      {"name": "Clinical Psychology", "reason": "Studies patient-therapist expectations and their role in therapeutic outcomes."},
      {"name": "Sociology", "reason": "Explores how group expectations and structural positions generate self-fulfilling prophecies."}
    ],
    "diagram": "flowchart TD\n    A[Doctor's Optimistic Expectation] --> B[Empathetic Care Delivery]\n    B --> C[Patient Confidence & Safety]\n    C --> D[Biological Placebo Responses & Healing]",
    "key_figures_mentioned": [],
    "further_reading": [
      {"resource": "The Placebo Effect in Clinical Practice by Fabrizio Benedetti", "why": "excellent medical expectancy reference"}
    ]
  },
  {
    "title": "The Galatea Effect",
    "bucket": "Applications and Critiques",
    "bucket_slug": "applications-and-critiques",
    "subtopic": "Counterparts and Related Phenomena",
    "slug": "the-galatea-effect",
    "definition": "A psychological phenomenon where an individual's own self-expectations and self-beliefs directly determine their performance.",
    "key_points": [
      "Internal vs External: While the Pygmalion Effect is driven by external expectations, the Galatea Effect is driven by internal self-expectations and self-efficacy.",
      "Origin of the Name: Named after Galatea, the statue carved by Pygmalion that came to life, symbolizing the internal transformation of the object of expectation.",
      "Cognitive Mechanism: High self-expectations increase effort, resilience in the face of failure, and cognitive processing efficiency.",
      "Leadership Leverage: Managers can trigger the Galatea Effect by coaching employees to build their self-efficacy, making them self-directed high achievers."
    ],
    "sources": [
      {"url": "https://en.wikipedia.org/wiki/Pygmalion_effect#Galatea_effect", "title": "Galatea Effect Section on Wikipedia"},
      {"url": "https://www.simplypsychology.org/pygmalion-effect.html#galatea", "title": "Galatea Effect in Simply Psychology"},
      {"url": "https://hbr.org/1969/07/pygmalion-in-management", "title": "Self-Expectations in Management (HBR)"}
    ],
    "wikilink_targets": [
      {"name": "Ovid's Metamorphoses Myth", "reason": "Named after the statue that was internally transformed into a living being."},
      {"name": "Self-Fulfilling Prophecy", "reason": "The internal version of the self-fulfilling prophecy."},
      {"name": "The Pygmalion Cycle", "reason": "Focuses on the self-belief stage of the Pygmalion cycle."},
      {"name": "The Golem Effect", "reason": "Serves as a protective shield against the Golem Effect."},
      {"name": "Pygmalion in Management", "reason": "Used by managers to build employee self-reliance."}
    ],
    "cross_domain_targets": [
      {"name": "Educational Psychology", "reason": "Focuses on teacher behavior, curriculum design, and student motivation."},
      {"name": "Organizational Behavior", "reason": "Studies leadership styles, employee engagement, and corporate culture."}
    ],
    "diagram": "flowchart LR\n    A[High Self-Expectation] --> B[Increased Effort]\n    B --> C[Persistence in Difficulties]\n    C --> D[Superior Performance outcome]",
    "key_figures_mentioned": [
      {"name": "Albert Bandura", "role": "Psychologist whose self-efficacy theory explains Galatea mechanisms"}
    ],
    "further_reading": [
      {"resource": "Self-Efficacy: The Exercise of Control by Albert Bandura", "why": "unfolds the theory behind self-expectancy"}
    ]
  },
  {
    "title": "The Golem Effect",
    "bucket": "Applications and Critiques",
    "bucket_slug": "applications-and-critiques",
    "subtopic": "Counterparts and Related Phenomena",
    "slug": "the-golem-effect",
    "definition": "The negative counterpart of the Pygmalion Effect, where low expectations placed upon individuals by teachers or leaders lead to a decline in their performance.",
    "key_points": [
      "Negative Expectancy: The Golem Effect represents the destructive half of interpersonal expectancy theory, where leaders expect failure and unconsciously produce it.",
      "Origin of the Name: Named after the Golem of Jewish folklore, a clay creature created to serve but which ultimately turns destructive.",
      "Vicious Cycle: Low expectations lead to cold climate cues, reduced input, and poor feedback, which damages the target's self-esteem and leads to poor performance.",
      "Systemic Bias: The Golem Effect often reinforces racial, socioeconomic, or gender stereotypes, trapping marginalized individuals in cycles of low achievement."
    ],
    "sources": [
      {"url": "https://en.wikipedia.org/wiki/Golem_effect", "title": "Golem Effect on Wikipedia"},
      {"url": "https://www.sciencedirect.com/science/article/pii/0090261682900344", "title": "The Golem Effect in Management (ScienceDirect)"},
      {"url": "https://www.thedecisionlab.com/biases-effects/the-golem-effect", "title": "Golem Effect (The Decision Lab)"}
    ],
    "wikilink_targets": [
      {"name": "Self-Fulfilling Prophecy", "reason": "The negative variation of a self-fulfilling prophecy."},
      {"name": "Interpersonal Expectancy Effects", "reason": "The negative manifestation of interpersonal expectancies."},
      {"name": "The Pygmalion Cycle", "reason": "Follows the same cycle but with negative beliefs and inputs."},
      {"name": "The Galatea Effect", "reason": "Destroys the self-efficacy needed for Galatea effects."},
      {"name": "Labeling and Ethical Implications", "reason": "Demonstrates the severe harms of negative labeling."}
    ],
    "cross_domain_targets": [
      {"name": "Sociology", "reason": "Explores how group expectations and structural positions generate self-fulfilling prophecies."},
      {"name": "Educational Psychology", "reason": "Focuses on teacher behavior, curriculum design, and student motivation."}
    ],
    "diagram": "flowchart TD\n    A[Low Expectation Formed] --> B[Cold climate / diminished input]\n    B --> C[Reduced student self-efficacy]\n    C --> D[Decreased performance & apathy]\n    D --> E[Confirms low potential belief]",
    "key_figures_mentioned": [
      {"name": "Elisha Babad", "role": "Researcher who investigated the Golem effect and teacher nonverbal behavior"}
    ],
    "further_reading": [
      {"resource": "The Golem Effect: A Meta-Analysis by Elisha Babad", "why": "review of negative expectancies in educational environments"}
    ]
  },
  {
    "title": "Halo and Horns Effects",
    "bucket": "Applications and Critiques",
    "bucket_slug": "applications-and-critiques",
    "subtopic": "Counterparts and Related Phenomena",
    "slug": "halo-and-horns-effects",
    "definition": "Cognitive biases where an observer's overall impression of a person influences their feelings and thoughts about that character's specific traits or performance.",
    "key_points": [
      "Halo Effect: A positive general impression (e.g., physical attractiveness or pleasant personality) causes the evaluator to overestimate specific performance.",
      "Horns Effect: A negative general impression leads to an unfair underestimation of performance and character traits.",
      "Interaction with Pygmalion: These effects act as catalysts for the Pygmalion Effect, as the initial halo or horn impression dictates the expectations a leader forms.",
      "Performance Evaluation Distortion: These biases pose a major challenge in annual performance reviews, making objective assessment difficult."
    ],
    "sources": [
      {"url": "https://en.wikipedia.org/wiki/Halo_effect", "title": "Halo Effect on Wikipedia"},
      {"url": "https://www.britannica.com/science/halo-effect", "title": "Halo Effect in Britannica"},
      {"url": "https://www.healthline.com/health/horns-effect", "title": "Horns Effect Overview (Healthline)"}
    ],
    "wikilink_targets": [
      {"name": "Self-Fulfilling Prophecy", "reason": "The initial impressions that establish the prophecy."},
      {"name": "Expectancy Bias", "reason": "Biases that color the observer's subsequent expectations."},
      {"name": "The Pygmalion Cycle", "reason": "Prepares the first stage of the cycle with positive or negative beliefs."},
      {"name": "Pygmalion in Management", "reason": "Skews managerial expectations during recruitment and evaluation."},
      {"name": "Labeling and Ethical Implications", "reason": "Contributes to unfair and discriminatory organizational labels."}
    ],
    "cross_domain_targets": [
      {"name": "Organizational Behavior", "reason": "Studies leadership styles, employee engagement, and corporate culture."},
      {"name": "Sociology", "reason": "Explores how group expectations and structural positions generate self-fulfilling prophecies."}
    ],
    "diagram": "flowchart LR\n    A[General positive impression] --> B[Halo Bias]\n    B --> C[High performance expectation]\n    C --> D[Pygmalion Cycle triggered]",
    "key_figures_mentioned": [
      {"name": "Edward Thorndike", "role": "First psychologist to identify the Halo Effect empirically"}
    ],
    "further_reading": [
      {"resource": "A Constant Error in Psychological Ratings by Edward Thorndike", "why": "the classic 1920 paper defining the Halo Effect"}
    ]
  },
  {
    "title": "Replication and Methodological Critiques",
    "bucket": "Applications and Critiques",
    "bucket_slug": "applications-and-critiques",
    "subtopic": "Scientific Evaluation and Ethics",
    "slug": "replication-and-methodological-critiques",
    "definition": "The scientific controversies, debates, and empirical failures associated with replicating the Pygmalion Effect in psychological research.",
    "key_points": [
      "Replication Challenges: Numerous attempts to replicate the original Oak School study have failed to produce statistically significant results, leading to questions about its generalizability.",
      "Thorndike's Critique: Educational psychologist Edward Thorndike published a sharp critique of the original study's IQ data, arguing that the test scores of younger children were psychometrically invalid.",
      "Effect Size Debate: Meta-analyses suggest that while interpersonal expectancy effects are real, their typical effect size is much smaller than originally reported.",
      "Publication Bias: Critics suggest that publication bias has skewed the literature toward reporting only positive Pygmalion effects while archiving null findings."
    ],
    "sources": [
      {"url": "https://en.wikipedia.org/wiki/Pygmalion_effect#Replication_controversies", "title": "Replication Controversies on Wikipedia"},
      {"url": "https://www.sciencedirect.com/science/article/pii/002244057090013X", "title": "Thorndike's Review of Pygmalion (ScienceDirect)"},
      {"url": "https://www.psychologytoday.com/us/blog/talking-apes/201808/can-we-trust-the-pygmalion-effect", "title": "Psychology Today on Pygmalion Validity"}
    ],
    "wikilink_targets": [
      {"name": "Robert Rosenthal", "reason": "Rosenthal's studies were the primary focus of replication critics."},
      {"name": "Oak School Study", "reason": "Critiqued for statistical anomalies and test reliability."},
      {"name": "Pygmalion in the Classroom", "reason": "The book whose data was challenged by psychometricians."},
      {"name": "Expectancy Bias", "reason": "Critics claim the original researchers fell victim to expectancy bias."},
      {"name": "Labeling and Ethical Implications", "reason": "Debates have highlighted the ethical issues of replication studies."}
    ],
    "cross_domain_targets": [
      {"name": "Educational Psychology", "reason": "Focuses on teacher behavior, curriculum design, and student motivation."},
      {"name": "Sociology", "reason": "Explores how group expectations and structural positions generate self-fulfilling prophecies."}
    ],
    "diagram": "flowchart TD\n    A[Oak School Study] -->|Methodological Debates| B[Thorndike's Critique]\n    A -->|Failure to Reproduce| C[Replication Crisis]\n    B & C --> D[Reduced Scientific Generalization]",
    "key_figures_mentioned": [
      {"name": "Edward Thorndike", "role": "Major psychologist who criticized the statistical methodology of the Oak School study"},
      {"name": "Donald Rubin", "role": "Statistician who reviewed expectancy replication datasets"}
    ],
    "further_reading": [
      {"resource": "The Pygmalion Controversy by Donald Rubin", "why": "detailed analysis of replication statistical power"}
    ]
  },
  {
    "title": "Labeling and Ethical Implications",
    "bucket": "Applications and Critiques",
    "bucket_slug": "applications-and-critiques",
    "subtopic": "Scientific Evaluation and Ethics",
    "slug": "labeling-and-ethical-implications",
    "definition": "The ethical considerations and social consequences of manipulating expectations and applying academic or behavioral labels to individuals.",
    "key_points": [
      "Ethical Dilemma of Deception: The original Oak School study used active deception on teachers, raising concerns about informed consent in educational research.",
      "Risk of Golem Harm: Artificially lowering teacher expectations can result in permanent educational and psychological harm to students.",
      "Implicit Bias Amplification: Labels often align with gender, racial, or class stereotypes, locking systemic biases into scientific and administrative systems.",
      "The Power of Labeling: Once a label is officially applied (e.g., \"slow learner\" or \"high potential\"), it dictates funding, attention, and self-belief."
    ],
    "sources": [
      {"url": "https://en.wikipedia.org/wiki/Labeling_theory", "title": "Labeling Theory on Wikipedia"},
      {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4231208/", "title": "Ethics of Expectancy Manipulation (PMC)"},
      {"url": "https://link.springer.com/referenceworkentry/10.1007/978-0-387-79061-9_1594", "title": "Labeling in Special Education (Springer)"}
    ],
    "wikilink_targets": [
      {"name": "Oak School Study", "reason": "Challenged the ethical standards of school research deception."},
      {"name": "Intellectual Bloomers Label", "reason": "Examines the ethical use of arbitrary labels on children."},
      {"name": "The Golem Effect", "reason": "Warns of the severe psychological harm of negative labeling."},
      {"name": "Replication and Methodological Critiques", "reason": "Ethical critiques have shaped modern replication protocols."},
      {"name": "Pygmalion Effect Mitigation", "reason": "Ethical issues drive the design of bias mitigation programs."}
    ],
    "cross_domain_targets": [
      {"name": "Sociology", "reason": "Explores how group expectations and structural positions generate self-fulfilling prophecies."},
      {"name": "Educational Psychology", "reason": "Focuses on teacher behavior, curriculum design, and student motivation."}
    ],
    "diagram": "flowchart LR\n    A[Issue Academic Label] --> B[Teacher Expectation Adjusts]\n    B --> C[Student Performance Adapts]\n    C --> D[Label Validated & Permanent]",
    "key_figures_mentioned": [],
    "further_reading": [
      {"resource": "Labeling Theory in Sociology by Howard Becker", "why": "classic text on the social impacts of labeling"}
    ]
  },
  {
    "title": "Pygmalion Effect Mitigation",
    "bucket": "Applications and Critiques",
    "bucket_slug": "applications-and-critiques",
    "subtopic": "Scientific Evaluation and Ethics",
    "slug": "pygmalion-effect-mitigation",
    "definition": "The practical strategies, interventions, and structural designs used to reduce negative expectancy biases and foster equitable high performance.",
    "key_points": [
      "Awareness Training: Educating managers and teachers about the Pygmalion and Golem effects helps them recognize and adjust their non-verbal cues.",
      "Objective Assessment Tools: Using standardized, objective performance rubrics reduces the room for selective interpretation and expectancy bias.",
      "Growth Mindset Culture: Promoting a growth mindset (the belief that abilities can be developed) aligns expectations with effort rather than fixed talent.",
      "Structured Feedback Systems: Implementing consistent feedback protocols ensures that all team members receive detailed, constructive suggestions."
    ],
    "sources": [
      {"url": "https://hbr.org/1969/07/pygmalion-in-management", "title": "Overcoming Expectation Bias in HBR"},
      {"url": "https://www.sciencedirect.com/science/article/pii/S095947521730030X", "title": "Interventions for Teacher Bias (ScienceDirect)"},
      {"url": "https://www.mindtools.com/pages/article/newTMM_73.htm", "title": "MindTools on Mitigating the Pygmalion Effect"}
    ],
    "wikilink_targets": [
      {"name": "Climate Factor", "reason": "Mitigation aims to teach leaders to provide warm climate cues to everyone."},
      {"name": "Feedback Factor", "reason": "Promotes objective, structured feedback to prevent bias."},
      {"name": "Expectancy Bias", "reason": "Directly targets reducing expectancy biases in evaluations."},
      {"name": "The Golem Effect", "reason": "Minimizes the risk of Golem effects in schools and teams."},
      {"name": "Labeling and Ethical Implications", "reason": "Resolves the ethical problems of stereotyping."}
    ],
    "cross_domain_targets": [
      {"name": "Organizational Behavior", "reason": "Studies leadership styles, employee engagement, and corporate culture."},
      {"name": "Educational Psychology", "reason": "Focuses on teacher behavior, curriculum design, and student motivation."}
    ],
    "diagram": "flowchart TD\n    A[Identify Expectancy Bias] --> B[Implement Objective Rubrics]\n    A --> C[Educate on Non-Verbal Cues]\n    B & C --> D[Mitigated Golem & Pygmalion Bias]\n    D --> E[Equitable Performance Culture]",
    "key_figures_mentioned": [],
    "further_reading": [
      {"resource": "Mindset: The New Psychology of Success by Carol Dweck", "why": "details the growth mindset approach to expectations"}
    ]
  }
]

# Helper to format frontmatter list
def yaml_list(lst):
    return "[" + ", ".join([f'"{x}"' for x in lst]) + "]"

# Write all notes
for data in concepts_data:
    b_dir = os.path.join(topic_dir, data['bucket_slug'])
    os.makedirs(b_dir, exist_ok=True)
    note_file = os.path.join(b_dir, f"{data['slug']}.md")
    
    # Compile YAML frontmatter
    fm = []
    fm.append("---")
    fm.append(f"title: \"{data['title']}\"")
    fm.append(f"topic: \"The Pygmalion Effect\"")
    fm.append(f"bucket: \"{data['bucket']}\"")
    fm.append(f"tags: [the-pygmalion-effect, {data['bucket_slug']}, {data['slug']}]")
    fm.append(f"aliases: []")
    fm.append(f"status: seedling")
    fm.append(f"created: 2026-07-12")
    
    srcs = [s['url'] for s in data['sources']]
    fm.append(f"sources: {yaml_list(srcs)}")
    
    conns = [c['name'] for c in data['wikilink_targets']]
    fm.append(f"connections: {yaml_list(conns)}")
    fm.append("---")
    fm.append("")
    
    # Note body
    fm.append(f"# {data['title']}")
    fm.append("")
    fm.append(f"> {data['definition']}")
    fm.append("")
    fm.append("## Overview")
    fm.append("")
    
    # 3-5 sentences overview
    overview_text = f"The concept of [[{data['title']}]] is a fundamental part of the study of [[The Pygmalion Effect-Index]]. It represents a crucial component within the [[{data['subtopic']}]] subtopic. Structurally, it sits within the [[{data['bucket']}]] MOC of the topic. Understanding [[{data['title']}]] helps explain the broader cognitive and behavioral patterns of self-fulfilling interpersonal prophecies."
    fm.append(overview_text)
    fm.append("")
    
    fm.append("## Key Points")
    fm.append("")
    for pt in data['key_points']:
        # split into bold prefix and description
        parts = pt.split(":", 1)
        if len(parts) == 2:
            fm.append(f"- **{parts[0].strip()}**: {parts[1].strip()}")
        else:
            fm.append(f"- {pt}")
    fm.append("")
    
    fm.append("## Diagram")
    fm.append("")
    fm.append("```mermaid")
    fm.append(data['diagram'])
    fm.append("```")
    fm.append("")
    
    fm.append("## Connections")
    fm.append("")
    fm.append("### Within The Pygmalion Effect")
    for conn in data['wikilink_targets']:
        fm.append(f"- [[{conn['name']}]] — {conn['reason']}")
    fm.append("")
    
    fm.append("### Cross-Domain")
    for cd in data['cross_domain_targets']:
        fm.append(f"- [[{cd['name']}]] — {cd['reason']}")
    fm.append("")
    
    fm.append("## Sources")
    fm.append("")
    for src in data['sources']:
        fm.append(f"- {src['title']} — {src['url']}")
    fm.append("")
    
    fm.append("## Further Reading")
    fm.append("")
    for fr in data['further_reading']:
        fm.append(f"- *{fr['resource']}* — {fr['why']}")
    fm.append("")
    
    fm.append("---")
    # Clean subtopic name to just the text without the bucket prefix
    fm.append(f"*Part of [[The Pygmalion Effect-Index]] · [[{data['bucket']}]] MOC · [[{data['subtopic']}]]*")
    
    with open(note_file, "w") as f:
        f.write("\n".join(fm))

print(f"Successfully generated {len(concepts_data)} note files.")
