import os
from colorama import init, Fore, Style

#Iniciasmos Colorama para la coloración de texto en la consola

init(autoreset=True)

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')    

def imprimir_titulo(texto):
    print(f"\n{Fore.GREEN}{Style.BRIGHT}=== {texto.upper()} ==={Style.RESET_ALL}")

def imprimir_error(texto):
    print(f"{Fore.RED}{Style.BRIGHT}ERROR: {texto}{Style.RESET_ALL}")

def imprimir_exito(texto):
    print(f"{Fore.GREEN}{Style.BRIGHT}ÉXITO: {texto}{Style.RESET_ALL}")

def validar_input_string(prompt):
    while True:
        dato = input(f"{Fore.YELLOW}{prompt}{Style.RESET_ALL}").strip()
        # Ingresa el nombre del producto
        if dato: 
            return dato
        imprimir_error("Entrada inválida. No puede estar vacía.")

def validar_input_float(prompt):
    while True:
        try:
            dato_str = input(f"{Fore.YELLOW}{prompt}{Style.RESET_ALL}").strip()
            if not dato_str:
                imprimir_error("Entrada no puede estar vacía.")
                continue
            dato = float(dato_str)
            if dato >= 0:
                return dato
            else:
                imprimir_error("El valor debe ser >= 0.")
        except ValueError:
            imprimir_error("Entrada inválida. Ingrese un número decimal válido.")

def validar_input_int(prompt):
    while True:
        try:
            dato_str = input(f"{Fore.YELLOW}{prompt}{Style.RESET_ALL}").strip()
            if not dato_str:
                imprimir_error("Entrada no puede estar vacía.")
                continue
            dato = int(dato_str)
            if dato >= 0:
                return dato
            else:
                imprimir_error("El valor debe ser >= 0.")
        except ValueError:
            imprimir_error("Entrada inválida. Ingrese un número entero válido.")

