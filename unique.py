"""
Author: Paul Sommers
Date written: 11/11/2024
Assignment: Exercise 5-7 - Unique Words
Short Desc: This program reads a text file, extracts unique words, and prints them in alphabetical order. 
"""

# Get the file name from the user
file = input("Enter the input file name: ")

# Initialize an empty list to store unique words
uniqueWords = []

# Open the file
with open(file, 'r') as f:
    
    # Loop through each line
    for text in f:
        
        # Split the line into words
        wordList = text.split()
        
        # Loop through each word
        for word in wordList:
            
            # If the word is unique, add it to the list
            if word not in uniqueWords:
                uniqueWords.append(word)

# Sort the unique words in alphabetical order (capitalized words come first)
uniqueWords.sort()

# Output: Print each unique word
for word in uniqueWords:
    print(word)