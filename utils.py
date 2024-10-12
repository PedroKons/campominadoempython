import os
import platform
from colorama import Fore, Style, init

init()

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls") # Para windows
    else:
        os.system("clear") # Para Linux

def color_cell(cell):
    if cell == "#":
        return Fore.LIGHTYELLOW_EX + cell + Style.RESET_ALL  # Laranja para áreas não reveladas
    elif cell == "B":
        return Fore.RED + cell + Style.RESET_ALL  # Vermelho para bombas
    elif cell == "-":
        return Fore.WHITE + cell + Style.RESET_ALL  # Branco para espaços vazios
    else:
        return Fore.BLUE + cell + Style.RESET_ALL  # Azul para número de bombas ao redor