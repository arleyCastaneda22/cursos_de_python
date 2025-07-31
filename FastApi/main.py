from fastapi import FastAPI
app = FastAPI()

app.title = "Aprendiendo FastApi"


@app.get("/")
async def hello():
    return {"message": "Hello word"}


