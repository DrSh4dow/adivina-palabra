##########################################################
# AUTHOR: Daniel Moretti Valdivia  | github.com/DrSh4dow #
##########################################################
# Importe de Modulos y librerias necesarias
import sanitizer
import utility

utility.clear_screen()
# Dar la bienvenida al juego
print(utility.bcolors.HEADER + utility.bcolors.BOLD +
      "-------------------------------------------")
print("-    Bienvenidos a Adivina Palabra!!      -")
print("-------------------------------------------\n\n" + utility.bcolors.ENDC)

# Preguntar por los nombres de los jugadores en un
# loop de manera que puedan confirmar su seleccion
jugador1_nombre = ""
jugador2_nombre = ""

while True:
    jugador1_nombre = input(
        utility.bcolors.OKGREEN+"Ingrese el nombre del jugador numero 1: "+utility.bcolors.ENDC)
    if jugador1_nombre == "":
        print(utility.bcolors.FAIL +
              "El nombre del jugador no puede estar vacio!"+utility.bcolors.ENDC)
        continue
    print(utility.bcolors.OKBLUE + "Jugador 1: " +
          jugador1_nombre + utility.bcolors.ENDC)
    utility.loading_dots()

    utility.clear_screen()
    break

while True:
    jugador2_nombre = input(
        utility.bcolors.OKGREEN+"Ingrese el nombre del jugador numero 2: "+utility.bcolors.ENDC)
    if jugador2_nombre == "":
        print(utility.bcolors.FAIL +
              "El nombre del jugador no puede estar vacio!"+utility.bcolors.ENDC)
        continue
    print(utility.bcolors.OKBLUE + "Jugador 2: " +
          jugador2_nombre + utility.bcolors.ENDC)

    utility.loading_dots()

    utility.clear_screen()
    break
