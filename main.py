##########################################################
# AUTHOR: Daniel Moretti Valdivia  | github.com/DrSh4dow #
##########################################################
# Importe de Modulos y librerias necesarias
import sanitizer
import utility
import corelogic

# Dar la bienvenida al juego
utility.clear_screen()
print(utility.bcolors.HEADER + utility.bcolors.BOLD +
      "-------------------------------------------")
print("-    Bienvenidos a Adivina Palabra!!      -")
print("-------------------------------------------\n\n" + utility.bcolors.ENDC)

# Preguntar por los nombres de los jugadores
jugador1_nombre = corelogic.input_nombre_jugador("1")
jugador2_nombre = corelogic.input_nombre_jugador("2")


# Se le pregunta a los jugadores la cantidad de palabras que deben adivinar
cantidad_palabras = corelogic.input_cantidad_palabras()

# Se pregunta por la cantidad maxima de intentos para adivinar cada palabra
cantidad_intentos = corelogic.input_cantidad_intentos()

# Se presentan la configuracion ingresada
utility.clear_screen()
print(utility.bcolors.HEADER + utility.bcolors.BOLD +
      "-------------------------------------------")
print("-        Configuracion Seleccionada       -")
print("-------------------------------------------\n" + utility.bcolors.ENDC)

print(utility.bcolors.OKBLUE + "Jugador 1: " +
      jugador1_nombre + utility.bcolors.ENDC)
print(utility.bcolors.OKBLUE + "Jugador 2: " +
      jugador2_nombre + utility.bcolors.ENDC)
print(utility.bcolors.OKBLUE + "Numero de Palabras: " +
      str(cantidad_palabras) + utility.bcolors.ENDC)
print(utility.bcolors.OKBLUE + "Intentos por Palabra: " +
      str(cantidad_intentos) + utility.bcolors.ENDC+"\n")

print(utility.bcolors.WARNING+"Iniciando Partida"+utility.bcolors.ENDC)
utility.loading_dots(1.4)
utility.clear_screen()
