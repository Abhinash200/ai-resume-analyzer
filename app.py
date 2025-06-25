import streamlit as st
import os
import requests
from utils import extract_text_from_pdf
from prompts import resume_prompt, fit_prompt
from dotenv import load_dotenv

# Load API key from .env or Streamlit Secrets
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")

# Streamlit App UI
st.set_page_config(page_title="AI Resume Analyzer", page_icon="🧠")
st.title("🧠 AI Resume Analyzer (Groq LLM)")

# File and Job Description Input
resume_file = st.file_uploader("📄 Upload Your Resume (PDF)", type=["pdf"])
job_description = st.text_area("🧾 Paste Job Description Here")

# Groq API Request Function
def call_groq(prompt, model="mixtral-8x7b-32768"):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.4
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

# Analyze Button Logic
if st.button("🚀 Analyze") and resume_file and job_description:
    with st.spinner("Analyzing your resume with Groq..."):
        resume_text = extract_text_from_pdf(resume_file)

        # Step 1: Extract resume info
        prompt1 = resume_prompt.format(resume_text=resume_text)
        resume_info = call_groq(prompt1)

        # Step 2: Analyze fit with JD
        prompt2 = fit_prompt.format(resume_info=resume_info, job_description=job_description)
        fit_analysis = call_groq(prompt2)

    # Display results
    st.subheader("📌 Extracted Resume Info")
    st.markdown(resume_info)

    st.subheader("📊 Fit Score & Suggestions")
    st.markdown(fit_analysis)
