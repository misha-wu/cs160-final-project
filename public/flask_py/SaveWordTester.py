import json
import os

file_name = 'Words.json'
path = os.path.dirname(os.path.realpath(__file__))
def read_data_from_file():
    with open(os.path.join(path, file_name), 'r') as file:
        
        data = json.load(file)
        return data

def save_data_to_file(words):
    with open(os.path.join(path, file_name), 'w') as file:
        json.dump(words, file)

# Word should be in a json object
def add_one_word(words, word):
    words[word["phrase"]] = word

def delete_word(words, phrase):
    if isinstance(phrase, str):
        del words[phrase]
    else:
        del words[phrase["phrase"]]
    