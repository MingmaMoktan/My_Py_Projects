from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define a Pydantic model for our data
class Item(BaseModel):
    id: int
    name: str
    price: float

# In-memory storage for items
items: List[Item] = []

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI CRUD example!"}

# Create (POST): Add a new item
@app.post("/items", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item

# Read (GET): Get all items
@app.get("/items", response_model=List[Item])
async def read_items():
    return items

# Update (PUT): Update an existing item by id
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    for idx, existing_item in enumerate(items):
        if existing_item.id == item_id:
            items[idx] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# Delete (DELETE): Remove an item by id
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for idx, existing_item in enumerate(items):
        if existing_item.id == item_id:
            del items[idx]
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")