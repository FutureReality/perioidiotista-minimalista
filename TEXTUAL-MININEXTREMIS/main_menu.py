import keyboard as kb
from colorama import init, Fore, Style
import os
import time
import work_engine as wk


init(autoreset=True) 


    
    
def main_menu():
    selected = "START"
    options = ["START", "CARGAR", "SALIR"]
    tecla = "k"
    return_action = None
    while True:

        if kb.is_pressed(tecla):
            continue

        os.system('cls')        
        print("PERIO-IDIOTISTA")
        print()
        selected = wk.selection(selected, tecla, options)
        if tecla == "q":
            exit()
        if tecla == "enter":
            if selected == "START":
                return "iniciar_juego"
            elif selected == "CARGAR":
                return "cargar_juego"
            elif selected == "SALIR":
                return "salir_juego"
        tecla = kb.read_key()
        

        
#menu(text)