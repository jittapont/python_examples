from fastapi import FastAPI

app = FastAPI()
# declare the HTTP method you want to use with the path
@app.get("/")
# define your function
# Note: if you are going to have an await you'll need to define an async function
async def root():
    return {"message": "Hello World"}
