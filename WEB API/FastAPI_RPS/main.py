import requests
from fastapi import FastAPI
import random

app = FastAPI()

sessions = {}
@app.get('/api/start_session')
async def start_session(username: str):
    session_id=random.randint(3000,9000)
    return {
        "status": 1,
        "message": f"session {session_id} was created successfully.",
        "session_id": session_id,
        "username": username
}