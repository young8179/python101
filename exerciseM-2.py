
bill = float(input("Total bill amount: "))
service = input("Level of service: ")
number_split =  int(input("Split how many ways: "))


if service.lower() == "good" :
    tip = (bill * 0.2)
    bill_total = (bill + tip)
    per_person = bill_total / number_split
    print(f'Tip amount: ${"%.2f" % tip}')
    print(f'Total amount: ${"%.2f" % bill_total}')
    print(f'Amount per person: ${"%.2f" % per_person}')
elif service.lower() == "fair" :
    tip = (bill * 0.15)
    bill_total = (bill + tip)
    per_person = bill_total / number_split
    print(f'Tip amount: ${"%.2f" % tip}')
    print(f'Total amount: ${"%.2f" % bill_total}')
    print(f'Amount per person: ${"%.2f" % per_person}')
elif service.lower() == "bad" :
    tip = (bill * 0.1)
    bill_total = (bill + tip)
    per_person = bill_total / number_split
    print(f'Tip amount: ${"%.2f" % tip}')
    print(f'Total amount: ${"%.2f" % bill_total}')
    print(f'Amount per person: ${"%.2f" % per_person}')
else:
    print("Total bill Should be number, and Choice of Level of service: good, fair, bad.")
