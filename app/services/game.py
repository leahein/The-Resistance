from typing import List, FrozenSet
from random import shuffle
from . import constants
from .player import Player

class Game:

    all = {}

    def __init__(
            self,
            id: int,
            player_names: List[str],
            with_merlin: bool = True) -> None:
        self.id = id
        self.player_names = player_names.split(',')
        self.n_players = len(player_names)
        self._players = None # type: Optional[List[Player]]
        self.all[self.id] = self

    def teams(self):
        spy_team_size = int(len(player_names) / 3)


    def team_names(self) -> FrozenSet[str]:
        return constants.TEAM_NAMES

    @property
    def players(player_names: List[str]) ->
        if self._players is None:
            players = players
            self.players = [
                Player(name=name, game=self)
                for name in shuffle(self.player_names)
            ]
        return self.players

    @property
    def resistance(self) -> List[Player]:
        return [
            player for player in self.players
            if player.team == constants.RESISTANCE
        ]

    @property
    def spies(self) -> List[Player]:
        return [
            player for player in self.players
            if player.team == constants.SPIES
        ]


    def destroy(self) -> None:
        del self.all[self.id]
