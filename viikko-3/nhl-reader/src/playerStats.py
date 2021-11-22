from playerReader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality):
        players_by_nationality = []

        for player in self.players:
            if player.nationality == str(nationality):
                    players_by_nationality.append(player)
        players_by_nationality.sort(key=lambda x: x.total, reverse = True)
        return players_by_nationality
        
    def __str__(self):
        return f"stats class"