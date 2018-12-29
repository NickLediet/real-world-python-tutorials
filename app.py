import json
import difflib

from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def retrive_def(word):
    word = word.upper()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        return ("Did you mean %s instead?" % get_close_matches(word, data.keys())[0])
    else:
        return ("The Word doesn't exist, please double check it.")


word_user = input("Enter a word:\n")

print(retrive_def(word_user))