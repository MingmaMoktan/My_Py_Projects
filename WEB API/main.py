from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/page",response_class=HTMLResponse)
async def page():
    html = '''
    <html>
        <head>
            <title>My Page</title>
        </head>
        <body>
            <h1>My Page</h1>
            <form action="/signup" method="post">
                <input type="text" name="email" placeholder="Email" required>
                <input type="text" name="firstname" placeholder="First Name" required>
                <button type="submit">Submit</button>
            </form>
        </body>
    </html>
    '''
    return HTMLResponse(content=html)

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
    
# /cart/add
@app.get("/cart/add")
async def cartAdd(itemName, amount):
    if not amount.isnumeric(): return {'error': 'Amount should be numeric.'}
    amount = int(amount)
    if amount < 0: return {'error': 'Amount should be more than 0.'}
    
    # We could add the item to some state, database...
    
    return {
        "message": f"Added {amount} of item {itemName} into cart.",
        "itemName": itemName,
        "amount": amount
    }

@app.get("/cart/remove")
async def cartRemove(itemName, amount=1):
    amount = int(amount)
    return {
        "message": f"{amount} item {itemName} has been removed.",
        "itemName": itemName,
        "amount": amount
    }

user = {}

@app.post("/signup")
async def signup(email: str = Form(), firstname: str = Form()):

    return {
        "message": "user was added",
        "firstname": firstname,
        "email": email
    }