## reverse string
given_string = input("please give me a string: ")

rev_string = ""

for letters in given_string :
    rev_string = str(letters) + rev_string

print(rev_string)

## other way

given_string1 = input("please give me a string: ")

answer = given_string1[::-1]
print(answer)