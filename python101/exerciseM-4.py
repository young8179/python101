
width = int(input("Width? "))
height = int(input("Height? "))
start_end_line = "*" * width


print(start_end_line)

while  height != 2 :
    middle = "*" + " " *  (width - 2) + "*"
    print(middle)
    height -= 1


print(start_end_line)