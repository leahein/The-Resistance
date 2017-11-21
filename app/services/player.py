# from .game import Game

class Player:

    def __init__(
            self,
            name: str,
            team: str,
            game,
            is_merlin: bool
    ) -> None:
        self.name = name
        self.game = game
        self.merlin = is_merlin
        self.team = None

