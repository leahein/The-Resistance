'''Main logic for the resistance game role assignment'''

from typing import List, Optional # pylint: disable=unused-import
import random

from . import constants
from .containers import PlayerInfo, Player
from .sns import SNS

class Game:

    def __init__(
            self,
            players: List[PlayerInfo],
            with_merlin: bool = False
    ) -> None:
        self.players_info = random.sample(players, k=len(players))
        self._spies = None # type: Optional[List[Player]]
        self._resistance = None # type: Optional[List[Player]]
        self.with_merlin = with_merlin

    @property
    def n_players(self) -> int:
        return len(self.players_info)

    @property
    def n_spies(self) -> int:
        '''round up number of spies if players not divisible by 0'''
        third = int(self.n_players / 3)
        return int(third + 1) if self.n_players % 3 else third

    @property
    def resistance(self) -> List[Player]:
        if self._resistance is None:
            resistance = [
                Player(
                    Playerinfo=player_info,
                    team=constants.RESISTANCE,
                    is_merlin=False
                    )
                for player_info in self.players_info[self.n_spies:-1]
            ]
            merlin = [Player(
                Playerinfo=self.players_info[-1],
                team=constants.RESISTANCE,
                is_merlin=self.with_merlin
            )]
            self._resistance = resistance + merlin
        return self._resistance

    @property
    def spies(self) -> List[Player]:
        if self._spies is None:
            self._spies = [
                Player(
                    Playerinfo=name,
                    team=constants.SPIES,
                    is_merlin=False
                )
                for name in self.players_info[0: self.n_spies]
            ]
        return self._spies

def inform_players(game: Game, sns: SNS)-> None:
    """sends sms and informs the players about their team"""

    spies = game.spies
    resistance = game.resistance

    spy_names = ', '.join(player.Playerinfo.name for player in spies)

    for player in resistance:
        message = (
            constants.MERLIN_MESSAGE + (spy_names) if player.is_merlin else
            constants.RESISTANCE_MESSAGE
        )
        sns.send(
            phone=player.Playerinfo.phone,
            message=message
        )

    for spy in spies:
        sns.send(
            phone=spy.Playerinfo.phone,
            message=constants.SPY_MESSAGE + spy_names
        )
