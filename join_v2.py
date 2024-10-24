import pandas as pd
import json

# Load the CSV file
csv_file = '35_generated500.csv'
df_csv = pd.read_csv(csv_file, header=None, names=["text", "model", "temperature", "genre", "format", "style", "timestamp"])

# Load the JSONL file
jsonl_file = 'human_dataset/mixed_poems_v2.jsonl'
human_poems = []
with open(jsonl_file, 'r', encoding='utf-8') as f:
    for line in f:
        poem_data = json.loads(line)
        human_poems.append(poem_data['poem'])

# Extract 100 records from each
df_csv_sample = df_csv.head(100)
human_poems_sample = human_poems[:100]

# Label the records
df_csv_sample['label'] = 'machine'
human_poems_sample = [{'text': poem, 'label': 'human'} for poem in human_poems_sample]

# Combine the records
combined_poems = pd.concat([df_csv_sample[['text', 'label']], pd.DataFrame(human_poems_sample)])

# Save to a new JSONL file
output_file = 'combined_poems.jsonl'
with open(output_file, 'w', encoding='utf-8') as f:
    for _, row in combined_poems.iterrows():
        f.write(json.dumps({"text": row['text'], "label": row['label']}) + '\n')

print(f"Combined poems saved to {output_file}")