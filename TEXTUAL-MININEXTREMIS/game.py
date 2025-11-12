import keyboard as kb
from colorama import init, Fore, Style
import os
import time
import work_engine as wk
import json


#---Esta funcion es simplemente para imprimir la interfaz, habria que moverla al work_engine---#
def interfaz(modo, sala, interfaz, text):
    
    print(f"modo actual: {modo} || sala actual: {sala}")
    print()
    print(interfaz)
    print()
    print(text)
    print()
#---Esta funcion es simplemente para imprimir la interfaz, habria que moverla al work_engine---# 

#---Diccionario de funciones que actuan en los callbacks---#
callbacks = {
    "dormir": dormir,
    # otros callbacks en caso de que existan
}
#---Diccionario de funciones que actuan en los callbacks---#



def game_loop():



#---Abrimos y asignamos a variable el JSON que contiene informacion de objetos, salas y las tomas de acciones---#
    with open('objetos.json', 'r', encoding='utf-8') as f:
        objetos = json.load(f)
#---Abrimos y asignamos a variable el JSON que contiene informacion de objetos, salas y las tomas de acciones---#



#---Aqui inicializamos las variables para que luego puedan ser utilizadas---#
    modo = "ninguno"
    tecla = "k"
    interfaz = "nada"
    text = "nada"
    objeto_interactuando = "ninguno"
    sala_actual = "dormitorio"
    
    
    options = ["moverse", "actuar", "menu"]
    selected = "moverse"
#---Aqui inicializamos las variables para que luego puedan ser utilizadas---#
    
    #DEBUGGING
    loops = 0
    #DEBUGGING
    
    
    while True:


#---Este pequenyo trozo de aqui permite que al pulsar una tecla no se detecten tresmil pulsaciones, y se tomen de una en una---#
        if kb.is_pressed(tecla):
            continue
        loops = loops + 1   
#---Este pequenyo trozo de aqui permite que al pulsar una tecla no se detecten tresmil pulsaciones, y se tomen de una en una---#

        
        os.system('cls') 
        print("modo actual: ", modo, "||", "sala actual: ", sala_actual, "||", "tecla_actual: ", tecla, "loops: ", loops, "objeto_interactuando: ", objeto_interactuando)
        print()
        print(interfaz)
        print()
        print(text)
        print()
        
        
        
        
#---Este trozo de codigo maneja el que sucede cada vez que pulsas un boton, para hacerlo escalable lee las acciones del JSON---#
        if tecla == "enter":
            tecla = "k"
            if modo == "ninguno": 
            
            
                if selected == "moverse":
                    modo = "moverse"
                    options = []
                    for sala in objetos["salas"]:
                        options.append(sala)
                    options.append("atras")
                    continue
                elif selected == "actuar":
                    modo = "actuar"
                    options = []
                    for objeto in objetos["objetos"]:
                        if objetos["objetos"][objeto]["location"] == sala_actual:
                            options.append(objeto)
                        else:
                            pass
                    options.append("atras")
                    continue
                elif selected == "menu":
                    break
            
            
            
            elif modo == "actuar":
            
                if selected == "atras":
                    modo = "ninguno"
                    options = ["moverse", "actuar", "menu"]
                elif selected in options:
                    modo = "interaccion"
                    options = []
                    objeto_interactuando = selected
                    #---Anyadir al menu de opciones las acciones---#
                    for accion in objetos["objetos"][selected]["acciones"]:
                        options.append(accion)
                    options.append("atras")
                    #---Anyadir al menu de opciones las acciones---#
                    
                    #---Anyadir el texto de descripcion---#
                    #text = objetos["objetos"][selected]["descripcion_actual"]
                continue
                
                
                
            elif modo == "moverse":
                if selected == "atras":
                    modo = "ninguno"
                    options = ["moverse", "actuar", "menu"]
                else:
                    for sala in objetos["salas"]:
                        if selected == sala:
                            sala_actual = sala
                        elif selected != sala:
                            pass
                continue
            
            elif modo == "interaccion":
                if selected == "atras":
                    modo = "ninguno"
                    options = ["moverse", "actuar", "menu"]
                elif selected in options and selected != "atras":
                    text = objetos["objetos"][objeto_interactuando]["acciones"][selected]["describir_accion"]
                    interfaz = objetos["objetos"][objeto_interactuando]["acciones"][selected]["escena"]
                continue
         
#            +-----Aqui haria falta agregar un modo "interactuando para que al darle a <<atras>> no se vaya al menu general-----+
#            |                                                                                                                  |
#            |                                                                                                                  |
#            +-----Aqui haria falta agregar un modo "interactuando para que al darle a <<atras>> no se vaya al menu general-----+
           
#---Este trozo de codigo maneja el que sucede cada vez que pulsas un boton, para hacerlo escalable lee las acciones del JSON---#
      
                
                
        selected = wk.selection(selected, tecla, options)               
        tecla = kb.read_key()
