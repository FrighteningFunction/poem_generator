from openai import OpenAI
import os

# models: "gpt-4o-mini", "gpt-4o"

# Initialize API client
token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"

client = OpenAI(base_url=endpoint, api_key=token)

def openai_api_call(model, temperature, userprompt, systemprompt) -> str:
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"{systemprompt}",
            },
            {
                "role": "user",
                "content": f"{userprompt}",
            }
        ],
        temperature=temperature,
        top_p=1.0,
        max_tokens=300,
        model=model
    )

    return response.choices[0].message.content