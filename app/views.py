import random
import json
from flask import render_template, request


from app import app
from .forms import GameForm
from .config import (
    GS_CLIENT,
    GS_BOOK_CODE,
    SNS_CLIENT,
    GAME_RULES,
)

from .services import constants
from .services.google_sheet import GoogleSpreadsheet
from .services.game import Game, inform_players
from .services.containers import PlayerInfo
from .services.sns import SNS

@app.route('/')
@app.route('/game/new')
def new():
    team_data = GoogleSpreadsheet(
        book_code=GS_BOOK_CODE,
        client=GS_CLIENT
    ).get_worksheet_data('kepler')
    form = GameForm()
    form.players.choices = [
        (player[constants.PHONE], player[constants.NAME])
        for player in team_data
    ]
    return render_template('game/new.html', form=form)


@app.route('/game', methods=['POST'])
def create():
    players_received = request.form.getlist('players')
    with_merlin = request.form.get('merlin')

    team_data = GoogleSpreadsheet(
        book_code=GS_BOOK_CODE,
        client=GS_CLIENT
    ).get_worksheet_data('kepler')
    players_info = [
        PlayerInfo(
            name=player[constants.NAME],
            phone=player[constants.PHONE]
        ) for player in team_data
    ]
    playing_players = [
        player for player in players_info
        if str(player.phone) in players_received
    ]
    game = Game(
        players=playing_players,
        with_merlin=True if with_merlin else False
    )
    inform_players(
        game=game,
        sns=SNS(SNS_CLIENT)
    )

    starting_person = random.choice(playing_players).name
    mission_rules = (
        GAME_RULES[10] if game.n_players > 10 else
        GAME_RULES[game.n_players]
    )
    return json.dumps(
        {
            'Staring at': starting_person,
            'Mission size per round': mission_rules
        }
    )
