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
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        # self.bus = 
        
    def book_ticket(self, bus_number, name, phone):
        pass
        
class BusSystem:
    def __init__(self):
        self.buses_list = []
        self.passengers_list = []
        
    def add_bus(self, bus):
        self.buses_list.append(bus)
    
    def show_buses(self):
        print("\n---------------------- Bus List -----------------------\n")
        print(f"Number of buses: {len(self.buses_list)} \n")
        for bus in self.buses_list:
            print(f"# Bus number: {bus.number}, Route: {bus.route}, Seats: {bus.total_seats}")
    
class Admin:
    def __init__(self, bus_system):
        self.__username = 'admin'
        self.__password = '1234'
        self.bus_system = bus_system
    
    def login(self, username, password):
        if username != self.__username:
            print("Admin username is incorrect")
        else:
            if password != self.__password:
                print("Admin password is incorrect")
            else:
                self.admin_menu()
    
    def admin_menu(self):
        while True:
            print("\n\t --- Welcome Admin --- ")
            print("1. Add Bus. ")
            print("2. View All Buses. ")
            print("3. Logout. ")
            
            opt = int(input("Enter your choice: "))
            
            if opt == 1:
                number = int(input("Enter bus number: "))
                route = input("Enter route: ")
                total_seats = int(input("Enter seats: "))
                bus = Bus(number, route, total_seats)
                self.bus_system.add_bus(bus)
                
            elif opt == 2:
                self.bus_system.show_buses()
                
            elif opt == 3:
                print("Please wait...")
                sleep(random.randint(2, 3))
                break
            
            else:
                print("Incorrect choice!!!")
    
bus_system = BusSystem()
admin = Admin(bus_system)

while True:
    print("\n\t --------- Welcome ---------")
    print("1. Admin Login. ")
    print("2. Book Ticket. ")
    print("3. View Buses. ")
    print("4. Exit. ")
    
    option = int(input("Enter your choice: "))
    
    if option == 1:
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        admin.login(username, password)
    elif option == 2:
        bus_number = int(input("Enter bus number: "))
        name = input("Enter your name: ")
        phone = input("Enter your phone: ")
        passenger = Passenger(name, phone)
        passenger.book_ticket(bus_number, name, phone)
        
    elif option == 3:
       bus_system.show_buses()
        
    elif option == 4:
        print("Thank you for being with us!!!")
        sleep(2)
        print("Hopefully see you again!!!")
        sleep(2)
        break
    
    else:
        print("Incorrect choice!!!")