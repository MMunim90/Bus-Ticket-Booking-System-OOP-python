from time import sleep
import random
class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        booked_seats = 0
        
    def available_seats(self):
        pass
    
    def book_seat(self):
        pass
    
class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus
        
    def book_ticket(self, bus_number, name, phone):
        pass
    
def show_buses():
    pass
        
class BusSystem:
    buses_list = []
    passengers_list = []
    
class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def add_bus(self, number, route, seats):
        pass
    
    def admin_login():
        while True:
            print("\n\t --- Welcome Admin --- ")
            print("1. Add Bus. ")
            print("2. View All Buses. ")
            print("3. Logout. ")
            
            opt = int(input("Enter your choice: "))
            
            if opt == 1:
                number = input("Enter bus number: ")
                route = input("Enter route: ")
                seats = int(input("Enter seats: "))
                Admin.add_bus(number, route, seats)
                
            elif opt == 2:
                show_buses()
                
            elif opt == 3:
                print("Please wait...")
                sleep(random.randint(2, 3))
                break
            
            else:
                print("Incorrect choice!!!")
    
while True:
    print("\n\t --------- Welcome ---------")
    print("1. Admin Login. ")
    print("2. Book Ticket. ")
    print("3. View Buses. ")
    print("4. Exit. ")
    
    option = int(input("Enter your choice: "))
    
    if option == 1:
        username = input("Enter admin username: ")
        if username != 'admin':
            print("Admin username is incorrect")
        else:
            password = input("Enter admin password: ")
            if password != '1234':
                print("Admin password is incorrect")
            else:
                Admin.admin_login()
        
    elif option == 2:
        bus_number = input("Enter bus number: ")
        name = input("Enter your name: ")
        phone = input("Enter your phone: ")
        Passenger.book_ticket(bus_number, name, phone)
        
    elif option == 3:
        show_buses()
        
    elif option == 4:
        print("Thank you for being with us!!!")
        sleep(2)
        print("Hopefully see you again!!!")
        sleep(2)
        break
    
    else:
        print("Incorrect choice!!!")