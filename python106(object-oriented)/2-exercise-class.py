class Person:
    
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
         self.friends = []
         self.greeting_count = 0

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}\n{self.name}'s phone number: {self.phone}")
    
    def add_friend(self, other_friend):
        self.friends.append(other_friend)
        print(self.friends)
    def num_friends(self):
        print(len(self.friends))
    
        
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")

jordan = Person("Jordan", "jordan@aol.com", "495-586-3456" )

sonny.greet(jordan)
jordan.greet(sonny)
print(sonny.email,sonny.phone)
print(jordan.email,jordan.phone)

print("---------------------------------------------------")
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.make, self.model, self.year)

car = Vehicle("Tesla", "CyberTruck", 2022)

print(car.make, car.model, car.year)
car.print_info()

sonny.print_contact_info()
jordan.print_contact_info()


sonny.friends.append("jordan")


print(len(jordan.friends))
print("------------------------")
jordan.add_friend("sonny")
jordan.num_friends()
print(jordan.friends)
print(sonny.friends)
jordan.add_friend("heeyoung")

print("-------------------------")
sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(jordan)
jordan.greet(sonny)
print(sonny.greeting_count)
print(jordan.greeting_count)

