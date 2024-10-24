# Standalone script for generating titles for poems from a chosen dataset,
# hard coded with dataset,
# model and parameters
# and number of jsonl records to process

import json
import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def openai_pure_call(model, temperature, userprompt, systemprompt) -> str:
    completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": f"{systemprompt}"},
            {"role": "user", "content": f"{userprompt}"}
        ],
        temperature=temperature,
        top_p=1.0,
        max_tokens=50,
        model=model
    )
    return completion.choices[0].message.content

# Read the first 100 records from mixed_poems_v2.jsonl
input_file = 'human_dataset/mixed_poems_v2.jsonl'
output_file = 'poems_titled.jsonl'
poems = []

with open(input_file, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i >= 100:
            break
        poems.append(json.loads(line))

# Generate titles for each poem
results = []
for poem in poems:
    text = poem['poem']
    userprompt = f"Generate a title for the following poem:\n\n{text}"
    systemprompt = "You are a creative poet. Generate a concise and fitting title for the given poem. You must not use any markdown formatting and you only respond with the title, no comments."
    title = openai_pure_call("gpt-4o-mini", 0.7, userprompt, systemprompt)
    results.append({"text": text, "aititle": title.strip()})

# Save the results to a new JSONL file
with open(output_file, 'w', encoding='utf-8') as f:
    for result in results:
        f.write(json.dumps(result) + '\n')

print(f"Titles generated and saved to {output_file}")