''' Caesar Cipher
Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"'''

try:
    sentence = input("input sentence: ")
    shift = int(input("shift: "))
    alpha = "abcdefghijklmnopqrstuvwxyz"
    caesar = ""
    translation = ""

## make caesar alphabet

    if shift < 26:
        caesar = caesar + alpha[shift: ] + alpha[0:shift] 


    ## translate 
        for letters in sentence :
            if letters == " ":
                translation = translation + letters
            elif letters != " ":
                translation = translation + caesar[alpha.index(letters)]
        print(translation)

    else:
        print("insert number between 0 and 25")
except ValueError:
      print("invalid input")


## andswer = you must unlean what you have learned (shift 13)