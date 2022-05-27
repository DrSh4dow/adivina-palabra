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

# Se inicializan los puntajes de cada jugador:
jugador1_puntaje = 0
jugador2_puntaje = 0

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

    # Se inicia el turno del adivinador
    puntaje_ronda = corelogic.adivinar(
        palabra, adivinador, cantidad_intentos, numero_ronda)

    if numero_ronda % 2 == 0:
        jugador2_puntaje += puntaje_ronda
    else:
        jugador1_puntaje += puntaje_ronda

utility.clear_screen()
print(utility.bcolors.HEADER + utility.bcolors.BOLD +
      "-------------------------------------------")
print("-         El Juego Ha Finalizado!!        -")
print("-------------------------------------------\n\n" + utility.bcolors.ENDC)

# se inicializa la variable ganador
ganador = ""
# Se verifica si hubo un empate
if jugador1_puntaje == jugador2_puntaje:
    print(utility.bcolors.BOLD + utility.bcolors.OKCYAN + "Ambos jugadores obtuvieron el mismo puntaje de "+str(round(jugador1_puntaje, 2))+", por lo que ambos ganaron!!!\n" +
          utility.bcolors.ENDC + utility.bcolors.BOLD+"(o tal vez ambos perdieron...)"+utility.bcolors.ENDC)
    exit()
elif jugador1_puntaje > jugador2_puntaje:
    ganador = jugador1_nombre
else:
    ganador = jugador2_nombre

print(utility.bcolors.UNDERLINE+utility.bcolors.BOLD +
      "RESULTADOS: "+utility.bcolors.ENDC)
print("El jugador "+jugador1_nombre+" obtuvo " +
      str(round(jugador1_puntaje, 2))+" puntos.")
print("El jugador "+jugador2_nombre+" obtuvo " +
      str(round(jugador2_puntaje, 2))+" puntos.")

print("\n\n" + utility.bcolors.HEADER + utility.bcolors.BOLD +
      "EL GANADOR ES " + ganador + "!!!\n\n"+utility.bcolors.ENDC)
