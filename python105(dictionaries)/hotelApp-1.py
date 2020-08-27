
new_hotel = {}
nice_hotel = {
     '101': {
        'guest': {
            'name': 'asdfd Alderson',
            'phone': 2352626,
            'paid' : 'yes'
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Diejfi Kfeiwoefjo',
            'phone': 142525,
            'paid' : 'no'
         }
    },
    '105': {},
}

good_hotel = {
     '201': {
        'guest': {
            'name': 'Pdfeg Alderson',
            'phone': 2352626,
            'paid' : 'yes'
            
        }
    },
    '202': {},
    '203': {},
    '204': {
        'guest': {
            'name': 'Yefoj Kfeiwoefjo',
            'phone': 142525,
            'paid' : 'yes'

         }
    },
    '205': {},
}

better_hotel = {
     '301': {
        'guest': {
            'name': 'Pfvdbn',
            'phone': 2352626,
            'paid' : 'yes'
        }
    },
    '302': {},
    '303': {},
    '304': {
        'guest': {
            'name': 'Ydfo',
            'phone': 142525,
            'paid' : 'no'
         }
    },
    '305': {},
}

hotels = [nice_hotel, good_hotel, better_hotel, new_hotel]

def print_status():
    for hotel in hotels:
        for key in hotel.keys():
            if hotel[key]:
                print(f"{key} Guest name: {hotel[key]['guest']['name']}.")
                print(f"{key} Guest phone: {hotel[key]['guest']['phone']}.")
            else:
                print(f"Room {key} is empty.")


def check_in2(user_checkin_hotel, user_checkin_room):
    if 'guest' not in hotels[user_checkin_hotel][user_checkin_room] :
        name_input = input("what is your name: ")
        phone_input = input("what is your phone number: ")
        paid_input = input("Do you want to pay now? yes or no : ")
        guest_info = {'guest': {'name': name_input,
                            'phone': phone_input,
                            'paid': paid_input.lower()}}
        hotels[user_checkin_hotel][user_checkin_room].update(guest_info)
        
    else:
        print("-----------------------")
        print("The room is occupied")
        print(f"current guest: {hotels[user_checkin_hotel][user_checkin_room]}")
        print("-----------------------")
    return print_status()    

def check_out(hotel, room):
    if 'guest' in hotels[hotel][room] and hotels[hotel][room]['guest']['paid'] == 'yes': 
       del hotels[hotel][room]['guest']
    elif hotels[hotel][room]['guest']['paid'] == 'no':
        print("--------------------")
        print("Need to pay")
        print("--------------------")
    else:
        print("No guest in the room")
    return print_status()


while True:
    user_input = int(input("""\nMain Menu
    \nWhat would you like to do?
    \n[1] Print hotel room status
    \n[2] Check in customer
    \n[3] Check out customer
    \n[4] Quit
    \n[5] Open a new hotel
    \n[6] close an existing hotel> """))
    print(user_input)
    
    if user_input == 1:
        print_status()
    elif user_input == 2:
        print("list of hotel: \n0. nice_hotel\n1. good_hotel\n2. better_hotel")
        user_checkin_hotel = int(input("type the number: "))
        user_checkin_room = input("what room would you like: ")
        check_in2(user_checkin_hotel, user_checkin_room)
    elif user_input == 3:
         print("list of hotel: \n0. nice_hotel\n1. good_hotel\n2. better_hotel")
         check_out_hotel = int(input("what is your hotel: "))
         check_out_room = input("what is your room number: ")
         check_out(check_out_hotel, check_out_room)
    elif user_input == 4:
        quit
    elif user_input == 5:
        open_hotel = list(input("type hotel name: "))
        hotel_open(open_hotel)
    elif user_input == 6:
        print("list of hotel: \n0. nice_hotel\n1. good_hotel\n2. better_hotel")
        close_hotel

    else:
        print("type the number between 1 and 4")

        
        