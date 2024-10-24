from openai import OpenAI
import os

client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))


def openai_pure_call(model, temperature, userprompt, systemprompt) -> str:
    completion = client.chat.completions.create(
        messages=[
            {"role": "system", 
             "content": f"{systemprompt}"},
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

    return completion.choices[0].message.content