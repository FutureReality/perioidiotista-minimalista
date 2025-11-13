import keyboard as kb
from colorama import init, Fore, Style
import os
import time
import work_engine as wk
import json



def dormir():

    with open('objetos.json', 'r', encoding='utf-8') as f:
        objetos = json.load(f)

    dia = objetos["world"]["mundo"]["dia"]
    if dia < 3:
        objetos["world"]["mundo"]["dia"] = dia + 1  
    elif dia == 3:
        return "final"
    with open('objetos.json', 'w') as f:
        json.dump(objetos, f, indent=4)


def final():
    text = "Fin del juego"
    return text

    
callbacks = {
    "dormir": dormir,
    # otros callbacks en caso de que existan
}

eventos = {
    "final": final,
} 