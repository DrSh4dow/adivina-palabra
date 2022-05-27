#!/usr/bin/env python3
##########################################################
# AUTHOR: Daniel Moretti Valdivia  | github.com/DrSh4dow #
#                                                        #
#                 ARCHIVO PRINCIPAL                      #
#                                                        #
##########################################################
# Importe de Modulos
# utility para imprimir colores y detalles graficos
# corelogic contiene la logica principal de la aplicacion
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
utility.print_configuracion(
    jugador1_nombre, jugador2_nombre, cantidad_palabras, cantidad_intentos)
utility.loading_dots(1.4)
utility.clear_screen()

# Inicia el juego tomando la forma de un loop de tantas rondas como el doble de palabras por cada jugador
for numero_ronda in range(cantidad_palabras*2):
    numero_ronda = numero_ronda+1
    adivinador = ""
    proponedor = ""
    utility.clean_print_ronda(numero_ronda)
    # Se calcula quien es el proponedor y adivinador
    if numero_ronda % 2 == 0:
        proponedor = jugador1_nombre
        adivinador = jugador2_nombre
    else:
        proponedor = jugador2_nombre
        adivinador = jugador1_nombre

    # La logica especifica esta contenida en el modulo corelogic
    palabra = corelogic.input_palabra_adivinar(proponedor)

    # CASO ESPECIAL: Victoria por abandono. En caso de que el jugador proponedor no logre
    # poner una palabra valida dentro de 3 intentos, se considera victoria por abandono
    if palabra == "":
        utility.clear_screen()
        # Se calcula quien fue el proponedor y el jugador adivinador de la ronda
        print(utility.bcolors.BOLD + utility.bcolors.WARNING +
              "\n\n[ VICTORIA POR ABANDONO ]\nEl jugador proponedor ("+proponedor+") no ha propuesto ninguna palabra valida por \nmas de 3 intentos, por este motivo automaticamente\nse ha considerado ganador al jugador: "+utility.bcolors.ENDC+utility.bcolors.HEADER+adivinador+utility.bcolors.ENDC)
        print("\n\n")
        quit()

    puntaje_ronda = corelogic.adivinar(
        palabra, adivinador, cantidad_intentos, numero_ronda)
