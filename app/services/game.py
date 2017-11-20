from typing import List, FrozenSet
import random
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
        self.seed = random.random()
        self._spies = None # type: Optional[List[Player]]
        self._resistance = None # type: Optional[List[Player]]
        self.all[self.id] = self

    @property
    def n_players(self):
        return len(self.players)

    @property
    def n_spies(self) -> int:
        return int(self.n_players / 3)

    def _players_shuffled(self):
        return shuffle(self.player_names)

    def team_names(self) -> FrozenSet[str]:
        return constants.TEAM_NAMES

    @property
    def players(player_names: List[str]) -> List[Player]:
        if self._players is None:
            players =
            spies = [Player(name=name, game=self, team=constants.SPIES)
                players[0: self.n_spies]
            resistance = players[self.n_spies: -1]
            self.players = [
                Player(name=name, game=self, team=)
                for name in
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
