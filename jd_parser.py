def parse_job_description(file_path):
    with open(file_path, 'r') as f:
        text = f.read().lower()

    # Simplified parser for demo
    skills = []
    experience = 0
    education = []

    # Very basic keyword matching (you can expand this with NLP)
    if "python" in text:
        skills.append("Python")
    if "machine learning" in text:
        skills.append("Machine Learning")
    if "bachelor" in text:
        education.append("Bachelor")
    if "3+ years" in text or "3 years" in text:
        experience = 3

    return {
        'skills': skills,
        'experience': experience,
        'education': education
    }