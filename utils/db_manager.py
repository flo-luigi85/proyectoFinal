import sqlite3
from utils.helpers import imprimir_error
from config import DB_NAME, TABLE_NAME

def conectar_db():
    return sqlite3.connect(DB_NAME)

def inicializar_db():
    try:
        with conectar_db() as conn:
            cursor = conn.cursor()
            sql = f'''
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL
                categoria TEXT
            )
            '''
            cursor.execute(sql)
            conn.commit()
    except sqlite3.Error as e:
        imprimir_error(f"Error al inicializar la base de datos: {e}")   

def registrar_producto(nombre, descripcion, cantidad, precio, categoria):
    try: 
        with conectar_db() as conn:
            cursor = conn.cursor()
            sql = f'''
            INSERT INTO {TABLE_NAME} (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
            '''
            cursor.execute(sql, (nombre, descripcion, cantidad, precio, categoria))
            conn.commit()
            return True
    except sqlite3.Error as e:
        imprimir_error(f"Error al registrar el producto: {e}")
        return False


        
