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
