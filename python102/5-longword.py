

long_word = input("please give me a word: ")
final_translation = ""


for letters in long_word:
    if letters.lower()  not in "aeiou":
       final_translation += letters
    for i in range(len(long_word)-1):
        if letters.lower() in "aeiou" and long_word[i] == long_word[i+1]:
           final_translation = final_translation + (letters * 3 )
        else:
            pass

print(final_translation)

