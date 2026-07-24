import os
import re

research_dir = "/home/ali/v2/.agents/skills/notes-projection-workspace/iteration-1/eval-0/with_skill/outputs/the-pygmalion-effect/.research"
output_dir = "/home/ali/v2/.agents/skills/notes-projection-workspace/iteration-1/eval-0/with_skill/outputs/the-pygmalion-effect"

concept_to_meta = {
    "the-rosenthal-jacobson-study": ("Foundations", "Historical Context & Discovery", "foundations"),
    "robert-rosenthal": ("Foundations", "Historical Context & Discovery", "foundations"),
    "lenore-jacobson": ("Foundations", "Historical Context & Discovery", "foundations"),
    "mythological-origins": ("Foundations", "Historical Context & Discovery", "foundations"),
    "self-fulfilling-prophecy": ("Foundations", "Theoretical Frameworks", "foundations"),
    "social-expectancy-theory": ("Foundations", "Theoretical Frameworks", "foundations"),
    "behavioral-confirmation": ("Foundations", "Theoretical Frameworks", "foundations"),
    "the-golem-effect": ("Foundations", "Theoretical Frameworks", "foundations"),
    "mediation-pathways": ("Mechanisms", "Psychological Processes", "mechanisms"),
    "affective-climate": ("Mechanisms", "Psychological Processes", "mechanisms"),
    "input-factor": ("Mechanisms", "Psychological Processes", "mechanisms"),
    "output-factor": ("Mechanisms", "Psychological Processes", "mechanisms"),
    "feedback-factor": ("Mechanisms", "Psychological Processes", "mechanisms"),
    "cognitive-dissonance": ("Mechanisms", "Cognitive & Neurological Factors", "mechanisms"),
    "implicit-bias": ("Mechanisms", "Cognitive & Neurological Factors", "mechanisms"),
    "neurobiology-of-expectation": ("Mechanisms", "Cognitive & Neurological Factors", "mechanisms"),
    "classroom-dynamics": ("Applications & Implications", "Educational Applications", "applications-implications"),
    "socioeconomic-expectancy-gap": ("Applications & Implications", "Educational Applications", "applications-implications"),
    "teacher-training-interventions": ("Applications & Implications", "Educational Applications", "applications-implications"),
    "pygmalion-in-leadership": ("Applications & Implications", "Organizational & Leadership Applications", "applications-implications"),
    "the-galatea-effect": ("Applications & Implications", "Organizational & Leadership Applications", "applications-implications"),
    "organizational-culture": ("Applications & Implications", "Organizational & Leadership Applications", "applications-implications"),
    "placebo-and-nocebo-effects": ("Applications & Implications", "Organizational & Leadership Applications", "applications-implications")
}

def parse_research_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    data = {}
    
    concept_match = re.search(r'^CONCEPT:\s*(.*)$', content, re.MULTILINE)
    data['concept'] = concept_match.group(1).strip() if concept_match else ""
    
    slug_match = re.search(r'^SLUG:\s*(.*)$', content, re.MULTILINE)
    data['slug'] = slug_match.group(1).strip() if slug_match else ""
    
    def_match = re.search(r'^DEFINITION:\s*(.*)$', content, re.MULTILINE)
    data['definition'] = def_match.group(1).strip() if def_match else ""
    
    # Extract KEY_POINTS
    kp_section = re.search(r'KEY_POINTS:\s*\n(.*?)(?=\n\s*[A-Z_]+:|\Z)', content, re.DOTALL)
    kp_list = []
    if kp_section:
        for line in kp_section.group(1).strip().split('\n'):
            line = line.strip()
            if line.startswith('-'):
                # strip lead -
                line = line[1:].strip()
                kp_list.append(line)
    data['key_points'] = kp_list

    # Extract SOURCES
    sources_section = re.search(r'SOURCES:\s*\n(.*?)(?=\n\s*[A-Z_]+:|\Z)', content, re.DOTALL)
    sources_list = []
    if sources_section:
        for line in sources_section.group(1).strip().split('\n'):
            line = line.strip()
            if line.startswith('-'):
                line = line[1:].strip()
                sources_list.append(line)
    data['sources'] = sources_list

    # Extract WIKILINK_TARGETS
    wl_section = re.search(r'WIKILINK_TARGETS:\s*\n(.*?)(?=\n\s*[A-Z_]+:|\Z)', content, re.DOTALL)
    wl_list = []
    if wl_section:
        for line in wl_section.group(1).strip().split('\n'):
            line = line.strip()
            if line.startswith('-'):
                line = line[1:].strip()
                wl_list.append(line)
    data['wikilink_targets'] = wl_list

    # Extract CROSS_DOMAIN_TARGETS
    cd_section = re.search(r'CROSS_DOMAIN_TARGETS:\s*\n(.*?)(?=\n\s*[A-Z_]+:|\Z)', content, re.DOTALL)
    cd_list = []
    if cd_section:
        for line in cd_section.group(1).strip().split('\n'):
            line = line.strip()
            if line.startswith('-'):
                line = line[1:].strip()
                cd_list.append(line)
    data['cross_domain_targets'] = cd_list

    # Extract DIAGRAM
    diagram_match = re.search(r'DIAGRAM:\s*\n(.*?)(?=\n\s*[A-Z_]+:|\Z)', content, re.DOTALL)
    if diagram_match:
        diag = diagram_match.group(1).strip()
        # strip ```mermaid or <mermaid> if exists
        diag = re.sub(r'^```mermaid\s*', '', diag)
        diag = re.sub(r'^<mermaid>\s*', '', diag)
        diag = re.sub(r'\s*```$', '', diag)
        diag = re.sub(r'\s*</mermaid>$', '', diag)
        data['diagram'] = diag.strip()
    else:
        data['diagram'] = ""

    # Extract FURTHER_READING
    fr_section = re.search(r'FURTHER_READING:\s*\n(.*?)(?=\n\s*[A-Z_]+:|\Z)', content, re.DOTALL)
    fr_list = []
    if fr_section:
        for line in fr_section.group(1).strip().split('\n'):
            line = line.strip()
            if line.startswith('-'):
                line = line[1:].strip()
                fr_list.append(line)
    data['further_reading'] = fr_list

    return data

for filename in os.listdir(research_dir):
    if not filename.endswith('.md'):
        continue
    slug = filename[:-3]
    if slug not in concept_to_meta:
        continue
        
    bucket_name, subtopic_name, bucket_slug = concept_to_meta[slug]
    research_path = os.path.join(research_dir, filename)
    data = parse_research_file(research_path)
    
    # Let's verify we parsed it
    print(f"Parsed {slug}: {data['concept']} with {len(data['key_points'])} key points")
