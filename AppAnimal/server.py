from fastapi import FastAPI
from typing import List,Optional
from pydantic import BaseModel
from uuid import uuid4
app = FastAPI()

class Animal(BaseModel):
    id: Optional[int]
    nome: str
    idade: int
    sexo: str
    cor: str
banco: List[Animal] = []


@app.get('/animais')
def lisar_animais():
    return banco

@app.post('/animais')
def criar_animais(animal:Animal):
    banco.append(animal)
    animal.id = uuid4()
    return None
