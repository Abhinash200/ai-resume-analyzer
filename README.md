# 🧠 AI Resume Analyzer

A Streamlit web app powered by Groq's LLMs that allows users to upload a resume and job description, analyze the candidate's fit, extract key features, and get personalized suggestions—all using generative AI.

![Streamlit App Screenshot](https://placehold.co/800x400?text=AI+Resume+Analyzer+Demo)

---

## 🚀 Features

- 📄 Upload Resume (PDF)
- 📋 Paste or upload Job Description
- 🤖 LLM-powered skill & experience extraction
- 📊 Candidate-job fit score (0–100)
- 🛠️ Suggestions to improve your resume
- 🔐 Secure Groq API key handling via Streamlit Secrets

---

## 🧪 Tech Stack

| Layer         | Tools Used                                |
|---------------|--------------------------------------------|
| Frontend      | Streamlit                                  |
| LLM API       | Groq (`llama3-70b-8192`)                |
| Resume Parsing| PyMuPDF                                    |
| Backend       | Python, Requests, Prompt Templates         |
| Secrets Mgmt  | Streamlit Secrets (`.env` not committed)   |

---

## 📂 Folder Structure

ai-resume-analyzer/ ├── app.py                      # Main Streamlit app ├── prompts.py                 # LLM prompt templates ├── utils.py                   # Resume extraction utilities ├── requirements.txt           # Python dependencies ├── .env                       # API key (Groq) └── assets
