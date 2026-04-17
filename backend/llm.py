import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Check your .env file")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")

def generate_ddr(inspection_text, thermal_text):
    prompt = f"""
You are an expert building inspection analyst.

Generate a Detailed Diagnostic Report (DDR).

STRICT RULES:
- Do NOT invent information
- If missing → write "Not Available"
- If conflict → clearly mention conflict
- Avoid duplicate points
- Use simple client-friendly language

OUTPUT FORMAT:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment (with reasoning)
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information

DATA:

INSPECTION REPORT:
{inspection_text}

THERMAL REPORT:
{thermal_text}
"""

    response = model.generate_content(prompt)
    return response.text