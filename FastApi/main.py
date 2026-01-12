from fastapi import FastAPI

import requests
from httpx import request
import uvicorn


from FastApi.schemas import Item, UserProfile






# 1. Create the App instance
app = FastAPI()

# 2. Define a Path Operation (Route)
@app.get("/")
async def root():
    return {"message": "Hello World, welcome to FastAPI!"}

api_url = "https://jsonplaceholder.typicode.com/posts"
@app.get("/posts")
async def api_urls():

    responce=requests.get(api_url)
    data = responce.json()
    return {"data":data}


@app.post("/add")
async def add(a:int, b:int):
    result = a+b 
    return{"result":result}




print("Server started! Go to http://127.0.0.1:8000/docs to see the Swagger UI.")

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # FastAPI automatically converts item_id to an integer because of the type hint!
    return {"item_id": item_id, "type": type(item_id).__name}

print("Route /items/{item_id} added.")


@app.get("/users/")
async def read_users(skip: int = 0, limit: int = 10):
    return {
        "skip": skip,
        "limit": limit,
        "data": ["user1", "user2", "user3"][skip : skip + limit]
    }

print("Route /users/ added.")



@app.post("/items/")
async def create_item(item: Item):
    # item is now a Pydantic object
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

print("POST Route /items/ added.")


# --- STEP 3: Use the Model in a Route ---
@app.post("/create-user/")
async def create_user(user: UserProfile):
    # At this point, FastAPI has already validated the data!
   
    # We can access data like a standard Python object
    user_message = f"User {user.username} created with email {user.email}"
   
    if user.age < 18:
        return {"status": "error", "message": "User is too young"}
   
    # We can also convert the model back to a dictionary
    return {
        "status": "success",
        "message": user_message,
        "received_data": user.dict()
    }

print("User route created. Try sending data to it!")

# 3. Run the Application
if __name__ == "__main__":
    uvicorn.run(app)

from fastapi import HTTPException

@app.get("/items-check/{item_id}", status_code=200)
async def read_item_check(item_id: int):
    if item_id == 0:
        # Return a 404 Error
        raise HTTPException(status_code=404, detail="Item not found (ID cannot be 0)")
    return {"item_id": item_id}

print("Route /items-check/{item_id} added.")


from fastapi import Depends
from typing import Optional


# A simple dependency function
async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


# Using the dependency in a route
@app.get("/products/")
async def read_products(commons: dict = Depends(common_parameters)):
    return {"message": "Products retrieved", "params": commons}



@app.get("/orders/")
async def read_orders(commons: dict = Depends(common_parameters)):
    return {"message": "Orders retrieved", "params": commons}

print("Routes using Dependency Injection added.")