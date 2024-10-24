import pandas as pd
import re

def clean_text(text):
    # Remove invisible and strange unicode characters
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    # Remove leading and trailing whitespace
    text = text.strip()
    # Replace multiple newlines with a single newline
    text = re.sub(r'\n{2,}', '\n', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s{2,}', ' ', text)
    return text

# Load the CSV file
df = pd.read_csv('human_dataset/PoetryFoundationData.csv')

# Apply the cleaning function to each column
df = df.applymap(lambda x: clean_text(x) if isinstance(x, str) else x)

# Save the cleaned dataframe to a new CSV file
df.to_csv('Cleaned_PoetryFoundationData.csv', index=False)