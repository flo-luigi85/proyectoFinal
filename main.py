from utils.helpers import *
from utils import db_manager
import sys

def mostrar_tabla(productos):
    if not productos:
        print("No hay productos para mostrar.")
        return
    print(f"{'ID?':<5} {'NOMBRE':<20} {'CATEGORIA':<15} {'PRECIO'}'}")




