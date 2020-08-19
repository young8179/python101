print("Total bill Should be number, and Choice of Level of service: good, fair, bad.")

bill = float(input("Total bill amount: "))
service = input("Level of service: ")

if service.lower() == "good" :
    tip = bill * 0.20
    bill_total = bill + tip
    print('Tip amount: ' + "$" + "%.2f" % tip)
    print('Total amount: ' + "$" + "%.2f" % bill_total)

elif service.lower() == "fair" :
    tip = bill * 0.15
    bill_total = bill + tip
    print(f'Tip amount: ${"%.2f" % tip}')
    print(f'Total amount: ${"%.2f" % bill_total}')
elif service.lower() == "bad" :
    tip = bill * 0.10
    bill_total = bill + tip
    print(f'Tip amount: ${"%.2f" % tip}')
    print(f'Total amount: ${"%.2f" % bill_total}')
else:
    print("Invalid input. Choice of Level of service: good, fair, bad.")
