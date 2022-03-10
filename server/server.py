from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

ssh_mon_args = reqparse.RequestParser()
ssh_mon_args.add_argument("hostname", type=str, help="Provide the server hostname", required=True)
ssh_mon_args.add_argument("attempt", type=int, help="Provide ssh attempt", required=True)

ssh_mon={}
 
class SSHMon(Resource):
    def get(self,host):
        return ssh_mon[host]

    def put(self,host):
        args=ssh_mon_args.parse_args()
        ssh_mon[host]=args
        return ssh_mon[host], 201

api.add_resource(SSHMon, "/<string:host>")

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0")