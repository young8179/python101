
size =  3
board = []

for y in range(size):
    board.append([])
    for x in range(size):
        board[y].append("[%d][%d]" % (y, x))

for row in board :
    for column in row:
        print("%s " % column, end = "")
    print("\n")

print("\n\nPlayer X is moving.\n\n")
board[0][2] = "X"

for row in board :
    for column in row:
        print("%s " % column, end = "")
    print("\n")

print("\n\nPlayer Y is moving.\n\n")
board[1][1] = "Y"

for row in board :
    for column in row:
        print("%s " % column, end = "")
    print("\n")

print("\n\nPlayer X is moving.\n\n")
board[2][2] = "X"

for row in board :
    for column in row:
        print("%s " % column, end = "")
    print("\n")

    print("\n\nPlayer Y is moving.\n\n")
board[1][2] = "Y"

for row in board :
    for column in row:
        print("%s " % column, end = "")
    print("\n")

print("\n\nPlayer X is moving.\n\n")
board[1][0] = "X"

for row in board :
    for column in row:
        print("%s " % column, end = "")
    print("\n")

print("\n\nPlayer Y is moving.\n\n")
board[0][1] = "Y"

for row in board :
    for column in row:
        print("%s " % column, end = "")
    print("\n")

print("\n\nPlayer X is moving.\n\n")
board[2][1] = "X"

for row in board :
    for column in row:
        print("%s " % column, end = "")
    print("\n")

print("\n\nPlayer Y is moving.\n\n")
board[2][0] = "Y"

for row in board :
    for column in row:
        print("%s " % column, end = "")
    print("\n")

    print("\n\nPlayer X is moving.\n\n")
board[0][0] = "X"

for row in board :
    for column in row:
        print("%s " % column, end = "")
    print("\n")




