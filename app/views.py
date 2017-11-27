from flask import render_template

from app import app
from services.google_sheet import GoogleSpreadsheet
import config

@app.route('/')
@app.route('/game/new')
def new():
    team_data = GoogleSpreadsheet(
        book_code=config.GS_BOOK_CODE,
        client=config.GS_CLIENT
    ).get_worksheet_data('kepler')
    render_template(
        'game/new.html',
        players=[player['Name'] for player in team_data]
    )
