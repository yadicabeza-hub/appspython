import sqlite3
from pathlib import Path

path = Path(__file__).resolve().parent / 'gestion_productos.db'
print('db path:', path)
print('exists:', path.exists())
conn = sqlite3.connect(path)
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
print('tables:', tables)
if ('productos',) in tables:
    cur.execute('PRAGMA table_info(productos);')
    print('productos schema:', cur.fetchall())
conn.close()
