# app.py

import streamlit as st
import openai
from utils import extract_text_from_pdf

# Add your API key
openai.api_key = "YOUR_API_KEY"

st.title("📄 AI Resume Analyzer & Job Fit Scorer")

# Upload resume
resume_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

# Paste job description
job_description = st.text_area("Paste Job Description")

if resume_file and job_description:

    # Step 1: Extract resume text
    resume_text = extract_text_from_pdf(resume_file)

    st.success("Resume uploaded successfully!")

    # Step 2: Create prompt
    prompt = f"""
    You are an AI recruiter.

    Analyze the resume and job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Give output in this format:
    1. Match Score (out of 100)
    2. Matched Skills
    3. Missing Skills
    4. Suggestions to improve resume
    """

    # Step 3: Call LLM
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response["choices"][0]["message"]["content"]

    # Step 4: Display output
    st.subheader("📊 Analysis Result")
    st.write(result)