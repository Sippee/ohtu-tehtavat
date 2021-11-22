class Player:
    def __init__(self, name, nationality, goals, assists):
        self.name = name
        self.nationality = nationality
        self.goals = goals
        self.assists = assists
        self.total = goals + assists
    
    def __str__(self):
        return f"{self.name:20} {self.nationality} {self.goals} + {self.assists} = {self.total}"
