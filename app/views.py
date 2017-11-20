from app import app

@app.route('/')
@app.route('/game/new')
def new():
    return "Hello, World!"
