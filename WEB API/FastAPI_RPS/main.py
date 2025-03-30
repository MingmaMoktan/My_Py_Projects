import requests
from fastapi import FastAPI
import random

app = FastAPI()

sessions = {} # This is the main dictionary where we will be storing our data.
@app.get('/api/start_session')
async def start_session():
    session_id = str(random.randint(3000,9000))
    sessions[session_id]={"players": {}}
    return {
        "status": 1,
        "message": f"session {session_id} was created successfully.",
        "session_id": session_id,
        }


@app.get('/api/join_session')
async def join_session(session_id:str, username:str):
    if session_id not in sessions:
        return "Session ID doesn't exist. Try Again."
    session = sessions[session_id] # This is the element of the sessions where there is another dictionary that stores the list of users.
    if len(session["players"])>=2:# This condition makes sure that there are only two players. 
        return "You cannot join the session is already full."
    
    if username in session["players"]:
        return {
            'status': 0,
            'message': "The username already exist."
        }
        
    result = random.choice(['rock','paper','scissor']) # This creates the game for the user.
    session['players'][username]=result # This stores the result for the player.
    return {
        'status': 1,
        'message': f"{username} joined the session {session_id}",
        'session_id': session_id,
        'usernme': username
    }
    
    
app.get('/api/session_info')
async def session_info(session_id: str):
    if 