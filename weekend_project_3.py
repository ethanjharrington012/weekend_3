class Parking_Garage():
    
    def __init__(self,parkingSpaces, name):
        self.tickets_available = parkingSpaces
        self.parkingSpaces = parkingSpaces
        self.currentTicket = {}
        self.allowed_parking_time = None
        self.name = name
# - takeTicket
# - This should decrease the amount of tickets available by 1
    def takeTicket(self):
        tickets_needed = int(input("How many tickets do you need?: "))
        if tickets_needed > self.tickets_available:
            print("Hey McFly, that's too many tickets! Try less. ")
        else:            
            self.tickets_available -= tickets_needed
            
    def returnTicket(self):
        tickets_returning = int(input("How many vehicles are leaving?: "))
        if tickets_returning > self.tickets_available:
            print(f"Well, that doesn't make sense.  Are you sure that you're returning {tickets_returning}. Try again. ")
        else:            
            self.tickets_available += tickets_returning
            self.checkoutTicket()


    def showTicketavailable(self): 
            print(f'{self.tickets_available} tickets available.') 
      
    def checkoutTicket(self):
        print(f" Thanks for parking at {self.name}.")
            
    def run(self):   
    
        while True:
            response = input("What are you doing? Entering/Exiting/Show (tickets): ").lower()

            if response == 'entering':
                self.takeTicket()

            elif response == 'exiting':
                self.returnTicket()
            elif response == 'show':
                self.showTicketavailable()
    
            elif response == 'checkout':
                self.checkoutTicket()
    
                break

            else:
                print("Invalid entry. Please try again, doofus.")

# Other Ideas:
"""

- show tickets available
- possibly add time somehow
- input variables to enter drivers info: name, vehicle, etc. - stored in dictionary
- 

"""
            
            

            
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking


# - Display an input that waits for an amount from the user and store it in a variable

# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)


ethans_Garage = Parking_Garage(100, "Ethans ass garage")
            
ethans_Garage.run()