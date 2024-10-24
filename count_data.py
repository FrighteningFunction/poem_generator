import csv
import sys

def count_records(filename):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        count = sum(1 for row in reader)
    return count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_data.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    print(f'Total records in {filename}: {count_records(filename)}')