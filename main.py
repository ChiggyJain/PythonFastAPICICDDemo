
from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Testing1"}


@app.get("/add")
def add(a: int, b: int):
    return {"Sum of two numbers:": a + b}
