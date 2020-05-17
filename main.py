import json
from difflib import SequenceMatcher
from difflib import get_close_matches

#loading data
data = json.load(open("data/data.json"))

#getting the word definition function
def getMeaning(word):
    if word in data:
        for definition in data[word]:
            print(definition)
    elif len(get_close_matches(word,data.keys(),n=3,cutoff=0.7))>0:
        closeMatch = getCloseMatch(word)
        check = input("Did you mean "+getCloseMatch(word).upper()+"? [Y/N] ")
        if (check=='Y' or check== 'y'):
            getMeaning(closeMatch)
        else:
            wordNotExist()
    else:
        wordNotExist()

def getCloseMatch(word):
    close_Match = get_close_matches(word,data.keys(),n=3,cutoff=0.7)
    return close_Match[0]

def wordNotExist():
    print("Word does not exist. Please check the spelling.")

#user input
exit_q = ""
while (exit_q!="Y" and exit_q!="y"):
    word = input("Enter a word: ")
    word = word.lower().strip(" ")
    getMeaning(word)
    exit_q = input("Do you want to exit? [Y/N]: ")

print("Thank you for using dictionary!!!")
