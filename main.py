from utils.helpers import *
from utils import db_manager
import sys

def mostrar_tabla(productos):
    if not productos:
        print("No hay productos para mostrar.")
        return
    print(f"{'ID?':<5} {'NOMBRE':<20} {'CATEGORIA':<15} {'PRECIO' :<10} {'CANTIDAD' :<10}")
    print("-" * 65)
    for producto in productos:
        print(f"{producto[0]:<5} {producto[1][:18]:<20} {producto[5][:13]:<15} {producto[4]:<9.2f} {producto[3]:<10}")
    print("-" * 65)
    
def menu_registrar():
    imprimir_titulo("Registrar Nuevo Producto")
    nombre = validar_input_string("Ingrese el nombre del producto: ")
    descripcion = input("Ingresa la descrippción (opcional):").strip()
    categoria = validar_input_string("Ingrese la categoría del producto: ") 
    cantidad = validar_input_int("Cantidad inicial: ")
    precio = validar_input_float("Ingrese el precio del producto: ")
    
    if db_manager.registrar_producto(nombre, descripcion, cantidad, precio, categoria):
        imprimir_exito("Producto registrado exitosamente.")
        
def menu_mostrar():
    imprimir_titulo("Lista de Productos")
    productos = db_manager.obtener_productos()
    
def menu_actualizar():
    imprimir_titulo("Actualizar Producto")
    
    id_producto = validar_input_int("Ingrese el ID del producto a actualizar: ")
    producto_actual = db_manager.buscar_producto_por_id(id_producto)
    if not producto_actual:
        imprimir_error("Producto no encontrado.")
        return
    print(f"Editando producto: {producto_actual[1]}")
    print("Presione Enter para mantener el valor actual.")
    
    nuevo_nombre = input(f"Nuevo nombre [{producto_actual[1]}]: ").strip() or producto_actual[1]
    nueva_descripcion = input(f"Nueva descripción [{producto_actual[2]}]: ").strip or producto_actual[2]
    nueva_categoria = input(f"Nueva categoría [{producto_actual[5]}]: ").strip() or producto_actual[5]
    
    cantidad_str = input(f"Nueva cantidad [{producto_actual[3]}]: ").strip()
    nueva_cantidad = int(cantidad_str) if cantidad_str.isdigit() else producto_actual[3]
    
    precio_str = input(f"Nuevo precio [{producto_actual[4]}]: ").strip()
    nuevo_precio = float(precio_str) if precio_str else producto_actual[4]
    if db_manager.actualizar_producto(id_producto, nuevo_nombre, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_categoria):
        imprimir_exito("Producto actualizado exitosamente.")
    else:
        imprimir_error("Error al actualizar el producto.")

def menu_eliminar():
    imprimir_titulo("Eliminar Producto")
    menu_mostrar() # Mostrar productos antes de eliminar
    
    id_producto = validar_input_int("Ingrese el ID del producto a eliminar: ")
    
    confirmacion = input(f"¿Está seguro de que desea eliminar el producto con ID {id_producto}? (s/n): ").strip().lower()
    if confirmacion == 's':
        if db_manager.eliminar_producto(id_producto):
            imprimir_exito("Producto eliminado exitosamente.")
        else:
            imprimir_error("Error al eliminar el producto.")

def menu_buscar():
    imprimir_titulo("Buscar Producto")
    print("1. Buscar por ID")
    print("2. Buscar por Nombre o Categoría")
    opcion = input("Opción: ")
    
    if opcion == '1':
        id_producto = validar_input_int("Ingrese el ID del producto: ")
        repuesta = db_manager.buscar_producto_por_id(id_producto)
        if repuesta:
            mostrar_tabla([repuesta])
        else:
            imprimir_error("Producto no encontrado.")
    elif opcion == '2':
        termino = validar_input_string("Ingrese el término de búsqueda: ")
        resultados = db_manager.buscar_producto_texto(termino)
        mostrar_tabla(resultados)
    else:
        imprimir_error("Opción inválida.")
        
def menu_reporte():
    imprimir_titulo("Reporte de Bajo Stock")
    limite = validar_input_int("Ingrese el límite de stock: ")
    respuesta = db_manager.reporte_bajo_stock(limite)
    if respuesta:
        imprimir_exito(f"Se encontraron {len(respuesta)} productos con stock <= {limite}.")
        mostrar_tabla(respuesta)
    else:
        imprimir_exito("No hay productos con bajo stock.")

def main():
    # Inicializar la base de datos
    db_manager.inicializar_db()
    while True:
        print("\n" + "="*30)
        print("=== SISTEMA DE INVENTARIO ===")
        print("="*30)
        print("1. Registrar Producto")
        print("2. Mostrar Productos")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Buscar Producto")
        print("6. Reporte de Bajo Stock")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            menu_registrar()
        elif opcion == '2':
            menu_mostrar()
        elif opcion == '3':
            menu_actualizar()
        elif opcion == '4':
            menu_eliminar()
        elif opcion == '5':
            menu_buscar()
        elif opcion == '6':
            menu_reporte()
        elif opcion == '7':
            print("Saliendo del sistema. ¡Hasta luego!")
            sys.exit()
        else:
            imprimir_error("Opción inválida. Por favor intente de nuevo.")

if __name__ == "__main__":
    main()
        
     