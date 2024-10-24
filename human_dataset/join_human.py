import pandas as pd
import json
import random

# Load the CSV file
df1 = pd.read_csv('human_dataset/PoetryFoundationData.csv')

# Load the JSONL file
poems2 = []
with open('human_dataset/old_poems.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        poem_data = json.loads(line)
        poems2.append(poem_data['content'])

# Extract the poem text from the CSV dataset
poems1 = df1['Poem'].dropna().tolist()

# Combine and shuffle the poems
all_poems = poems1 + poems2
random.shuffle(all_poems)

# Save the mixed poems to a JSONL file
with open('MixedPoems.jsonl', 'w', encoding='utf-8') as f:
    for poem in all_poems:
        f.write(json.dumps({"poem": poem}) + '\n')