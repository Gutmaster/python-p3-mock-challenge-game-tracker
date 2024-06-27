class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, 'title'):
            raise Exception("Title is immutable")
        if title == "":
            raise Exception("Title must be a non-empty string")
        if isinstance(title, str):
            self._title = title

            
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
    all = []
    def __init__(self, username):
        self.username=(username)
        self._results = []
        self._games_played = []
        Player.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise ValueError("Username must be a string of 2 to 16 characters")
        
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

    @classmethod
    def highest_scored(cls, game):
        highest = 0
        high_player = None
        for player in cls.all:
            if player.played_game(game):
                if game.average_score(player) > highest:
                    highest = game.average_score(player)
                    high_player = player
        return high_player

class Result:
    all = []

    def __init__(self, player, game, score):
        game.results().append(self)
        player.results().append(self)
        self.score = score
        self.player = player
        self.game = game

        if not player in game.players():
            game.players().append(player)
            player.games_played().append(game)

        Result.all.append(self)
            
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if hasattr(self, '_score'):
            raise Exception("Score is immutable")
        if not isinstance(score, int):
            raise Exception("Score must be an integer")
        if 1 <= score <= 5000:
            self._score = score