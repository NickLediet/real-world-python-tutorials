import json
import difflib

from difflib import SequenceMatcher

data = json.load(open("dictionary.json"))

def retrive_def(word):
    return data[word]

word_user = input("Enter a word:\s")

print(retrive_def(word_user.upper()))