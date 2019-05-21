from flask import Flask
from flask import request
from random import randint

app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return "Hello World!"

    if request.method == 'POST':
        name = request.data
        return "Hello World! {}".format(name)


next_id = 0
clients = {}


@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        global next_id
        res = next_id
        clients[res] = (0, 0)
        next_id += 1
        return "{}".format(res)


@app.route('/status')
def status():
    global clients
    return "{}".format(clients)


@app.route('/get_task', methods=['POST'])
def get_task():
    if request.method == 'POST':
        global clients
        client_id = request.data
        task_num = randint(-10, 10)
        # clients[client_id] = (clients[client_id], task_num)
        return "{}".format(task_num)


if __name__ == "__main__":
    app.run()
