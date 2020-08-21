# smallest number
numbers = [10, 20, 30, 99, 50, 12, 87, 90, 1, 101, 9182691, 12, -11, 42]

smallest_num = 0
for index in range(len(numbers)):
    if smallest_num > numbers[index] :
       smallest_num = numbers[index]
    else: 
        smallest_num = smallest_num

print(smallest_num)
