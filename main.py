from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ResumeRequest(BaseModel):
    resume_text: str
    job_role: str
    experience_level: str


@app.get("/")
def home():
    return {"status": "Resume AI Backend is running"}


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

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You help people get jobs."},
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "improved_resume": completion.choices[0].message.content
    }
