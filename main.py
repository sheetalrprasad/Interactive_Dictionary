"""
Author: Sheetal Prasad
Date Created: 15 May 2020
Last Modified: 18 May 2020
"""

import json
from difflib import SequenceMatcher
from difflib import get_close_matches

#loading data
data = json.load(open("data/data.json"))

#getting the word definition
def getMeaning(word):
    if word in data:
        prettyPrint(data[word])
    elif word.title() in data:
<<<<<<< HEAD
        prettyPrint(data[word.title()])
    elif len(get_close_matches(word,data.keys(),n=3,cutoff=0.7))>0:
=======
        prettyPrint(data[word.title()])    
    elif len(get_close_matches(word,data.keys(),n=3,cutoff=0.8))>0:
>>>>>>> a85aff86fa1d3d5b54226378e8044c572755e6ed
        closeMatch = getCloseMatch(word)
        check = input("Did you mean "+getCloseMatch(word).upper()+"? [Yes(Y)/No(N)] ")
        if (check=='Y' or check== 'y'):
            getMeaning(closeMatch)
        else:
            wordNotExist(2)
    else:
        wordNotExist(1)

#finding close matches for word
def getCloseMatch(word):
    close_Match = get_close_matches(word,data.keys(),n=3,cutoff=0.7)
    return close_Match[0]

def wordNotExist(code):
    if code == 1:
        print("Word does not exist. Please check the spelling.")
    elif code == 2 :
        print("I did not understand your query. Please try again.")
        
def prettyPrint(definitions):
    for item in definitions:
        print(item)

def prettyPrint(definitions):
    for item in definitions:
        print(item)

#user input
exit_q = ""
while (exit_q!="Y" and exit_q!="y"):
    word = input("Enter a word: ")
    word = word.lower().strip(" ")
    getMeaning(word)
    exit_q = input("Do you want to exit? [Yes(Y)/No(N)]: ")

print("Thank you for using dictionary!!!")
