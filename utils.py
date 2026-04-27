# utils.py

# This file extracts text from PDF resumes

from pypdf import PdfReader

def extract_text_from_pdf(file):
    """Extract text from uploaded PDF"""
    reader = PdfReader(file)
    text = ""
    
    for page in reader.pages:
        text += page.extract_text()
    
    return text