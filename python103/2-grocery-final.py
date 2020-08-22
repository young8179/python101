
g_list = []
another_input = "yes"



while True:
    #print menu
    # ask to pick
    menu = input("pick what you want? add/print/remove/exit: ")
    print(menu)
   
   #if add,
    while True:
         
        if menu == "add" :
            item_input = input("add item: ")
            g_list.append(item_input)
            other_input = input("add another? yes or no ")

            if other_input.lower() == "no":
                 break
            elif other_input.lower() != "yes" and other_input != "no":  ##invalid input for yes or no
                print("invalid input.")
                break
#if remove
    
        elif menu == "remove":
            remove_input = int(input("type number of item: "))
            del g_list[remove_input-1]
            break
    
# if print 
        elif menu == "print" :
            
            for item in range(len(g_list)) :
                print(f"{item+1}. " + g_list[item] )
                
            break
#if exit 
        elif menu == "exit":
            quit()
        else:                                                   #invalid input for menu
            print("invalid input")
            break
