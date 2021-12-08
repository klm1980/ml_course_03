from pydantic import BaseModel

class Message(BaseModel):
    message: str


class CalcRequest(BaseModel):
    a: float
    b: float


class CalcResponse(BaseModel):
    result: float

class HousePrice(BaseModel):
    price: float


class HouseInfo(BaseModel):
    n_floors: int = 3
    area: int = 50
    heating: str = 'A'


class TextInput(BaseModel):
    text: str = 'Hello World!!!'


class TextOutput(BaseModel):
    sentiment: str
    score: int