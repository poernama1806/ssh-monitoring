from crypt import methods
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

hosts_list = [
    {
        "id": 0,
        "hostname":"test01",
        "attempt": 1,   
    },
    {
        "id": 1,
        "hostname":"test02",
        "attempt": 3,  
    },
]

@app.route('/hosts', methods=['GET', 'POST'])
def hosts():
    if request.method == 'GET':
        if len(hosts_list) > 0:
            return jsonify(hosts_list)
        else:
            'Nothing Found', 404
    
    if request.method == 'POST':
        iD = hosts_list[-1]['id']+1
        new_host = request.form['hostname']
        new_attempt = request.form['attempt']
        
        new_obj = {
            'id': iD,
            'hostname': new_host,
            'attempt': new_attempt
        }
        hosts_list.append(new_obj)
        return jsonify(hosts_list), 201

@app.route('/host/<string:hostname>', methods=['GET', 'POST', 'PUT'])
def single_host(hostname):
    if request.method == 'GET':
        for server in hosts_list:
            if server['hostname'] == hostname:
                return jsonify(server)

    if request.method == 'PUT':
        for server in hosts_list:
            if server['hostname'] == hostname:
                server['hostname'] = request.form['hostname']
                server['attempt'] = request.form['attempt']
                update_host = {
                    'hostname': hostname,
                    'attempt': server['attempt'],
                    'id': server['id']
                }
                return jsonify(update_host)


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)
    
if __name__ == "__main__":
    #app.run(host="0.0.0.0", debug=True)
    #socketio.run(app, debug=True)
    socketio.run(app, host="0.0.0.0", debug=True)
    #app.run(host="0.0.0.0")

# web page
