class Game:
    def __init__(self, title):
        self._title = title
        self._results = []
        self._players = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, 'title'): return
        if isinstance(title, str) and title != "":
            self._title = title
        else:
            raise Exception("Title must be a non-empty string")

    def results(self):
        return self._results

    def players(self):
        return self._players

    def average_score(self, player):
        total = 0
        for result in self.results():
            if result.player == player:
                total += result.score
        return total / len(self.results())

class Player:
    def __init__(self, username):
        self._username = username
        self._results = []
        self._games_played = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        
    def results(self):
        return self._results

    def games_played(self):
        return self._games_played

    def played_game(self, game):
        return self in game.players()

    def num_times_played(self, game):
        gamecount = 0
        for result in self.results():
            if result in game.results():
                gamecount += 1
        return gamecount


class Result:
    all = []

    def __init__(self, player, game, score):
        game._results.append(self)
        player.results().append(self)
        self._score = score
        self.player = player
        self.game = game

        if not player in game._players:
            game._players.append(player)
            player._games_played.append(game)

        Result.all.append(self)
            
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if hasattr(self, 'score'): return
        if isinstance(score, int) and 1 <= score <= 5000:
            self._score = score
        else:
            raise Exception("Score must be an integer between 1 and 5000")