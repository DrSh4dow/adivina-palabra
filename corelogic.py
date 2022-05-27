import utility
import getpass


def input_nombre_jugador(numero_jugador):
    # Funcion para preguntar el nombre del jugador con verificacion.
    # la funcion devuelve el nombre del jugador luego de verificar que no esta vacio
    nombre = ""
    while True:
        nombre = input(
            utility.bcolors.OKGREEN+"Ingrese el nombre del jugador numero "+numero_jugador+": "+utility.bcolors.ENDC)
        if nombre == "":
            print(utility.bcolors.FAIL +
                  "El nombre del jugador no puede estar vacio!"+utility.bcolors.ENDC)
            continue
        print(utility.bcolors.OKBLUE + "Jugador "+numero_jugador+": " +
              nombre + utility.bcolors.ENDC)
        break
    return nombre


def input_cantidad_palabras():
    # Funcion para preguntar la cantidad de palabras a adivinar.
    # la funcion devuelve un entero luego de realizar la conversion de string a int y verificar que los datos ingresados sean logicos y validos.
    cantidad_palabras = 0
    while True:
        cantidad_palabras = input(utility.bcolors.OKGREEN +
                                  "Digite la cantidad de palabras que debe adivinar cada jugador: "+utility.bcolors.ENDC).strip()
        if cantidad_palabras.isnumeric():
            cantidad_palabras = int(cantidad_palabras)
            if cantidad_palabras > 0:
                break
            else:
                print(utility.bcolors.FAIL +
                      "Debe ingresar numeros mayores que 0!"+utility.bcolors.ENDC)
        else:
            print(utility.bcolors.FAIL +
                  "Debe ingresar solo numeros!"+utility.bcolors.ENDC)
    return cantidad_palabras


def input_cantidad_intentos():
    cantidad_intentos = 0
    while True:
        cantidad_intentos = input(utility.bcolors.OKGREEN +
                                  "Digite la cantidad de intentos para adivinar cada palabra: "+utility.bcolors.ENDC).strip()
        if cantidad_intentos.isnumeric():
            cantidad_intentos = int(cantidad_intentos)
            break
        else:
            print(utility.bcolors.FAIL +
                  "Debe ingresar solo numeros!"+utility.bcolors.ENDC)
    return cantidad_intentos