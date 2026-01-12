from httpx import request
import uvicorn
from fastapi import FastAPI
import requests





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

# 3. Run the Application
if __name__ == "__main__":
    uvicorn.run(app)


print("Server started! Go to http://127.0.0.1:8000/docs to see the Swagger UI.")