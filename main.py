import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

# 1️⃣ Create FastAPI app FIRST
app = FastAPI()

# 2️⃣ Create OpenAI client
client = OpenAI()

# 3️⃣ Request model
class ResumeRequest(BaseModel):
    resume_text: str
    job_role: str
    experience_level: str

# 4️⃣ Health check
@app.get("/")
def home():
    return {"status": "Resume AI Backend is running"}

# 5️⃣ Main API
@app.post("/improve-resume")
def improve_resume(data: ResumeRequest):
    prompt = f"""
You are an ATS resume expert for the Indian job market.

Target job role: {data.job_role}
Experience level: {data.experience_level}

Improve the resume below:
- Use professional, simple English
- Make it ATS-friendly
- Add relevant skills if missing
- Use bullet points
- Do not exaggerate

Resume:
{data.resume_text}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return {
        "improved_resume": response.output_text
    }
