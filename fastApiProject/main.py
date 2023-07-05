from typing import Union

from fastapi import FastAPI

from uce.ai.openaitest import Document, inference

app = FastAPI()


@app.get("/")
async def root():
    return {"Mensaje": "Hola Mundo"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post('/inference', status_code=200)
def inference_endpoint(doc: Document):
    response = inference(doc.prompt)
    return {
        'inference': response[0],
        'usage': response[1]
    }


