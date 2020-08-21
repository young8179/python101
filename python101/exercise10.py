
try:
    i = 0
    y = int(input("How big is the square: "))
    j = ""


    while i < y :
        j = "*" * y
        print(j)
        i += 1

except ValueError:
    print("type a number!!!!!!!!!!!!")