from flask import Flask

app = Flask(__name__) # pylint: disable=invalid-name
app.config.from_object('config')

from app import views # pylint: disable=wrong-import-position
