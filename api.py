# main.py

from fastapi import FastAPI
from workflow import workflow

app = FastAPI()

@app.get("/{url}")
async def root(url:str):
    try:
        print("received new request: {}".format(url))
        result = workflow()
        print("return request: {}".format(url))
        return {"{}\n{}".format(url, result)}
    except Exception as e:
        print(e)