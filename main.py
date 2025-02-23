from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message":"Hello World"}


@app.get("/profile")
async def profile():
    return {"name":"Jose alves sobrinho neto"}


