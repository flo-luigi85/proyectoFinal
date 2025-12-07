import sqlite3
from utils.helpers import imprimir_error
from config import DB_NAME, TABLE_NAME  # ← Importamos correctamente

DB_NAME = 'inventario.db' #Hardcodeado para evitar dependencia de config.py
TABLE_NAME = 'productos' #Hardcodeado

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
                precio REAL NOT NULL,
                categoria TEXT
            )
            '''
            cursor.execute(sql)
            conn.commit()
            print("Base de datos inicializada correctamente.")
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

def obtener_productos():
    try:
        with conectar_db() as conn:
            cursor = conn.cursor()
            sql = f'SELECT * FROM {TABLE_NAME}'
            cursor.execute(sql)
            return cursor.fetchall()
    except sqlite3.Error as e:
        imprimir_error(f"Error al obtener los productos: {e}")
        return []

def buscar_producto_por_id(producto_id):
    try:
        with conectar_db() as conn:
            cursor = conn.cursor()
            sql = f'SELECT * FROM {TABLE_NAME} WHERE id = ?'
            cursor.execute(sql, (producto_id,))
            return cursor.fetchone()
    except sqlite3.Error as e:
        imprimir_error(f"Error al buscar el producto: {e}")
        return None
    
def buscar_producto_texto(termino):
    try:
        with conectar_db() as conn:
            cursor = conn.cursor()
            sql = f'SELECT * FROM {TABLE_NAME} WHERE nombre LIKE ? OR categoria LIKE ?'
            patron = f'%{termino}%'
            cursor.execute(sql, (patron, patron))
            return cursor.fetchall()
    except sqlite3.Error as e:
        imprimir_error(f"Error al buscar productos: {e}")
        return []

def actualizar_producto(producto_id, nombre, descripcion, cantidad, precio, categoria):
    try:
        with conectar_db() as conn:
            cursor = conn.cursor()
            sql = f'''
            UPDATE {TABLE_NAME}
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?
            '''
            cursor.execute(sql, (nombre, descripcion, cantidad, precio, categoria, producto_id))
            conn.commit()
            return cursor.rowcount > 0
    except sqlite3.Error as e:
        imprimir_error(f"Error al actualizar el producto: {e}")
        return False

def eliminar_producto(producto_id):
    try:
        with conectar_db() as conn:
            cursor = conn.cursor()
            sql = f'DELETE FROM {TABLE_NAME} WHERE id = ?'
            cursor.execute(sql, (producto_id,))
            conn.commit()
            return cursor.rowcount > 0
    except sqlite3.Error as e:
        imprimir_error(f"Error al eliminar el producto: {e}")
        return False
    
def reporte_bajo_stock(limite):
    try:
        with conectar_db() as conn:
            cursor = conn.cursor()
            sql = f'SELECT * FROM {TABLE_NAME} WHERE cantidad <= ?'
            cursor.execute(sql, (limite,))
            return cursor.fetchall()
    except sqlite3.Error as e:
        imprimir_error(f"Error al generar el reporte de bajo stock: {e}")
        return []
