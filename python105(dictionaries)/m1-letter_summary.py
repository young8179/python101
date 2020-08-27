'''#1. Letter Summary
Write a letter_histogram program that asks the user for input, 
and prints a dictionary containing the tally of how many times each letter 
in the alphabet was used in the word. For example:
'''

user_input = input("please enter a word: ")

def letter_count(word):
    letter_dict = {}
    
    for letter in word:
        if letter in letter_dict:
            letter_dict[letter] = letter_dict[letter] + 1
        else:
            letter_dict[letter] = 1
    return letter_dict

result = letter_count(user_input)
print(result)
