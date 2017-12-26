"""Containers: to store data from the google sheet in the organised way
"""

from collections import namedtuple, OrderedDict
from typing import Dict, Any

GoogleSheetHeader = OrderedDict([
    ('name', 'Name'),
    ('phone', 'Phone'),
])

Playerinfo = namedtuple('Playerinfo', 'name, phone')


def google_sheet_data(
        fields: Dict[str, Any]
) -> Playerinfo:
    """Retrieves data from google sheet
    """
    return Playerinfo(
        name=fields[GoogleSheetHeader['name']],
        phone=str(fields[GoogleSheetHeader['phone']]),
    )
