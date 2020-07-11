import json
import os
from difflib import get_close_matches

def search(word):
	
	word = word.lower()
	
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		
		print()
		
		print("Did you mean {} instead?".format(get_close_matches(word, data.keys())[0]))
		decision = input("Enter Y or N: ")
		
		if decision == "Y" or decision == "y":
			return data[get_close_matches(word, data.keys())[0]]
		elif decision == "N" or decision == "n":
			return "Word is not in dictionary."
		else:
			return "Invalid decision. Enter either Y or N."	
	else:
		return "Word is not in dictionary."
	

data = json.load(open(os.getcwd() + "/original.json"))

print()
print("--------------DICTIONARY--------------")
print()

word = input("Enter the word you want to search: ")

ans = search(word)

print()

if type(ans) == list:
	for definition in range(len(ans)):
		print(str(definition + 1) + ". " + ans[definition])
		print()
else:
	print(ans)
