import json

#loading data
data = json.load(open("data/data.json"))

#getting the word definition function
def getMeaning(word):
    if word in data:
        for definition in data[word]:
            print(definition)
    else:
        print("Word does not exist. Please check the spelling.")

#user input
exit_q = ""
while (exit_q!="Y" and exit_q!="y"):
    word = input("Enter a word: ")
    word = word.lower().strip(" ")
    getMeaning(word)
    exit_q = input("Do you want to exit? [Y/N]: ")
print("Thank you for using dictionary!!!")
