##########################################################
# AUTHOR: Daniel Moretti Valdivia  | github.com/DrSh4dow #
#                                                        #
#                 ARCHIVO PRINCIPAL                      #
#                                                        #
##########################################################
# Importe de Modulos y librerias necesarias
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
print(utility.bcolors.OKBLUE + "Numero de Palabras por Jugador: " +
      str(cantidad_palabras) + utility.bcolors.ENDC)
print(utility.bcolors.OKBLUE + "Intentos por Palabra: " +
      str(cantidad_intentos) + utility.bcolors.ENDC+"\n")

print(utility.bcolors.WARNING+"Iniciando Partida"+utility.bcolors.ENDC)
utility.loading_dots(1.4)
utility.clear_screen()

# Inicia el juego tomando la forma de un loop de tantas rondas como el doble de palabras por cada jugador
for numero_ronda in range(cantidad_palabras*2):
    numero_ronda = numero_ronda+1
    utility.clear_screen()
    print(utility.bcolors.HEADER + utility.bcolors.BOLD +
          "-------------------------------------------")
    print("-            Ronda Numero "+str(numero_ronda) +
          "               -")
    print("-------------------------------------------\n" + utility.bcolors.ENDC)
    palabra = ""
    if numero_ronda % 2 == 0:
        palabra = corelogic.input_palabra_adivinar(jugador1_nombre)
    else:
        palabra = corelogic.input_palabra_adivinar(jugador2_nombre)
