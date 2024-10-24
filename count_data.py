import csv

def count_records(filename):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        count = sum(1 for row in reader)
    return count

# Example usage
filename = 'generated_poems2.csv'
print(f'Total records in {filename}: {count_records(filename)}')