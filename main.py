from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Producto(BaseModel):
    nombre:str
    precio:float
    stock:bool

produtos = []

@app.get('/productos')
def listar_pro():
    return {'productos':produtos}

@app.post('/productos')
def agregar_pro(producto:Producto):
    produtos.append(producto)
    return {'mensaje':'Producto agregado',
            'producto': producto}

@app.put('/productos/{id}')
def actualizar_pro(id:int, nom:str):
    produtos[id] = nom
    return {'mensaje':'Producto actualizado',
            'producto': nom}

@app.delete('/productos/{id}')
def eliminar_pro(id:int):
    eliminar = produtos.pop(id)
    return {'mensaje':'Producto eliminado',
            'producto': eliminar}