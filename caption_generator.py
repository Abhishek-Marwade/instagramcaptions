import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_captions(context, style):
    prompt = f"Based on this image description: '{context}', write 3 {style.lower()} Instagram captions."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a social media content expert."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']
