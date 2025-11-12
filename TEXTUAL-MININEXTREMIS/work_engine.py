import keyboard as kb
from colorama import init, Fore, Style
import os
import time


def selection(selected, tecla, options):
    cantidad_opciones = len(options)
    
    if selected not in options:
        selected = options[0]
        
    posicion = options.index(selected)
    if tecla == "flecha derecha":
        if posicion == cantidad_opciones - 1:
            posicion = 0
        else:
            posicion = posicion + 1      
    elif tecla == "flecha izquierda":
        if posicion == 0:
            posicion = cantidad_opciones - 1
        elif posicion > 0:
            posicion = posicion - 1
    for option in options:
        if option == options[posicion]:
            print(Fore.RED + option + Style.RESET_ALL, end=' ')
        else:
            print(option, end=' ')
    selected = options[posicion]
    

        
    return selected