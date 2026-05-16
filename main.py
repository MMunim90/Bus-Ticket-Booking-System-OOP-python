from time import sleep
import random
class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0
        
    def available_seats(self, number):
        for i in bus_system.buses_list:
            if i.number == number:
                print(f"\n\t\tBus no.: {i.number} \t\t Route: {i.route}\n")
                    
        line = self.total_seats // 4
        print(f"\n\t\t ----- Available seats: {self.total_seats - self.booked_seats} -----\n")
        print("/---------------------------------------------------------------\\")
        print("|-----\t\t\t\t\t\t\t--------|")
        print(" Door \t\t\t\t\t\t\t Driver |")
        print("|--------------------------\t\t------------------------|")
        for x in range(line):
            for y in range(4):
                if bus_system.seats[number][x][y] == 'free':
                    print(f'\t{chr(x+65)}{y+1}', end = '\t')
                else:
                    print("\tX", end = '\t')
            print("\n")
        print("|---------------------------------------------------------------|")
    
    def book_seat(self, number, name, phone, booking_seats):
        flag = 0
        self.booked_tickets = []
        if number not in bus_system.seats:
            print("Wrong Bus ID")
        else:
            for x in booking_seats:
                r = ord(x[0]) - 65
                c = ord(x[1]) - 49
                
                if r >= self.total_seats // 4 or c >= 4 or r < 0 or c < 0:
                    print("Seat doesn't exists.")
                    
                elif bus_system.seats[number][r][c] != 'free':
                    print(f"{x} is already booked.")
                    
                else:
                    bus_system.seats[number][r][c] = 'X'
                    self.booked_tickets.append(x)
                    flag = 1
                    
            if flag == 1:
                print("\n\t ##### Ticket Booked Successfully #####")
                print("\n-----------------------------------------------------------------\n")
                print(f"Name: {name}")
                print(f"Phone: {phone}")
                print(f"Bus no.: {number}")
                print(f"Route: {self.route}")
                print("Tickets: ", end="")
                for i in self.booked_tickets:
                    print(i, end=", ")
                print(f"\nPrice: {500*len(self.booked_tickets)} Taka")
                self.booked_seats += len(self.booked_tickets)
                print("\n-----------------------------------------------------------------\n")
    
class Passenger:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        
    def book_ticket(self, bus_number, name, phone):
        if bus_number not in bus_system.seats:
            print("Wrong Bus ID")
        else:
            for bus in bus_system.buses_list:
                if bus.number == bus_number:
                    bus.available_seats(bus_number)
            
            while True:
                print("\n")
                print("1. Book Ticket. ")
                print("2. Back. ")
                
                opt = int(input("Choose your option: "))
                
                if opt == 1:
                    tickets = int(input("\nEnter number of tickets: "))
                    booking_seats = []
                    for i in range(tickets):
                        booking_seats.append(input("Enter your seat no: "))
                        
                    bus.book_seat(bus_number, name, phone, booking_seats)
                
                elif opt == 2:
                    print("Thank You!!!")
                    sleep(2)
                    break
                
                else:
                    print("Incorrect choice!!!")
        
class BusSystem:
    def __init__(self):
        self.buses_list = []
        self.passengers_list = []
        self.seats = {}
        
    def add_bus(self, bus):
        self.buses_list.append(bus)
        self.seat_list = []
        line = bus.total_seats // 4
        for i in range(line):
            row = []
            for j in range(4):
                row.append('free')
            self.seat_list.append(row)
        self.seats[bus.number] = self.seat_list
        print(f"Bus added Successfully!!! Bus no. {bus.number}")
    
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
                print("Processing...")
                sleep(random.randint(1, 2))
                self.admin_menu()
    
    def admin_menu(self):
        while True:
            print("\n\t --- Welcome Admin --- \n")
            print("1. Add Bus. ")
            print("2. View All Buses. ")
            print("3. Logout. ")
            
            opt = int(input("Enter your choice: "))
            
            if opt == 1:
                number = int(input("Enter bus number: "))
                route = input("Enter route: ")
                print("( Keep the seat count between 40 to 50 for better view! )")
                total_seats = int(input("Enter seats: "))
                bus = Bus(number, route, total_seats)
                self.bus_system.add_bus(bus)
                
            elif opt == 2:
                self.bus_system.show_buses()
                
            elif opt == 3:
                print("Please wait...")
                sleep(random.randint(1, 2))
                break
            
            else:
                print("Incorrect choice!!!")
    
bus_system = BusSystem()
admin = Admin(bus_system)

while True:
    print("\n\t --------- Welcome ---------\n")
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