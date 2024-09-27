import csv
from datetime import datetime

# Function to read poem from POEMINPUT.txt and log it to CSV
def log_poem_from_txt_to_csv():
    # Path to the input text file and the CSV file
    poem_input_file = "POEMINPUT.txt"
    csv_file = "generated_poems.csv"

    # Read the poem from the text file
    with open(poem_input_file, mode='r', encoding='utf-8') as file:
        poem_text = file.read().strip()  # Remove any trailing spaces or newlines

    # Timestamp for when the poem is logged
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Data to log, with all fields marked as "undefined" except the timestamp and poem text
    data = [poem_text, "gpt-4o-mini", "undefined", "undefined", "undefined", "undefined", timestamp]

    # Log the poem to the CSV file
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(data)

    print(f"Poem logged successfully with timestamp: {timestamp}")

# Example usage
log_poem_from_txt_to_csv()