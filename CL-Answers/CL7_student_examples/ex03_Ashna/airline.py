class PlaneTicket():
    
    def __init__(self, owner, airline, type_class, seat, destination):
        self.owner = owner
        self.airline = airline + ' airlines'
        self.type_class = type_class + ' class'
        self.seat = seat
        self.destination = destination
        
    def boarding_pass(self):
        return self.owner + ' is flying on ' + self.airline + '. The seat number is ' + self.seat + ' in ' + self.type_class + '.'
         
    def arrival(self):
        return self.owner + ' is flying to ' + self.destination + '.'
        
        
def seat_type(seat_row):
    for x in seat_row:
        if x >= 1 and x <= 5:
            print ('Row ' + str(x) + ' is in first class.')
        elif x > 5 and x <= 9:
            print ('Row ' + str(x) + ' is in business class.')
        else:
            print ('Row ' + str(x) + ' is in economy class.')
            

def group_tickets(group):
    for x in group:
        print(x.boarding_pass())


def group_destination(group):
    for x in group:
        print(x.arrival())
