from openai import OpenAI
from src.prompt import system_instruction

client = OpenAI()

messages=[
     {"role": "system", "content": system_instruction}]

def user_input(message, model="gpt-3.5-turbo",temperature=0.6):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content
