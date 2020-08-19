Schedule_working = int(input("Day (0-6)? : "))

if 5 >= Schedule_working > 0 :          #and Schedule_working <= 5 
    print("Go to work")
elif Schedule_working == 0 or Schedule_working == 6 :
    print("Sleep in")
else:
    print("put number between 0 and 6")
