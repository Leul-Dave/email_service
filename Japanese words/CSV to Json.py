import pandas as pd

# Convert CSV to JSON
csv_file_path = 'cleaned_japanese_words.csv'
json_file_path = 'cleaned_japanese_words.json'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Replace NaN values with empty strings
df = df.fillna('')

# Convert the DataFrame to JSON
df.to_json(json_file_path, orient='records', force_ascii=False, indent=4)

print(f"CSV file has been converted to JSON and saved as {json_file_path}")
