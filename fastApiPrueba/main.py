from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Mensaje de prueba": "Prueba de Desarrollo "}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.Post('/inference', status_code=200)
def inference_endpoint(doc:Document):

    return{
        'inference':response[0],
        'usage':response[1]
    }




