
g_list = []
menu = input("menu add/print/remove: ")



while True:
    #print menu
    # ask to pick
    print(menu)
    
    
    #if add,

    while True:
        if menu.lower() == "add":
            add_item = input("add item: ")
            print(add_item)
            g_list.append(add_item)
            while true:
                another_item = input("add another item? ") 
                print(another_item)
                if another_item.lower() == "yes":
                   print(add_item)
                   g_list.append(add_item)
                elif another_item.lower() == "no":
                    break
            

'''    #if remove
        elif another_input.lower() == "remove":
            print(remove_item)

    #print
    ## else break


remove_item = input("what item do you want to remove: ")'''



