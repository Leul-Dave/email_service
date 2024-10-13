import pandas as pd
import json
import math

# Convert CSV to JSON
csv_file_path = 'cleaned_japanese_words.csv'
json_file_path = 'cleaned_japanese_words.json'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Convert DataFrame rows to dictionaries
json_data = df.to_dict(orient='records')

# Iterate over each dictionary and remove the 'Kanji' field if it's NaN
for entry in json_data:
    # Check if 'Kanji' is NaN (using math.isnan to check for NaN)
    if isinstance(entry.get('Kanji'), float) and math.isnan(entry['Kanji']):
        del entry['Kanji']  # Remove the 'Kanji' field if it is NaN

# Save the cleaned JSON data
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)

print(f"CSV file has been converted to JSON and saved as {json_file_path}")
