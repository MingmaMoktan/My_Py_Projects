import requests
from fastapi import FastAPI

app = FastAPI()

sessions = {}
@app.get('/api/start_session')
async def start_session():
    session_id = 