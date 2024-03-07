from flask import Flask, render_template, send_from_directory, request, make_response, session
from flask_sock import Sock
from components.user_database import getUser, createUser, getUserBySessionToken, sendChatMessage, getRooms, getRoom
import json

app = Flask(__name__)
sock = Sock(app)

app.secret_key = "11234132446"

@app.route('/')
def index():
	return render_template('index.html')
	

@app.route('/static/<path:path>')
def send_static(path):
	return send_from_directory('static', path)

@app.route('/login', methods = ['POST'])
def login():
    session["user"] = request.form["username"]    
    user = None
    if not getUser(request.form["username"]):
        user = createUser(request.form["username"])
    else:
        user = getUser(request.form["username"])
    resp = make_response('{"loggedIn" : true}')
    resp.set_cookie("session_token", user['session_token'])
    return resp
    
@app.route('/rooms', methods = ['GET'])
def get_rooms():
    print(getRooms())
    return {"rooms" : getRooms() }

@app.route('/room/<roomname>/', methods = ['GET'])
def get_room(roomname):
    return {"room" : getRoom(roomname)}
    
@app.route("/get_session", methods = ['GET'])
def get_session():
    if request.cookies["session_token"]:
        return {"user" : getUserBySessionToken(request.cookies["session_token"])}
	
    
    
if __name__ == "__main__":
	app.run(debug=True)