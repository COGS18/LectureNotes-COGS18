def sort_alpha(roster_list_of_instances):
    alphabetize = []
    for item in roster_list_of_instances:
        alphabetize.append((item)['name'])
        alphabetize.sort(reverse = False)
    return alphabetize
def num_of_duckies(roster):
    counter = 0
    for duck in roster:
        counter += 1
    return counter
class ducklings_race():
    
    type_of_animal = 'waddles'
    
    def __init__(self):
        self.roster = []
        
    def add_duckling(self, name, amount_of_steps, comments):
        self.roster.append({'name' : name, 'amount of steps' : amount_of_steps, 'comments' : comments })
        
    def winner(self):
        output = []
        for duckies in self.roster:
            #I want to sort the amount of steps numerically
            if len(output) > 0:
                if duckies['amount of steps'] <= (output[0])['amount of steps']:
                    output.append(duckies)
                elif duckies['amount of steps'] > (output[0])['amount of steps']:
                    output.insert(0, duckies)
            else:
                output.append(duckies)
                
                
        self.winner = (output[0])['name']
            
        print(self.winner + ' is the winner')