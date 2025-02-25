from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List,Optional
from pydantic import BaseModel
from uuid import uuid4
app = FastAPI()

origins = ['http://127.0.0.1:8080']
app.add_middleware(
     CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Animal(BaseModel):
    id: Optional[str]
    nome: str
    idade: int
    sexo: str
    cor: str
banco: List[Animal] = []


@app.get('/animais')
def lisar_animais():
    return banco
@app.get("/animais/{animal_id}")
def obter_animai(animal_id: str):
    for animal in banco:
        if animal.id == animal_id:
            return animal
    return {'erro': 'Animal nao localizado'}

@app.delete('/animais/{animal_id}')
def remover_animal(animal_id: str):
    posicao = -1
    # Buscar a posicao do  animal
    for index, animal in enumerate(banco):
        if animal.id == animal_id:
            posicao = index
            break
    if posicao !=  -1:
        banco.pop(posicao)
        return {'mensagen':'Animal removido com sucesso!'}
    else:
        return {'erro': 'Animal nao localizado'}
    
@app.post('/animais')
def criar_animais(animal:Animal):
    banco.append(animal)
    animal.id = str(uuid4())
    return None
