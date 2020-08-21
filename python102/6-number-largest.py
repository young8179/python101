# largest number
numbers = [10, 20, 30, 99, 50, 12, 87, 90, 1, 101, 9182691, 12, -11, 42]

largest_num = 0
for number in numbers:
    if largest_num < number :
        largest_num = number
    else: 
        largest_num = largest_num

print(largest_num)


## other way

numbers.sort()
print(numbers[-1])