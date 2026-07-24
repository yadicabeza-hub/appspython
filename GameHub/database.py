from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings

# Formato URL SQLAlchemy: mysql+pymysql://user:password@host:port/database
# Si la contraseña está vacía, se omite
pwd = f":{settings.DB_PASSWORD}" if settings.DB_PASSWORD else ""
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{settings.DB_USER}{pwd}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}?charset=utf8mb4"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_recycle=3600,
    echo=False
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
