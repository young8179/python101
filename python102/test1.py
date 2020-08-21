def calculate_sum(number_list):
    if len(number_list) == 0:
        return 0
    else:
        return number_list[0] + calculate_sum(number_list[1:])
    
the_sum = calculate_sum(range(100))
print(the_sum)