from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from database import get_db
from config import settings
from schemas.token_schema import TokenData
from models.usuario import Usuario

# Utilizamos el esquema estándar de OAuth2 para obtener el token desde Authorization header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def obtener_usuario_actual(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> Usuario:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
        
    usuario = db.query(Usuario).filter(Usuario.nombre_usuario == token_data.username).first()
    if usuario is None:
        raise credentials_exception
    if not usuario.estado:
        raise HTTPException(status_code=400, detail="Usuario inactivo")
        
    return usuario
