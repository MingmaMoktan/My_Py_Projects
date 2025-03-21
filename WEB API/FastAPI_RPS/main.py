import requests
from fastapi import FastAPI

app = FastAPI()

@app.get('/api/start_session')
async def 