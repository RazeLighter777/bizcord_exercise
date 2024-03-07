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
    data = request.form
    session["user"] = data["username"]
    return {}
    
@app.route("/get_session", methods = ['GET'])
def get_session():
    if session["user"]:
        return {"user" : session["user"]}
    return {}
    
    
if __name__ == "__main__":
	app.run(debug=True)