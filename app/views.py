from flask import render_template

from app import app
from .services.google_sheet import GoogleSpreadsheet
from . import config
from .forms import GameForm

import pdb

@app.route('/')
@app.route('/game/new')
def new():
    team_data = GoogleSpreadsheet(
        book_code=config.GS_BOOK_CODE,
        client=config.GS_CLIENT
    ).get_worksheet_data('kepler')
    form = GameForm()
    form.players.choices = [
        (player['Phone'], player['Name'])
        for player in team_data
    ]
    return render_template('game/new.html', form=form)

@app.route('/game', methods=['POST'])
def create():
    form = GameForm()
    if form.validate_on_submit():
        pdb.set_trace()
