i = 4
j = "*"

while i >= 1 :
    space = " " * (i-1)
    print(space + j + space)
    j += "**"
    i -= 1

