from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class InfoPrevisao(BaseModel):
    empresa : str
    volume : float
    prev_fecham : float


@app.get("/")
async def root():
    return {"status": True,
            "message": "API carregada"}

@app.get("/predict")
def previsao(InfoPrevisao : InfoPrevisao):
    if InfoPrevisao.empresa == "aapl":
        w0, w1, w2 = [-15.36432, 1.06395, -3.23543]
        previsao = w0 + w1 * InfoPrevisao.prev_fecham + w2 * InfoPrevisao.volume
    else:
        previsao = None    

    return {"profecia": previsao}