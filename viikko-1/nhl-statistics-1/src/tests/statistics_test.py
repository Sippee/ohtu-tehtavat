import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
        self.name = "Lemieux"
        self.team_name = "PIT"
        self.randomname = "Kalle"
        
    def test_search_palauttaa_oikean_pelaajan(self):
        self.assertEqual(self.statistics.search(self.name).name, self.name)
        
    def test_team_palauttaa_oikean_listan_pelaajia(self):
        testilista = []
        for player in self.statistics.team(self.team_name):
            testilista.append(str(player.name))
        
        self.assertEqual(testilista, [self.name])
    
    def test_top_score_toimii(self):
        testilista = []
        for player in self.statistics.top_scorers(1):
            testilista.append(player)
        self.assertEqual(testilista[0].goals+testilista[0].assists, 124)
        
    def test_search_jos_ei_loyda(self):
        self.assertEqual(self.statistics.search(self.randomname), None)