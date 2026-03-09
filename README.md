# AI Resume Analyzer

A Streamlit web app powered by Groq's LLMs that allows users to upload a resume and job description, analyze the candidate's fit, extract key features, and get personalized suggestions—all using generative AI.


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

ai-resume-analyzer/
├── app.py                      # 🔷 Main Streamlit app
├── prompts.py                  # 📄 LLM prompt templates (for extraction & scoring)
├── utils.py                    # ⚙️ Utility functions (PDF parsing, formatting)
├── requirements.txt            # 📦 Python package dependencies
├── .env                        # 🔐 Environment variables (e.g., GROQ_API_KEY)
├── assets/
│   └── demo_screenshot.png     # 🖼️ Optional: for README/media
├── README.md                   # 📘 Project documentation
└── .gitignore                  # 🚫 Ignore files like .env, __pycache__, etc.
