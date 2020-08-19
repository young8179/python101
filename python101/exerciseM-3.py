


print("you have 0 coins")
re_coin = input("Do you want another?")
current_coin = 0

while re_coin.lower() == "yes" :
    current_coin += 1
    print(f"You have {current_coin} coins")
    re_coin = input("Do you want another?")


print("bye")

