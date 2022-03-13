from socket import socket
from threading import Lock
from flask import Flask, render_template, session
from flask_restful import Api, Resource, reqparse
from flask_socketio import SocketIO, emit


app = Flask(__name__)
socketio = SocketIO(app)
api = Api(app)
thread = None
thread_lock = Lock()

ssh_mon_args = reqparse.RequestParser()
ssh_mon_args.add_argument("hostname", type=str, help="Provide the server hostname", required=True)
ssh_mon_args.add_argument("attempt", type=int, help="Provide ssh attempt", required=True)

ssh_mon={}
 
class SSH_attempt(Resource):
    def put(self,host):
        args=ssh_mon_args.parse_args()
        ssh_mon[host]=args
        return ssh_mon[host], 201

class Host_List(Resource):
    def get(self,host):
        return ssh_mon[host]
    def get(self):
        return ssh_mon
api.add_resource(SSH_attempt, "/host/<string:host>")
api.add_resource(Host_List, "/get-host")

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)
    
if __name__ == "__main__":
    #app.run(debug=True)
    #socketio.run(app, debug=True)
    socketio.run(app, host="0.0.0.0", debug=True)
    #app.run(host="0.0.0.0")

# web page


