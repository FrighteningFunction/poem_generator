import csv
import os

def verify_csv(file_path, expected_columns=None, check_empty=False):
    """
    Verifies the structure and content of a CSV file.
    
    Args:
    - file_path (str): Path to the CSV file to verify.
    - expected_columns (list): List of expected column names. Pass None to skip this check.
    - check_empty (bool): If True, the function will check if the CSV contains any empty rows or fields.

    Returns:
    - dict: A dictionary with verification results.
    """
    verification_results = {
        "file_exists": False,
        "correct_columns": False,
        "has_empty_fields": False,
        "total_rows": 0,
        "issues": []
    }
    
    # Check if the file exists
    if not os.path.isfile(file_path):
        verification_results["issues"].append("File does not exist.")
        return verification_results
    verification_results["file_exists"] = True

    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)

            # Check for empty file
            if len(rows) == 0:
                verification_results["issues"].append("The CSV file is empty.")
                return verification_results
            
            # Check total rows
            verification_results["total_rows"] = len(rows)

            # Verify the header if expected_columns is provided
            if expected_columns:
                header = rows[0]
                if header == expected_columns:
                    verification_results["correct_columns"] = True
                else:
                    verification_results["issues"].append("Columns do not match the expected structure.")
                    verification_results["issues"].append(f"Expected: {expected_columns}, Found: {header}")
            
            # Check for empty rows or fields
            if check_empty:
                for i, row in enumerate(rows):
                    if len(row) == 0 or any(field.strip() == "" for field in row):
                        verification_results["has_empty_fields"] = True
                        verification_results["issues"].append(f"Empty row or field found at row {i+1}.")
    
    except Exception as e:
        verification_results["issues"].append(f"Error reading CSV: {e}")
    print("Everything is okay!")
    return verification_results

if __name__=="__main__":
    csv_file = "generated_poems.csv"
    expected_columns = ["poem_text", "model", "genre", "format", "style", "timestamp"]

    result = verify_csv(csv_file, None, check_empty=True)
    print(result)