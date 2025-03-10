from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Oh, Hello. I am your friendly neighbourhood API!"
    }
    
@app.get("/test")
async def test():
    return {
        'test': 'Here is the test function.'
    }