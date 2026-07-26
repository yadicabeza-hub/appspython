# Migration script from SQLite to MySQL
import sqlite3
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from urllib.parse import quote_plus

DB_USER = "root"
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "Gestion_productos_dbs"

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
DEFAULT_DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/"
)

# Create MySQL database if not exists
def ensure_database_exists():
    engine = create_engine(DEFAULT_DATABASE_URL)
    with engine.connect() as connection:
        connection.execute(
            sqlalchemy.text(
                f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
            )
        )
    engine.dispose()

ensure_database_exists()

Base = declarative_base()

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=False)
    precio = Column(Float, nullable=False)
    cantidad = Column(Integer, nullable=False)

mysql_engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base.metadata.create_all(bind=mysql_engine)

# Read data from SQLite
def read_sqlite_data():
    sqlite_conn = sqlite3.connect("gestion_productos.db")
    sqlite_cur = sqlite_conn.cursor()
    sqlite_cur.execute("SELECT id, nombre, descripcion, precio, cantidad FROM productos")
    rows = sqlite_cur.fetchall()
    sqlite_conn.close()
    return rows

rows = read_sqlite_data()
print(f"Migrando {len(rows)} filas desde SQLite a MySQL...")

# Insert rows into MySQL
def migrate_rows(rows):
    with mysql_engine.begin() as conn:
        insert_stmt = sqlalchemy.text(
            "INSERT INTO productos (id, nombre, descripcion, precio, cantidad) VALUES (:id, :nombre, :descripcion, :precio, :cantidad)"
        )
        for row in rows:
            conn.execute(insert_stmt, {
                "id": row[0],
                "nombre": row[1],
                "descripcion": row[2],
                "precio": row[3],
                "cantidad": row[4],
            })

migrate_rows(rows)
print("Migración completada.")
