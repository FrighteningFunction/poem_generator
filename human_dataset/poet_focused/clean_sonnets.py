import json
import re

def clean_text(text):
    # Remove numbers, punctuation, and the title "SONNET" with surrounding blank characters
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\n\s*SONNET\s*\n', '\n', text)
    # Remove pattern "O\nSONNET <number>\n"
    text = re.sub(r'\nO\nSONNET \d+\n', '\n', text)
    # Remove any remaining "SONNET" titles
    text = re.sub(r'\bSONNET\b', '', text)
    # Remove leading and trailing whitespace
    text = text.strip()
    return text

def read_sonnets(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    # Split sonnets by double newlines
    sonnets = content.split('\n\n')
    # Remove titles and "O" between sonnets
    cleaned_sonnets = []
    for sonnet in sonnets:
        lines = sonnet.split('\n', 1)
        if len(lines) > 1:
            cleaned_sonnet = clean_text(lines[1].replace('\nO\n', '\n'))
            if cleaned_sonnet:  # Ensure non-empty sonnets
                cleaned_sonnets.append(cleaned_sonnet)
    return cleaned_sonnets

def write_jsonl(sonnets, output_path):
    with open(output_path, 'w') as file:
        for sonnet in sonnets:
            json.dump({"text": sonnet}, file)
            file.write('\n')

if __name__ == "__main__":
    input_path = 'C:/Users/szoko/Documents/VSproj/poem_generator/human_dataset/poet_focused/100sonnets_shakespeare.txt'
    output_path = 'C:/Users/szoko/Documents/VSproj/poem_generator/human_dataset/poet_focused/cleaned_sonnets.jsonl'
    sonnets = read_sonnets(input_path)
    write_jsonl(sonnets, output_path)