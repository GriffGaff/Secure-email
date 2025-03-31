import pandas as pd

def clean_text(value):
    """Removes non-breaking spaces and trims leading/trailing spaces from text fields."""
    if isinstance(value, str):
        return value.replace('\u00A0', ' ').strip()  # Replace & Trim
    return value

def clean_file(input_file, output_file):
    """Reads a CSV/Excel file, cleans text fields, and saves the cleaned file."""
    
    # Determine file type (Excel or CSV)
    if input_file.endswith('.xlsx'):
        df = pd.read_csv(input_file, dtype=str)  # Read CSV with all columns as text
    else:
        df = pd.read_excel(input_file, dtype=str)  # Read Excel file

    # Apply cleaning function to all text fields
    df = df.applymap(clean_text)

    # Save cleaned file
    if output_file.endswith('.xlsx'):
        df.to_csv(output_file, index=False)  # Save as CSV
    else:
        df.to_excel(output_file, index=False)  # Save as Excel
    
    print(f"Cleaned file saved as: {output_file}")

# Example Usage:
input_path = "C:\Users\bolaj\Documents\Proxima Forte\pensioners_2011_2014.xlsx"  # Change this to your file path
output_path = "cleaned_data.xlsx"
clean_file(input_path, output_path)
