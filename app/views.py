from flask import render_template, request

from app import app
from . import config
from .forms import GameForm
import random

import yaml
import json

from .services.game import (
    Game,
    inform_players,
    get_the_rules,
)
from .config import (
    GS_CLIENT,
    GS_BOOK_CODE,
    SNS_CLIENT,
    GAME_RULES,
)
from .services import constants

from .services.sns import SNS

from .services.configurations import extract_data_from_google_sheet


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
    response_received =request.form.getlist('players')
    with_merlin = request.form.get('merlin')

    google_sheet_data = extract_data_from_google_sheet(
        GS_BOOK_CODE,
        GS_CLIENT,
    )

    sns = SNS(SNS_CLIENT)
    playing_players = list(filter(lambda t: t[1] in response_received, google_sheet_data))
    game = Game(
        playing_players,
        True if with_merlin else False
    )
    inform_players(game, sns)
    starting_person = f'You will start {random.choice(playing_players).name}'
    rules = f'Mission size: {get_the_rules(len(playing_players), GAME_RULES)}'

    return json.dumps((starting_person, rules))
