count = 0
input_string = input("How high should we count? ")
try:
    MAX = int(input_string)
    while (count < MAX):
        is_even = count % 2 == 0
        if is_even:
            print(count)
        count += 1
except ValueError:
    print("Please run the program again and type a number!")