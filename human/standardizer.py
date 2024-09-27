import csv

# Function to replace tabs with newlines in the "Poem" field
def replace_tabs_with_newlines(poem_text):
    return poem_text.replace('\t', '\n')

# Read input CSV and write to output CSV with cleaned "Poem" field
def clean_csv_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Read header and write it unchanged
        header = next(reader)
        writer.writerow(header)
        
        # Process each row, replacing tabs with newlines in the "Poem" field
        for row in reader:
            # Assuming the "Poem" is in the second column (index 1), adjust if necessary
            row[1] = replace_tabs_with_newlines(row[1])
            writer.writerow(row)

# Example usage
input_file = 'human/PoemDataset.csv'  # Replace with your input CSV file path
output_file = 'cleaned_poems.csv'  # The output CSV file path
clean_csv_file(input_file, output_file)