import random

class Chapstick: 
    def __init__(self, brand):
        self.brand = brand
        self.size = random.randint(70, 100)
        self.uses = 0
        
    def use_chapstick(self):
        self.uses += 1
        print(self.brand + ' chapstick has been used ' + str(self.uses) + ' times.')
        self.uses_left()
        
    def uses_left(self):
        if self.size - self.uses <= 0:
            print('The chapstick is empty')
        else:
            print('You have ' + str(self.size - self.uses) + ' uses left')
            
            
            
def rate_chapsticks(list_of_chapsticks):
    best = list_of_chapsticks[0]
    
    for chapstick in list_of_chapsticks:
        if chapstick.size > best.size:
            best = chapstick
            
    print('The best chapstick is ' + best.brand + ' with ' + str(best.size) + ' total uses')
    
def use_alot_of_chapstick(chapstick):
    for x in range(0, 20):
        chapstick.use_chapstick()