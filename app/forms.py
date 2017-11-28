from flask_wtf import Form
from wtforms import SelectMultipleField
from wtforms.validators import DataRequired

class PlayerForm(Form):
    players = SelectMultipleField('Players', choices=[])
