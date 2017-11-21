from typing import List, FrozenSet, Dict, Optional
from random import shuffle
from . import constants
from .player import Player

def _players_shuffled(player_names: str) -> List[str]:
    split_names = player_names.split(',')
    shuffle(split_names)
    return split_names


class Game:

    all = {} # type: Dict[int, 'Game']

    def __init__(
            self,
            id: int,
            player_names: str,
            with_merlin: bool = True) -> None:
        self.id = id
        self.player_names = _players_shuffled(player_names)
        self._spies = None # type: Optional[List[Player]]
        self._resistance = None # type: Optional[List[Player]]
        self.all[self.id] = self

    @property
    def n_players(self) -> int:
        return len(self.player_names)

    @property
    def n_spies(self) -> int:
        return int(self.n_players / 3)

    def team_names(self) -> FrozenSet[str]:
        return constants.TEAM_NAMES

    @property
    def players(self) -> List[Player]:
        return [*self.spies, *self.resistance]

    @property
    def resistance(self) -> List[Player]:
        if self._resistance is None:
            resistance = [
                Player(name=name, game=self,team=constants.RESISTANCE, is_merlin=False)
                for name in self.player_names[self.n_spies:-2]
            ]
            merlin = [Player(
                name=self.player_names[-1], 
                game=self, 
                team=constants.RESISTANCE, 
                is_merlin=True
            )]
            self._resistance = resistance + merlin
        return self._resistance

    @property
    def spies(self) -> List[Player]:
        if self._spies is None:
            self._spies = [
                Player(name=name, game=self, team=constants.SPIES, is_merlin=False)
                for name in self.player_names[0: self.n_spies]
            ]
        return self._spies


    def destroy(self) -> None:
        del self.all[self.id]
