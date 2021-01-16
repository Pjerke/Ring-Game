from flask import Flask, request
from flask_cors import CORS

game = 5
class MyServer:
    def __init__(self):
        self.globalData = "hello"

app = Flask(__name__)
CORS(app, support_credentials=True)

my_server = MyServer()

@app.route('/newgame', methods = ['GET'])
def new_game():
    # post_data = request.get_json()
    # post_data_keys = post_data.keys()
    # print(post_data.keys())
    print(my_server.globalData)
    my_server.globalData = 'hoi'
    return '2'

@app.route('/test', methods = ['GET'])
def test():
    print(my_server.globalData)
    return '3'

if __name__ == "__main__":
    app.run()