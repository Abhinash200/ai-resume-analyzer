#streamlit-based AI Resume Analyzer and job Fit Evaluator
import streamlit as st
import openai
import os
from utils import extract_text_from_pdf
from prompts import resume_prompt, fit_prompt
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🧠 AI Resume Analyzer (LLM-powered)")

# Upload resume PDF
resume_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste the Job Description")

if st.button("Analyze") and resume_file and job_description:
    with st.spinner("Extracting and analyzing..."):
        resume_text = extract_text_from_pdf(resume_file)

        # Prompt 1: Extract resume info
        prompt1 = resume_prompt.format(resume_text=resume_text)
        response1 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt1}],
            temperature=0.4
        )
        resume_info = response1.choices[0].message.content

        # Prompt 2: Compare with job description
        prompt2 = fit_prompt.format(resume_info=resume_info, job_description=job_description)
        response2 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt2}],
            temperature=0.4
        )
        fit_analysis = response2.choices[0].message.content

    st.subheader("📄 Extracted Resume Info")
    st.markdown(resume_info)

    st.subheader("📊 Fit Score & Recommendations")
    st.markdown(fit_analysis)
