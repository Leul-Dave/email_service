from datetime import datetime
import random as r
from dotenv import load_dotenv
from pymongo import MongoClient
from Notifications_All import Notify
import json

# Load environment variables
load_dotenv()

# Initialize notification system and database client
notify = Notify()
client = MongoClient('mongodb://localhost:27017/')
db = client['chinese_words_db']
collection = db['words']


# Function to get a random Chinese word from MongoDB collection
def get_random_chinese_word():
    total_words = collection.count_documents({})
    random_index = r.randint(0, total_words - 1)
    return collection.find().limit(1).skip(random_index).next()


# Function to get a random word from a JSON file
def get_random_word_from_json(file_path, word_key, translation_key, kanji_key=None):
    with open(file_path, 'r', encoding='utf-8') as f:
        words = json.load(f)
    random_word = r.choice(words)

    word = random_word[word_key]
    translation = random_word[translation_key]

    if kanji_key and kanji_key in random_word and random_word[kanji_key]:  # Check if kanji exists and is not empty
        kanji_ = random_word[kanji_key]
    else:
        kanji_ = None  # No kanji available

    return word, translation, kanji_


# Function to append words to vocabulary files
def append_to_vocab(file_name, word, translation):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f"{word} - {translation}\n")


# Get random Chinese word from MongoDB
chinese_word = get_random_chinese_word()
chinese = chinese_word['Simplified']
pinyin = chinese_word['Pinyin']
meaning = chinese_word['Meaning']

# Get random Korean word from JSON file
korean, k_english, _ = get_random_word_from_json('./Korean words/korean_words.json', 'Korean', 'English')

# Get random Japanese word and kanji (if available) from JSON file
japanese, j_english, kanji = get_random_word_from_json('./Japanese words/cleaned_japanese_words.json', 'Hiragana',
                                                       'English', 'Kanji')

# Append words to vocabulary files
append_to_vocab('chinese_vocabulary.txt', chinese, meaning)
append_to_vocab('korean_vocabulary.txt', korean, k_english)
append_to_vocab('japanese_vocabulary.txt', japanese, j_english)
# Determine whether to send emails based on the weekday
weekday = datetime.now().weekday()
if weekday:
    print(f"Weekday: {weekday}")
    # notify.send_mail_k(korean, k_english)
    notify.send_mail_c(chinese, pinyin, meaning)
    # If kanji exists, include it in the Japanese email
    # if kanji:
    #     notify.send_mail_j(japanese, kanji, j_english)
    # else:
    #     notify.send_mail_j(japanese, '', j_english)
else:
    print('Email not sent: Weekend or an undetected error')

client.close()
