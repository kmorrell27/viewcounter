from flask import Flask, render_template
from flask_sockets import Sockets
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from random import randint

app = Flask(__name__)
sockets = Sockets(app)

@sockets.route('/counter')
def echo_socket(ws):
    # Serve up fake visitors
    visitorCounter = randint(5000, 10000)
    while True:
        message = ws.receive()
        ws.send(str(visitorCounter))

        # Assume that the site is gaining viewers as we monitor it
        visitorCounter += randint(1, 10)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Set up a server for our WebSockets
    server = WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
    print(' * Running on http://127.0.0.1:5000/')
    server.serve_forever()
