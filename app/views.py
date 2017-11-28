from flask import render_template

from app import app
from . import config
from .forms import GameForm

from .services.google_sheet import GoogleSpreadsheet
from .services.game import Game
from .services import constants
from .services.sns import SNS

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
        game = Game(
            id=,
            player_names=form.players,
            with_merlin=form.with_merlin,
        )
        sns = SNS(config.SNS_CLIENT)
        for player in game.resistance:
            sns.send(
                phone=player.phone,
                message=(constants.MERLIN_MESSAGE
                         if player.is_merlin else
                         constants.RESISTANCE_MESSAGE)
        for player in game.spies:
            sns.send(
                phone=player.phone,
                message=constants.SPY_MESSAGE
            )
