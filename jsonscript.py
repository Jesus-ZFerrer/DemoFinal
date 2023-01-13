#!/bin/python
# Program to find a palindrome
# Practice No.2
# Created by: Jesus Zepeda Ferrer

import sys
import json  # Import function to create the json file

# w = input("Enter the word:")  # Variable to get the input in terminal manually if you are using and IDE like pycharm just uncomment this line and comment the below
w = sys.argv[1]                 # Variable to get the input in terminal using format "script.py argument"
reverse = w[::-1]               # Variable to reversing a string, list, or any iterable with an ordering.
counter = {}                    # Creating an empty dictionary

# Inside the if statement I do the counter of the letters, and also created the json file if the word is a palindrome
if w == reverse:
    wr = bool(reverse)  # wr is the variable to check if is true or false the word analyzed with the reverse variable declared

# Loop to count the words inside of variable w, this will explore if one word exist put the number 1, and if there are more than 2 words it will increase 1 by 1
    for word in w:
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] += 1

# For loop to show the values ordered instead of dict_items([('o', 2), ('s', 1)])
# So here will be printing the values from counter dictionary word by word with a format letter:number
    for letter, number in counter.items():
        "{}:{}".format(letter, number)

    # JSON file format creation
    file_json = {
        "name": w,
        "palindrome": wr,       # wr is the status True or False
        "sorted": counter,      # counter is the values in the Dictionary
        "length": len(w)        # len counts the number of letters from the word to check
    }
# If the word is not a palindrome then validate if the dictionary contains any value inside if not then set False, and print the JSON file.
else:
    wr = bool(counter)
    # JSON file format creation
    file_json = {
        "name": w,
        "palindrome": wr,
    }

y = json.dumps(file_json, indent=0)  # Convert into JSON the indent=0 is giving the format of the JSON
print(y)                             # The result is a JSON string
