from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os 

app = FastAPI()

#montar la carpeta static para archivos estaticos 
if os.path.exists("Static"):
  app.mount("/static", StaticFiles(directory="Static"), name="Static")

matrices = [ ["yadira", "daxania", "cabeza", "bravo"], ["yadira@hotmail.com", "daxania@gmail.com", "cabeza@gmail.com", "bravo@gmail.com"], ["yadira123", "daxania123", "cabeza123", "bravo123"]]


@app.post("/api/login")
async def login(request: Request):
    data = await request.json()
    user = data.get("usuario")
    password = data.get("contraseña")

    for i in range(len(matrices[0])):
        if(user == matrices[0][i] and password == matrices[2][i]):
            return {"message": "login exitoso su correo es " + matrices[1][i]}
            
    return {"message": "login fallido"}

    #Ruta para registrar usuario
     @app.post("/api/usuarios")
    async def get_usuarios():
            return {
                "nombre":"yadira",
                "apellido":"cabeza",
                "edad":"30",
                "carrera":"desarrollo de software",
                
                }

@app.get("/", response_class=HTMLResponse)
def index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

