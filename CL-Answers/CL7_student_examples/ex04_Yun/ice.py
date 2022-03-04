class Icecream():
    def __init__(self, size = 'large', takeaway = 'Yes'):
        self.size = size
        self.takeaway = takeaway
  
        
    def customerize (self):
        return self.size+takeaway
        
def my_fav(Icecream):
    if Icecream.takeaway == 'Yes':
        out = 'You may get it soon'
    else:
        out = 'we do not offer dine in'
    return out

def my_size(Icecream):
    if Icecream.size == 'large':
        my_order = 'it costs 5$'
    else:
        my_order='It costs $3'
    return my_order