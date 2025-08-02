
import tkinter as tk
from tkinter import filedialog
from resume_parser import parse_resume
from jd_parser import parse_job_description
from scorer import compute_match_score

def choose_file(title, filetypes):
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(title=title, filetypes=filetypes)

# Ask user to choose resume and job description files
resume_path = choose_file("Select Resume File", [("PDF files", "*.pdf"), ("DOCX files", "*.docx")])
jd_path = choose_file("Select Job Description File", [("Text files", "*.txt")])

resume_data = parse_resume(resume_path)
jd_data = parse_job_description(jd_path)

score_details = compute_match_score(resume_data, jd_data)

print("\nGHOSTEYE MATCH RESULT")
print("----------------------")
print(f"Match Score: {score_details['total_score']:.2f} / 100")
print("Details:")
for k, v in score_details['breakdown'].items():
    print(f"  {k}: {v:.2f} / 100")

