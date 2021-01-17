from flask import Flask, request
from flask_cors import CORS
from game import RingGame

app = Flask(__name__)
CORS(app, support_credentials=True)

ring_game = RingGame()

@app.route('/newgame', methods = ['POST'])
def new_game():
    post_data = request.get_json()
    ring_game.reset()
    ring_game.new_game(post_data['player_names'], post_data['stakes'], post_data['ante'])
    return 'game initialized'

@app.route('/newround', methods = ['GET'])
def new_round():
    ring_game.new_round()
    return ring_game.get_game_state()

@app.route('/endround', methods = ['POST'])
def end_round():
    post_data = request.get_json()
    ring_game.end_round(post_data['name'])
    return ring_game.get_game_state()

@app.route('/getgamestate', methods = ['GET'])
def get_game_state():
    # print()
    return ring_game.get_game_state()

if __name__ == "__main__":
    app.run(debug=True)