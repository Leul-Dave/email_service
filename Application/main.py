from datetime import datetime
import random as r
from dotenv import load_dotenv
from pymongo import MongoClient
from Notifications_All import Notify

# Load environment variables
load_dotenv()

# Initialize notification system and database client
notify = Notify()
client = MongoClient('mongodb://localhost:27017/')

db_c = client['chinese_words_db']
collection_c = db_c['words']

db_j = client['japanese_words_db']
collection_j = db_j['words']

db_k = client['korean_words_db']
collection_k = db_k['words']


# Function to get a random Chinese word from MongoDB collection
def get_random_chinese_word():
    total_words = collection_c.count_documents({})
    random_index = r.randint(0, total_words - 1)
    return collection_c.find().limit(1).skip(random_index).next()


chinese_word = get_random_chinese_word()
chinese = chinese_word['Simplified']
pinyin = chinese_word['Pinyin']
meaning_c = chinese_word['Meaning']


def get_random_japanese_word():
    total_words = collection_j.count_documents({})
    random_index = r.randint(0, total_words - 1)
    return collection_j.find().limit(1).skip(random_index).next()


japanese_word = get_random_japanese_word()
hiragana = japanese_word.get('Hiragana')
kanji = japanese_word.get('Kanji')
meaning_j = japanese_word.get('English')


def get_random_korean_word():
    total_words = collection_k.count_documents({})
    random_index = r.randint(0, total_words - 1)
    return collection_k.find().limit(1).skip(random_index).next()


korean_word = get_random_korean_word()
korean = korean_word['Korean']
meaning_k = korean_word['English']


# Function to append words to vocabulary files
def append_to_vocab(file_name, word, translation):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f"{word}-{translation}\n")


# Append words to vocabulary files
append_to_vocab('../Data/chinese_vocabulary.txt', chinese, meaning_c)
append_to_vocab('../Data/korean_vocabulary.txt', korean, meaning_k)
append_to_vocab('../Data/japanese_vocabulary.txt', hiragana, meaning_j)

# Determine whether to send emails based on the weekday
weekday = datetime.now().weekday()
if weekday:
    print(f"Weekday: {weekday}")
    notify.send_mail_k(korean, meaning_k)
    notify.send_mail_c(chinese, pinyin, meaning_c)
    # If kanji exists, include it in the Japanese email
    if kanji:
        notify.send_mail_j(hiragana, kanji, meaning_j)
    else:
        notify.send_mail_j(hiragana, '', meaning_j)
else:
    print('Email not sent: Weekend or an undetected error')

client.close()
