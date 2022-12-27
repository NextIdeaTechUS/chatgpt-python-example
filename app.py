import os
import openai
from dotenv import load_dotenv
load_dotenv()

OPEN_API_KEY = os.getenv("OPEN_API_KEY")
openai.api_key = OPEN_API_KEY

def generate_response(prompt):
    model_engine = "text-davinci-003"
    prompt = (f"{prompt}")

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

prompt = input("Enter your question: ")
response = generate_response(prompt)

print(response)