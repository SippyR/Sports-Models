import cbbpy.mens_scraper as mens_scraper

class win_loss_model:
    # Predict winner of a game
    def predict_winner(self, team1, team2):
        return None
class point_spread_model:
    def predict_point_spread(self, team1, team2):
        return None

class over_under_model:
    def predict_over_under(self, team1, team2):
        return None

#print(mens_scraper.get_game(401522202, info=False))
games_range = mens_scraper.get_games_range('2024-01-01', '2024-01-02')
print(games_range)