'''1st (out of 1) project from the course - text dictionary'''
import json
from difflib import get_close_matches as gcm
source = json.load(open("data.json"))


def search_dict(word):
    if word.title() in source:
        return source[word.title()]
    elif word in source:
        return source[word]
    elif word.upper() in source:
        return source[word.upper()]
    elif gcm(word, source.keys(), cutoff=0.8) is not []:
        check = input(f"Did you mean {gcm(word, source.keys()) [0]}? Y - yes | N - no: ")
        if check.lower() == "y":
            return source[gcm(word, source.keys()) [0]]
        else:
            return "Sorry, that word is not in dictionary. Please check you typing"
    else:
        return "Sorry, that word is not in dictionary. Please check you typing"
print ("Welcome to dictionary!")
while True:
    w = input("\nPlease enter the word (to exit type 'end'): ").lower()
    if w.lower() == "end":
        break
    results = search_dict(w)
    if type(results) == list:
        for result in results:
            print (str(results.index(result)+1)+". "+result)
    else:
        print ("1. " + results)

