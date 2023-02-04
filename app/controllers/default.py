from app import app

@app.route('/eng')
def indexPT():
    return "HELLO WORLD"


@app.route('/por')
def index():
    return "Olá mundo"