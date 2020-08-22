'''Take a user's input for a number, and then print out all
numbers from 1 to that number. For any number
divisible by 3, print 'fizz'. For any number divisible by
5, print 'buzz'. Any number divisible by 3 AND 5, print
'fizzbuzz'. '''

user_input = int(input("give me a number: "))

number = 1

while number <= user_input:
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 5 == 0 :
        print("buzz")
    elif number % 3 == 0 :
        print("fizz")
    else:
        print(number)
    number += 1
    