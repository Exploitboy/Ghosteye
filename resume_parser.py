from pyresparser import ResumeParser

def parse_resume(file_path):
    data = ResumeParser(file_path).get_extracted_data()
    return {
        'skills': data.get('skills', []),
        'experience': data.get('total_experience', 0),
        'education': data.get('degree', [])
    }
