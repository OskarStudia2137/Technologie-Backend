from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/info")
def get_info():
    return {
        "app_name": "My First FastAPI",
        "version": "1.0.0",
        "author": "Oskar s7826"
    }