##########################################################
# AUTHOR: Daniel Moretti Valdivia  | github.com/DrSh4dow #
##########################################################
# se importa la libreria os para identificar el sistema operativo
# y ejecutar comandos de limpieza
import os
import sys
from time import sleep


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
