from fastapi import FastAPI

app = FastAPI()

@app.get("/saudacao/{nome}")
def home(nome: str):
    text = f"Ola tudo bem {nome}"
    return {"message": text}


@app.get('/quadrado/{numero}')
def quadrado(numero: int):
    resultado = numero * numero
    text = f"O quadrado do numero {numero} e {resultado}"
    return text

@app.get("/valor")
def dobro(valor:int):
    resultado = 2 * valor
    text = f" O dobro de {valor} e: {resultado}"
    return text
@app.get("/area_retangulo")
def area_retangulo(largura:int,altura:int = 1):
    area = altura * largura
    return {'area': area}
