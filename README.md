# AI Resume Analyzer & Job Fit Scorer

This project analyzes a resume against a job description using an LLM.

## Features
- Upload resume PDF
- Paste job description
- Get match score
- Identify missing skills
- Get improvement suggestions

## Tech Stack
- Python
- Streamlit
- OpenAI API
- PyPDF

## How it works
1. Extract text from resume
2. Combine with job description
3. Send prompt to LLM
4. Display structured output

## Run the app
```bash
pip install -r requirements.txt
streamlit run app.py