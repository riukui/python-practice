class Player:
    
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team
    
    def introduce(self):
        print(f"Hello! I'm {self.name} and I play for {self.team}")


class Team:
    
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []
    
    def show_players(self):
        for player in self.players:
            player.introduce()
    
    def total_xp(self):
        return sum(self.XPs)
    
    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)
    
    def drop_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player)
        print(f"{name} has been left from {self.team_name}")
        
    def total_xp(self):
        total_xp = 0
        for player in self.players:
            total_xp += player.xp
        print(f"We team's total XP is {total_xp}")
        print("---------")


team_x = Team("Team X")
team_x.add_player("Nico")
team_x.add_player("A")
team_x.add_player("C")

team_blue = Team("Team Blue")
team_blue.add_player("Lynn")
team_blue.add_player("B")
team_blue.add_player("D")

team_x.show_players()
team_x.total_xp()

team_blue.show_players()
team_blue.total_xp()

team_x.drop_player("A")
team_x.total_xp()

team_blue.drop_player("Lynn")
team_blue.total_xp()


"""
nico = Player(
    name = "Nico",
    team = "Team X"
)

lynn = Player(
    name = "Lynn",
    team = "Team Blue"
)
"""