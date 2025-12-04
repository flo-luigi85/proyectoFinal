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
    print(f"{Fore.BLUE}{Style.BRIGHT}ÉXITO: {texto}{Style.RESET_ALL}")

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
            dato = input(f"{Fore.YELLOW}{prompt}{Style.RESET_ALL}").strip()
            if dato >= 0:
                return dato
        except ValueError:
            imprimir_error("Entrada inválida. Por favor ingrese un número válido.")

def validar_input_int(prompt):
     while True:
        try:
            dato = int(input(f"{Fore.YELLOW}{prompt}{Style.RESET_ALL}")).strip()
            if dato >= 0:
                return dato
        except ValueError:
            imprimir_error("Entrada inválida. Por favor ingrese un número válido.")

