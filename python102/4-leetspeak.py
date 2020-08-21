
translator = input("give me sentence: ")
result = ""

for letter in translator:
    if letter.upper() == "A" :
        result = result + "4"
    elif letter.upper() == "E" :
        result = result + "3"
    elif letter.upper() == "G" :
        result = result + "6"
    elif letter.upper() == "I" :
        result = result + "1"
    elif letter.upper() == "O" :
        result = result + "0"
    elif letter.upper() == "S" :
        result = result + "5"
    elif letter.upper() == "T" :
        result = result + "7"
    else:
        result = result + letter

print(result)

