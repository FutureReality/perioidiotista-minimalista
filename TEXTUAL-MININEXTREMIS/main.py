import main_menu as mm
import game as gm

while True:
    return_action = mm.main_menu()
    if return_action == "iniciar_juego":
        return_action = gm.game_loop()
    elif return_action == "cargar_juego":
        pass
    elif return_action == "salir_juego":
        exit()