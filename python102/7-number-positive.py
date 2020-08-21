## positive number

numbers = [10, 20, 30, -99, 50, -12, 87, 90, 1, 101, 9182691, 12, -11, 42]

positive_num = []
for number in numbers:
    if number > 0:
        positive_num.append(number)

print(positive_num)