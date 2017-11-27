'''Helper classes and methods for working with Google sheets API'''

from typing import List, Dict, Any
from typing import Optional  # pylint: disable=unused-import

import gspread  # type: ignore
from gspread.models import Spreadsheet, Worksheet  # type: ignore
from gspread.client import Client  # type: ignore # pylint: disable=unused-import
from oauth2client.service_account import ServiceAccountCredentials # type: ignore
from oauth2client.crypt import Signer  # type: ignore

SCOPES = ('https://spreadsheets.google.com/feeds')

def google_sheet_client(credentials_filename: str) -> Client:
    '''Establish connection to client'''
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
            filename=credentials_filename,
            scopes=list(SCOPES),
        )
    return gspread.authorize(credentials)


class GoogleSpreadsheet:
    '''Helper class for working with google spreadsheets'''

    def __init__(self, book_code: str, client: Client) -> None:
        '''Initialize class constants'''
        self.book_code = book_code
        self.client = client
        self._workbook = None  # type: Optional[Spreadsheet]

    @property
    def workbook(self) -> Spreadsheet:
        '''Open a connection to a particular workbook'''
        if self._workbook is None:
            self._workbook = self.client.open_by_key(self.book_code)
        return self._workbook

    def get_worksheet_by_name(self, sheet_name: str) -> Worksheet:
        '''Get a worksheet by name from a workbook'''
        return self.workbook.worksheet(sheet_name)

    def get_worksheet_data(self, sheet_name: str) -> List[Dict[str, Any]]:
        '''Obtain all data from a google workbook worksheet

        Cleans records to ensure that:
            * blank rows are removed
            * Cells associated with a blank header are removed
            * blank cells are removed
        '''
        try:
            worksheet = self.get_worksheet_by_name(sheet_name)
            worksheet_raw = worksheet.get_all_records(default_blank=None)
        except IndexError:
            worksheet_raw = []

        worksheet_clean = (
            {k: v for k, v in d.items() if k.strip() and v is not None}
            for d in worksheet_raw
        )
        return [row for row in worksheet_clean if row]
