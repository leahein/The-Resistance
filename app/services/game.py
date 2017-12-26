from typing import List, FrozenSet, Dict, NamedTuple, Optional
import random
from collections import namedtuple

import yaml

from . import constants
from .containers import Playerinfo

class PlayerInfo(NamedTuple):
    pass

class Player(NamedTuple):
    '''Container representing a player in the game'''

    Playerinfo: NamedTuple
    game: 'Game'
    team: str
    is_merlin: bool = False

class Game:

    def __init__(
            self,
            players: List[Playerinfo],
            with_merlin: bool = False
    ) -> None:
        self.player_info = random.sample(players, k=len(players))
        self._spies = None # type: Optional[List[Player]]
        self._resistance = None # type: Optional[List[Player]]
        self.with_merlin = with_merlin

    @property
    def n_players(self) -> int:
        return len(self.player_info)

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
                Player(
                    Playerinfo=name,
                    game=self,
                    team=constants.RESISTANCE,
                    is_merlin=False
                    )
                for name in self.player_info[self.n_spies:-1]
            ]
            merlin = [Player(
                Playerinfo=self.player_info[-1],
                game=self,
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
                    game=self,
                    team=constants.SPIES,
                    is_merlin=False
                )
                for name in self.player_info[0: self.n_spies]
            ]
        return self._spies

def inform_players(game: Game, sns)-> None:
    """sends sms and informs the players about their team
    """

    spies = game.spies
    resistance = game.resistance

    spy_names = ', '.join(player.Playerinfo.name for player in spies)

    for player in resistance:
        message = constants.MERLIN_MESSAGE + (spy_names)\
            if player.is_merlin else constants.RESISTANCE_MESSAGE
        sns.send(
            phone=player.Playerinfo.phone,
            message=message
        )

    for spy in spies:
        sns.send(
            phone=spy.Playerinfo.phone,
            message=constants.SPY_MESSAGE + spy_names
        )


def get_the_rules(
        number_of_players: int,
        game_rules_book: str
) -> str:
    """Gets the rules as in the number of players needed to play in every
    round based on the number of players playing

    :param playing_players the number of players playing
    """

    with open (game_rules_book, 'r') as file_obj:
        rules = yaml.load(file_obj)

        if number_of_players > 10:
            return rules[10]

        return rules[number_of_players]
