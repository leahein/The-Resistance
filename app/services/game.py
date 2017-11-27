from typing import List, FrozenSet, Dict, NamedTuple, Optional
import random

from . import constants

class PlayerInfo(NamedTuple):
    pass

class Player(NamedTuple):
    '''Container representing a player in the game'''

    name: str
    game: 'Game'
    team: str
    is_merlin: bool = False

class Game:

    def __init__(
            self,
            id: int,
            player_names: List[str],
            with_merlin: bool = True
    ) -> None:
        self.id = id
        self.player_names = random.sample(player_names, k=len(player_names))
        self._spies = None # type: Optional[List[Player]]
        self._resistance = None # type: Optional[List[Player]]

    @property
    def n_players(self) -> int:
        return len(self.player_names)

    @property
    def n_spies(self) -> int:
        '''round up number of spies if players not divisible by 0'''
        third = int(self.n_players / 3)
        return int(third + 1) if self.n_players % 3 else third

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
