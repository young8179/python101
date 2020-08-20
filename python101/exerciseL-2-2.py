find_factors = int(input("insert number: "))

answer = ""
n = 1
while n <= find_factors :

    if find_factors % n == 0 :
        answer += str(n) + " "


    else:
        pass
    n += 1

print(answer)