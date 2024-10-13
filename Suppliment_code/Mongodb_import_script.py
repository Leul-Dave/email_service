import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['chinese_words_db']
collection = db['words']

# Read the JSON file
with open('../Chinese words/chinese_words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

# Insert the data into MongoDB
result = collection.insert_many(words)

print(f"Inserted {len(result.inserted_ids)} documents into MongoDB")

# Create an index on the 'Simplified' field for faster lookups
collection.create_index('Simplified')

# Close the connection
client.close()