resume_prompt = """
You are an AI assistant. Analyze the following resume and extract:
1. Name
2. Summary
3. Skills
4. Work Experience
5. Projects
6. Education

Resume Text:
{resume_text}
"""

fit_prompt = """
Given the extracted resume info and this job description, do the following:
1. Score the candidate's fit (0-100)
2. Explain why the candidate fits/doesn't fit
3. Suggest 3 improvements to the resume

Resume Info:
{resume_info}

Job Description:
{job_description}
"""
