import streamlit as st
import os
import requests
from utils import extract_text_from_pdf
from prompts import resume_prompt, fit_prompt
from dotenv import load_dotenv


load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")


st.set_page_config(page_title="AI Resume Analyzer", page_icon="🧠")
st.title("🧠 AI Resume Analyzer (Groq LLM)")


resume_file = st.file_uploader("📄 Upload Your Resume (PDF)", type=["pdf"])
job_description = st.text_area("🧾 Paste Job Description Here")


def call_groq(prompt, model="llama3-70b-8192"):
    if not groq_api_key:
        st.error("❌ API key not found. Please set GROQ_API_KEY in your .env file or Streamlit secrets.")
        return "API key missing."

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

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            st.error(f"❌ Groq API Error: {response.status_code}")
            st.code(response.text, language="json")
            return "Error from Groq API. Check model name or prompt structure."
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Request failed: {str(e)}")
        return "API request failed."


if st.button("🚀 Analyze") and resume_file and job_description:
    with st.spinner("Analyzing your resume with Groq..."):
        resume_text = extract_text_from_pdf(resume_file)

       
        prompt1 = resume_prompt.format(resume_text=resume_text)
        st.subheader("🔍 Debug: Prompt to Extract Resume Info")
        st.code(prompt1, language="text")
        resume_info = call_groq(prompt1)

      
        prompt2 = fit_prompt.format(resume_info=resume_info, job_description=job_description)
        st.subheader("🔍 Debug: Prompt to Evaluate Fit with JD")
        st.code(prompt2, language="text")
        fit_analysis = call_groq(prompt2)

 
    st.subheader("📌 Extracted Resume Info")
    st.markdown(resume_info)

    st.subheader("📊 Fit Score & Suggestions")
    st.markdown(fit_analysis)
