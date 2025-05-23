from fastapi import FastAPI, Form

app = FastAPI()

# class Item:
#     def __init__(self, id: int, name: str):
#         self.id = id
#         self.name = name
#     def __repr__(self):
#         return f"Item(id={self.id}, name='{self.name}')"

# items = []

# @app.post("/items/")
# def create_item(item: Item):
#     items.append(item)
#     return item

@app.get("/")
def root():
    data = {
        "message": "Hello from the FastAPI server"
    }
    return data

@app.post("/items/")
async def create_item(
    id: int = Form(...),
    name: str = Form(...)
):
    item = {
        "id": id,
        "name": name
    }
    return item