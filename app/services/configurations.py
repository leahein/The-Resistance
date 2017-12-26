"""Interface to the google sheet module
"""

from typing import List, Dict, Any

from gspread.client import Client
from .google_sheet import (
    GoogleSpreadsheet,
)

from .containers import google_sheet_data, Playerinfo


def get_google_sheet(
        book_code:str,
        client: Client,
) -> List[Dict[str, Any]]:
    worksheet = GoogleSpreadsheet(
        book_code=book_code,
        client=client,
    ).get_worksheet_data('kepler')

    return worksheet



def extract_data_from_google_sheet(
        book_code: str,
        client: Client,
) -> List[Playerinfo]:

    google_sheet = get_google_sheet(book_code, client)

    data = [
        google_sheet_data(i) for i in google_sheet
    ]
    return data

