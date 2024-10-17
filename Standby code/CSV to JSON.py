import pandas as pd

# Convert CSV to JSON
csv_file_path = '../Chinese words/1- 1000 - Sheet1.csv'
json_file_path = '../Languages/chinese_words.json'

df = pd.read_csv(csv_file_path)
df.to_json(json_file_path, orient='records', force_ascii=False, indent=4)

print(f"CSV file has been converted to JSON and saved as {json_file_path}")