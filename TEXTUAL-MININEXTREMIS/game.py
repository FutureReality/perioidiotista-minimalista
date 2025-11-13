import keyboard as kb
from colorama import init, Fore, Style
import os
import time
import work_engine as wk
import json
import callbacks as cb


#---Esta funcion es simplemente para imprimir la interfaz, habria que moverla al work_engine---#
def mostrar_interfaz(modo, sala, interfaz, text, dia, evento):
    os.system('cls') 
    print(f"modo actual: {modo} || sala actual: {sala} || Dia actual: {dia} || Evento: {evento}")
    print()
    print(interfaz)
    print()
    print(text)
    print()
#---Esta funcion es simplemente para imprimir la interfaz, habria que moverla al work_engine---# 






#---Diccionario de funciones que actuan en los callbacks---#



#---Diccionario de funciones que actuan en los callbacks---#



def game_loop():



#---Aqui inicializamos las variables para que luego puedan ser utilizadas---#
    modo = "ninguno"
    tecla = "k"
    interfaz = "nada"
    text = "" 
    objeto_interactuando = "ninguno"
    sala_actual = "dormitorio"
    evento = " "

    
    options = ["moverse", "actuar", "menu"]
    selected = "moverse"
#---Aqui inicializamos las variables para que luego puedan ser utilizadas---#
    
    #DEBUGGING
    loops = 0
    #DEBUGGING
    
    
    while True:

    #---Abrimos y asignamos a variable el JSON que contiene informacion de objetos, salas y las tomas de acciones---#
        with open('objetos.json', 'r', encoding='utf-8') as f:
            objetos = json.load(f)
    #---Abrimos y asignamos a variable el JSON que contiene informacion de objetos, salas y las tomas de acciones---#
        dia = objetos["world"]["mundo"]["dia"]

#---Este pequenyo trozo de aqui permite que al pulsar una tecla no se detecten tresmil pulsaciones, y se tomen de una en una---#
        if kb.is_pressed(tecla):
            continue
        loops = loops + 1   
#---Este pequenyo trozo de aqui permite que al pulsar una tecla no se detecten tresmil pulsaciones, y se tomen de una en una---#

        if evento in cb.eventos:
            text = cb.eventos[evento]()

        mostrar_interfaz(modo, sala_actual, interfaz, text, dia, evento)
        
        
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
                    for informacion in objetos["objetos"][objeto_interactuando]["acciones"][selected]:
                        if informacion == "callback":
                            callback_name = objetos["objetos"][objeto_interactuando]["acciones"][selected]["callback"]
                            if callback_name in cb.callbacks:
                                evento = cb.callbacks[callback_name]()
                        else:
                            pass
                continue
         
#            +-----Aqui haria falta agregar un modo "interactuando para que al darle a <<atras>> no se vaya al menu general-----+
#            |                                                                                                                  |
#            |                                                                                                                  |
#            +-----Aqui haria falta agregar un modo "interactuando para que al darle a <<atras>> no se vaya al menu general-----+
           
#---Este trozo de codigo maneja el que sucede cada vez que pulsas un boton, para hacerlo escalable lee las acciones del JSON---#
      
                
                
        selected = wk.selection(selected, tecla, options)               
        tecla = kb.read_key()
