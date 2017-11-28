from flask_wtf import Form
from wtforms import SelectMultipleField, BooleanField
from wtforms.validators import DataRequired

class GameForm(Form):
    players = SelectMultipleField(
        'Players', 
        choices=[], 
        validators=[DataRequired()]
    )
    with_merlin = BooleanField('merlin?', default=False)
