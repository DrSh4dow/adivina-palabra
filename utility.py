# se importa la libreria os para identificar el sistema operativo
# y ejecutar comandos de limpieza
import os
import sys
from time import sleep


# Funcion de utilidad para limpiar la pantalla
def clear_screen():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

# Funcion que crea la ilusion de movimiento en puntitos


def loading_dots(time_per_dot=0.75):
    for _ in range(3):
        sys.stdout.write(bcolors.BOLD+"."+bcolors.ENDC)
        sys.stdout.flush()
        sleep(time_per_dot)

# Clase para dar colores a los textos en python


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
