import json
import os
import random
import google.generativeai as genai
from tqdm import tqdm

genai.configure(api_key=os.environ["GEMINI_KEY"])

# Initialize Gemini model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are a creative poet. Generate a poem based on the given title or words. You must not use any markdown formatting and you only respond with the title, no comments."
)

# Read the titled poems from poems_titled.jsonl
input_file = 'tdk_code/poem_generator_v2/poems_titled.jsonl'
output_file = 'tdk_code/poem_generator_v2/combined_poems_labeled_v2.jsonl'
poems = []

with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        poems.append(json.loads(line))

# Generate poems for each title
with open(output_file, 'w', encoding='utf-8') as f:
    for poem in tqdm(poems, desc="Generating poems", leave=False):
        title = poem['aititle']
        try:
            response = model.generate_content(f"Generate a poem with this title: {title}")
            if response.text:
                generated_poem = {"text": response.text.strip(), "label": "machine"}
                f.write(json.dumps(generated_poem) + '\n')
                tqdm.write(f"Generated poem for title '{title}'")
            else:
                raise ValueError("Invalid response text")
            
        except ValueError as e:
            try:
                print(f"Error generating poem for title '{title}': {e}")
                # Generate a poem by explicitly asking to avoid inappropriate content
                filtered_poem = model.generate_content(f"Generate a poem with this title, avoiding abusive, explicitly sexual or inappropriate content: {title}")
                generated_poem = {"text": filtered_poem.text.strip(), "label": "machine"}
                f.write(json.dumps(generated_poem) + '\n')
                tqdm.write(f"Generated a filtered poem for title '{title}', poem: {filtered_poem.text.strip()}")
            except ValueError as e:
                print(f"Error generating filtered poem for title '{title}': Generating a neutral poem")
                poem = model.generate_content("Generate a poem")
                generated_poem = {"text": poem.text.strip(), "label": "machine"}
                f.write(json.dumps(generated_poem) + '\n')
                tqdm.write(f"Generated a neutral poem for title '{title}', poem: {poem.text.strip()}")

# Combine human poems with generated poems
combined_poems = []
for poem in poems:
    combined_poems.append({"text": poem['text'], "label": "human"})

# Save the human poems to the JSONL file
with open(output_file, 'a', encoding='utf-8') as f:
    for poem in combined_poems:
        f.write(json.dumps(poem) + '\n')

print(f"Combined poems saved to {output_file}")