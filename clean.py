import jsonlines

def clean_dataset(input_file, output_file):
    seen_poems = set()
    valid_labels = {"human", "machine"}

    with jsonlines.open(input_file, 'r') as reader, jsonlines.open(output_file, 'w') as writer:
        for article in reader:
            poem = article.get('Poem')
            label = article.get('Label')

            if isinstance(poem, str) and isinstance(label, str):
                poem = poem.strip()
                if poem and len(poem) > 10 and label in valid_labels:
                    if poem not in seen_poems:
                        writer.write({"Poem": poem, "Label": label})
                        seen_poems.add(poem)
                    else:
                        print(f"Skipping duplicate entry: {article}")
                else:
                    print(f"Skipping invalid entry: {article}")
            else:
                print(f"Skipping invalid entry: {article}")

def main():
    input_file = 'joint_poem_dataset.jsonl'  # Replace with the actual path to your input file
    output_file = 'cleaned_poem_dataset.jsonl'  # Replace with the actual path to your output file

    clean_dataset(input_file, output_file)
    print(f"Cleaned dataset saved to {output_file}")

if __name__ == "__main__":
    main()