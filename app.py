from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from aiohttp import ClientSession
from os import environ as env


class Data(BaseModel):
    text: str


app = FastAPI(docs_url=None)
urls = [f"http://max{i+1}:5000/model/predict" for i in range(4)]

@app.post("/")
async def get_prediction(data: Data, request: Request):
    if not "X-Api-Token" in request.headers:
        raise HTTPException(403, "You are not authorized to use this endpoint.")
    if request.headers["X-Api-Token"] != env.get("token"):
        raise HTTPException(403, "You are not authorized to use this endpoint.")

    url = urls.pop(0)
    urls.append(url)

    async with ClientSession() as sess:
        async with sess.post(url, json={"text":[data.text]}) as resp:
            results = await resp.json()

    return results["results"][0]["predictions"]
