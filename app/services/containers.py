"""Containers: to store data from the google sheet in the organised way"""

from typing import NamedTuple

class PlayerInfo(NamedTuple):
    name: str
    phone: int

class Player(NamedTuple):
    '''Container representing a player in the game'''

    Playerinfo: PlayerInfo
    team: str
    is_merlin: bool = False
