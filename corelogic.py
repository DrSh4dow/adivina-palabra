##########################################################
# AUTHOR: Daniel Moretti Valdivia  | github.com/DrSh4dow #
##########################################################
# Se importan las librerias necesarias
# Utility para imprimir colores y detalles graficos
# Getpass para no mostrar la palabra mientras esta se escribe
# y re para utilizar regex como medio de sanitizar
import utility
import getpass
import re


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
    # Funcion que pregunta la cantidad de intentos a adivinar por palabra.
    # Posee una verificacion de que los datos ingresados sean numericos
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


def input_palabra_adivinar(nombre_proponedor):
    # Funcion de ingreso para el proponedor, el cual ingresara la palabra a adivinar
    # En esta funcion se sanitiza la palabra quitandole espacios y pasandola a minusculas
    # Junto con esto se verifica que la palabra no este vacia, no sea mayor a 20 caracteres y que pertenezca al alfabeto español.
    intentos_proponedor = 0
    palabra = ""
    print(utility.bcolors.OKBLUE + "Ahora juega Proponedor: " +
          nombre_proponedor + utility.bcolors.ENDC)
    print(utility.bcolors.BOLD + utility.bcolors.WARNING +
          "\n\n[ ADVERTENCIA ]\nLa palabra no aparecera en pantalla mientras la escribe\nasi que digite teniendo eso en cuenta y que solo podra \ningresar caracteres pertenencientes al alfabeto español"+utility.bcolors.ENDC)

    # Se inicia un bucle para preguntar la palabra
    while True:
        # Intentos para ingresar la palabra a adivinar, si pasan los 3 intentos se considera derrota para el proponedor
        if intentos_proponedor >= 3:
            palabra = ""
            break
        print(utility.bcolors.BOLD+"intentos restantes:" +
              str(3-intentos_proponedor)+utility.bcolors.ENDC)

        # Se utiliza la funcion getpass de la libreria getpass para obtener la palabra de manera que el input no se vea reflejado al stdout
        # y no sea contraproducente para el juego
        palabra = getpass.getpass(
            utility.bcolors.OKGREEN+"Palabra: "+utility.bcolors.ENDC).lower().strip()

        # La verificacion de la palabra ocurre en las siguientes lineas
        if palabra == "":
            print(utility.bcolors.FAIL +
                  "La palabra no puede estar vacia!"+utility.bcolors.ENDC)
            intentos_proponedor += 1
            continue
        elif len(palabra) > 20:
            print(utility.bcolors.FAIL +
                  "La palabra no se mayor a 20 caracteres de largo!"+utility.bcolors.ENDC)
            intentos_proponedor += 1
            continue
        elif not re.match('^[a-zñ]+$', palabra):
            print(utility.bcolors.FAIL +
                  "La palabra debe pertenecer al alfabeto español!"+utility.bcolors.ENDC)
            intentos_proponedor += 1
            continue
        else:
            break

    return palabra


def adivinar(palabra, nombre_adivinador, limite_intentos, ronda):
    # Preparacion de variables
    palabra = list(palabra)
    progreso = []
    for _ in palabra:
        progreso.append("_")

    # Se inicia un bucle de adivinacion el cual pone como condicion el limite de errores vs la cantidad de errores
    errores = 0
    puntaje_ronda = 0
    while errores < limite_intentos:
        # Se verifica si el jugador completo la palabra y se calcula el puntaje en caso de que halla encontrado la palabra:
        if palabra == progreso:
            puntaje_ronda = (1-(errores/limite_intentos))*len(palabra)
            break
        # Se imprimen el numero de ronda y el jugador correspondiente luego de limpiar la pantalla para mantener una UI limpia
        utility.clean_print_ronda(ronda)
        print(utility.bcolors.OKBLUE + "Ahora juega Adivinador: " +
              nombre_adivinador + utility.bcolors.ENDC)
        print("\n")

        # Se ejecuta la funcion para mostrar el progreso de la adivinacion junto con la pista basada en el numero de letras
        render_palabra(progreso)

        print(utility.bcolors.BOLD+"intentos restantes:" +
              str(limite_intentos-errores)+utility.bcolors.ENDC)
        suposicion = input(utility.bcolors.OKGREEN+"Letra: " +
                           utility.bcolors.ENDC).lower().strip()

        # Se sanitiza el input de la suposicion verificando si se cumplen condiciones de datos.
        if suposicion == "":
            print(utility.bcolors.BOLD + utility.bcolors.WARNING +
                  "[ ADVERTENCIA ] La Suposicion no puede estar vacia (no se le descontara como error)"+utility.bcolors.ENDC)
            utility.loading_dots()
            continue
        elif not re.match('^[a-zñ]+$', suposicion):
            print(utility.bcolors.BOLD + utility.bcolors.WARNING +
                  "[ ADVERTENCIA ] La Suposicion debe pertenecer al alfabeto español (no se le descontara como error)"+utility.bcolors.ENDC)
            utility.loading_dots()
            continue
        elif len(suposicion) > 1:
            print(utility.bcolors.BOLD + utility.bcolors.FAIL +
                  "[ ERROR ] La Suposicion no puede contener mas de una letra (intentando pasarse de listo?)"+utility.bcolors.ENDC)
            errores += 1
            utility.loading_dots(1)
            continue

        progreso, numero_coincidancias = comparar(
            suposicion, palabra, progreso)

        if numero_coincidancias == 0:
            print(utility.bcolors.BOLD + utility.bcolors.FAIL +
                  "La palabra no contiene la letra: \""+suposicion+"\" "+utility.bcolors.ENDC)
            errores += 1
            utility.loading_dots(0.5)
            continue

    # En caso de que se supere el limite de intentos el jugador adivinador consigue 0 puntos en la ronda
    if errores == limite_intentos:
        utility.clean_print_ronda(ronda)
        print(utility.bcolors.OKBLUE + "Ahora juega Adivinador: " +
              nombre_adivinador + utility.bcolors.ENDC)
        print("\n")
        render_palabra(progreso)

        print(utility.bcolors.BOLD + utility.bcolors.FAIL +
              "Se supero el limite de intentos, el jugador "+nombre_adivinador+" obtiene un puntaje de 0 en esta ronda"+utility.bcolors.ENDC)
        utility.loading_dots()
    else:
        utility.clean_print_ronda(ronda)
        print(utility.bcolors.OKBLUE + "Ahora juega Adivinador: " +
              nombre_adivinador + utility.bcolors.ENDC)
        print("\n")
        render_palabra(progreso)
        print(utility.bcolors.BOLD + utility.bcolors.OKCYAN + "El jugador " +
              nombre_adivinador+" encontro la palabra y obtuvo: "+str(round(puntaje_ronda, 2))+" puntos en esta ronda!"+utility.bcolors.ENDC)
        utility.loading_dots(1)

    # Se devuelve el puntaje de la ronda
    return puntaje_ronda


def render_palabra(palabra):
    # Funcion que renderiza a stdout de manera elegante el progreso de la palabra que se esta adivinando
    rendered_figure = ""
    for letter in palabra:
        rendered_figure = rendered_figure + letter + " "
    print("PALABRA: "+utility.bcolors.BOLD +
          utility.bcolors.WARNING + rendered_figure + utility.bcolors.ENDC)


def comparar(letra, palabra, progreso):
    nuevo_progreso = []
    cantidad_coincidencias = 0
    for idx, letter in enumerate(palabra):
        if letra == letter:
            nuevo_progreso.append(letra)
            cantidad_coincidencias += 1
        else:
            nuevo_progreso.append(progreso[idx])

    return (nuevo_progreso, cantidad_coincidencias)
