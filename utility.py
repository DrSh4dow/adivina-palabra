##########################################################
# AUTHOR: Daniel Moretti Valdivia  | github.com/DrSh4dow #
##########################################################
# se importa la libreria os para identificar el sistema operativo
# y ejecutar comandos de limpieza
import os
import sys
from time import sleep


def print_configuracion(jugador1_nombre, jugador2_nombre, cantidad_palabras, cantidad_intentos):
    # Funcion para imprimir la configuracion actual del juego
    print(bcolors.HEADER + bcolors.BOLD +
          "-------------------------------------------")
    print("-        Configuracion Seleccionada       -")
    print("-------------------------------------------\n" + bcolors.ENDC)
    print(bcolors.OKBLUE + "Jugador 1: " +
          jugador1_nombre + bcolors.ENDC)
    print(bcolors.OKBLUE + "Jugador 2: " +
          jugador2_nombre + bcolors.ENDC)
    print(bcolors.OKBLUE + "Numero de Palabras por Jugador: " +
          str(cantidad_palabras) + bcolors.ENDC)
    print(bcolors.OKBLUE + "Intentos por Palabra: " +
          str(cantidad_intentos) + bcolors.ENDC+"\n")
    print(bcolors.WARNING+"Iniciando Partida"+bcolors.ENDC)


def clean_print_ronda(numero_ronda):
    # Se limpia la pantalla y empieza el turno del adivinador
    clear_screen()
    print(bcolors.HEADER + bcolors.BOLD +
          "-------------------------------------------")
    print("-            Ronda Numero "+str(numero_ronda) +
          "               -")
    print("-------------------------------------------\n" + bcolors.ENDC)


def clear_screen():
    # Funcion de utilidad para limpiar la pantalla
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


def loading_dots(time_per_dot=0.75):
    # Funcion que crea la ilusion de movimiento en puntitos
    for _ in range(3):
        sleep(time_per_dot/2)
        sys.stdout.write(bcolors.BOLD+"."+bcolors.ENDC)
        sys.stdout.flush()
        sleep(time_per_dot/2)


class bcolors:
    # Clase para dar colores a los textos en python
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
