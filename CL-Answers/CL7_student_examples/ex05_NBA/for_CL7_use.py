class NbaPlayer():
    
    def __init__(self):
        self.players = []
    
    def add_player(self, name, team, age):
                dictionary = {'name': name, 
                              'team': team,
                              'age': age}
                self.players.append(dictionary)
        
    def compare_age(self, attribute):
        youngest = self.players[0]
        for player in self.players:
            if player[attribute] < youngest[attribute]:
                youngest = player
        return print(youngest)
        

nba = NbaPlayer()
nba.add_player('Leborn James', 'Los Angeles Lakers', 36)
nba.add_player('Chris Paul', 'Phoenix Suns', 36)
nba.add_player('Kevin Durant', 'Brooklyn Nets', 32)
nba.add_player('Stephen Curry', 'Golden State Warriors', 33)
nba.compare_age('age')