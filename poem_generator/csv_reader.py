import csv

# Function to retrieve the content of a logged poem from the CSV file
def retrieve_poem_from_csv(csv_file, index):
    poems = []
    
    # Open the CSV file and read its content
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, quoting=csv.QUOTE_ALL)
        
        # Iterate over rows in the CSV and collect them in a list
        for row in reader:
            poems.append(row)

    print(f"Total rows: {len(poems)}")
    # Retrieve the poem at the specified index
    if 0 <= index < len(poems):
        poem_data = poems[index]
        poem_text = poem_data[0]  # Assuming poem text is in the first column
        
        print("Poem Text:", poem_text)
        print("Model:", poem_data[1])
        print("Temperature:", poem_data[2])
        print("Genre:", poem_data[3])
        print("Format:", poem_data[4])
        print("Style:", poem_data[5])
        print("Timestamp:", poem_data[6])
        
        return poem_data
    else:
        print("Index out of range.")
        return None


# Example of usage
csv_file = "generated_poems.csv"
index = 4  # Retrieve the first poem in the CSV
retrieve_poem_from_csv(csv_file, index)