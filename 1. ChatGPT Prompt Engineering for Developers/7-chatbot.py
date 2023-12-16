from openai import OpenAI
from dotenv import load_dotenv
from redlines import Redlines

load_dotenv()

client = OpenAI()
def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content