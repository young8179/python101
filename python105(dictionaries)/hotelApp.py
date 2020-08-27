hotel = {
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
         }
    },
    '105': {},
}

def is_vacant(which_hotel, rooms):
    if 'guest' in which_hotel[rooms]: 
        print("room is full")
        return True
    else:
        print("room is empty")
        return False



def check_in(rooms, guest_dictionary):
    
    if is_vacant(hotel, rooms):
        print("pick diffrent room")
    else:
        hotel[rooms] = guest_dictionary
        print(hotel[rooms])

guest_1 = {
            'name': 'Heeyong',
            'phone': 45652890
}

print(is_vacant(hotel, '102'))
check_in('102', guest_1)

def check_out(rooms):
    if is_vacant:
        pass
    else:
        hotel[rooms] = ""
    print(hotel)
check_out('102')

#---------------------------------
hotel = {
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
         }
    },
    '105': {},
}
# create function is_vacant
def is_vacant(which_hotel, rooms):
    if "guest" in which_hotel[rooms]:
        return True
    else :
        return False

new_guest = {
        'guest': {
            'name': 'Derek',
            'phone': 8923
         }
}
def check_in(rooms, guest_dictionary):
    if is_vacant(hotel, rooms) :
        print("pick a different a room")
    else:
        hotel[rooms]= guest_dictionary
        print(hotel[rooms],rooms)
print(is_vacant(hotel, '102'))
check_in('102',new_guest)
print(hotel)

#Create a function for check out
def check_out(rooms):
    if is_vacant ==  True:
        return "nothing"
    else :
        hotel[rooms] = {}
    print(hotel)
check_out('102')