import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_response(message: str, mode: str):

    if mode == "eli5":
        prompt = f"Explain like I am 5 years old: {message}"

    elif mode == "professional":
        prompt = f"Give a professional explanation of: {message}"

    else:
        prompt = message

    response = model.generate_content(prompt)

    return response.text