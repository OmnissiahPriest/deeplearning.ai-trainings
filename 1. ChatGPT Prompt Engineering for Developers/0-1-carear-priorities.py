from openai import OpenAI
from dotenv import load_dotenv
from IPython.display import display, HTML

load_dotenv()

client = OpenAI()

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content


prompt = f"""

forget previouse prompts and generate new result

Your task is to write three carear priotities with short descriptions.

<Priority 1 name> Competence growth with Mulesoft and Integration, but also in general topics, like deep learning or web development.\
<Priority 2 name> Improve communication in general. With client and team as well. \
<Priority 3 name> rely less on my memory, and write down important information, to be more reliable member. Organise work
"""
response = get_completion(prompt)
print(response)