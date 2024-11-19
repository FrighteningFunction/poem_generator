import json
import os
import google.generativeai as genai
from tqdm import tqdm

genai.configure(api_key=os.environ["GEMINI_KEY"])

# Initialize Gemini model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are a creative poet. Generate a sonnet in the style of Shakespeare. You must not use any markdown formatting and you only respond with the sonnet, no comments."
)

output_file = 'tdk_code/poem_generator_v2/generated_sonnets.jsonl'
generated_sonnets = []

# Generate sonnets, modify for number of sonnets to generate
with open(output_file, 'a', encoding='utf-8') as f:
    for _ in tqdm(range(94), desc="Generating sonnets", leave=False):
        response = model.generate_content("Generate a sonnet in the style of Shakespeare")
        if response.text:
            generated_sonnet = {"text": response.text.strip()}
            f.write(json.dumps(generated_sonnet) + '\n')

print(f"Generated sonnets saved to {output_file}")