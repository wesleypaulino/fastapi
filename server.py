from pydantic import BaseModel

from fastapi import FastAPI

# nome da aplicacao
app = FastAPI()

# Rota Home
@app.get("/")
# funcao a ser executada quando
async def home():
    return {"message": "Hello World"}

@app.get("/saudacao/{nome}")
async def home(nome: str):
    cMsg = f'Seja bem vindo ! {nome} '
    return {"message": cMsg}

@app.get("/profile")
async def profile():
    return {"nome": "Wesley Paulino"}

@app.post("/profile")
async def signup():
    return {"message": "Perfil criado com sucesso"}

@app.put("/profile")
async def atualizar():
    return {"message": "Atualizadoerfil criado com sucesso"}

@app.delete("/profile")
async def remover():
    return {"message": "Atualizadoerfil criado com sucesso"}

# Path Parameter - Servem para filtrar
@app.get("/quadrado/{numero}")
async def quadrado(numero: int):
    resultado = numero * numero
    cMsg = f'O quadrado de {numero} é: {resultado }'
    return {"message": cMsg}

# Path Parameter
@app.get("/dobro/{numero}")
async def dobro(numero: int):
    resultado = 2 * numero
    cMsg = f'O dobro de {numero} é: {resultado}'
    return {"message": cMsg}

# Query Parameters - Servem para ordenar, qualificar
# #http://127.0.0.1:8000/area-retangulo?largura
# @app.get("/area-retangulo")
# async def area_retangulo(largura:int, altura:int):
#     area = largura * altura
#     return {'area': area}

# Query Parameters
# http://127.0.0.1:8000/area-retangulo?largura
# Seta valor default 1 para altura deixando de ser obrigatorio

@app.get("/area-retangulo") # ?nome=valor
async def area_retangulo(largura: int, altura: int = 1):
    area = largura * altura
    return {'area': area}

# Request Body - envio de informacoes para servidor
# Cadastrar Produto

#Classe Model
class Produto(BaseModel):
    nome: str
    valor: float

@app.post("/produtos")
async def produtos(produto: Produto):
    return {"message": f'Produto: ({produto.nome} - $ {produto.valor} cadastrado com sucesso'}

