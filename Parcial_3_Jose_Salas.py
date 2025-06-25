#Haga un programa que permita generar un menú de gestión de entradas para la gira de Rock “los Fortificados” que realizará por distintas locaciones de Chile.
#El menú principal debe permitir mostrar 5 opciones:
#TOTEM AUTOSERVICIO GIRA ROCK AND CHILE IN CHILE
#1.- Comprar entrada a “los Fortificados” en Concepción.
#2.- Comprar entrada a “los Fortificados” en Puente Alto.
#3.- Comprar entrada a “los Fortificados” en Muelle Barón en Valparaíso.
#4.- Comprar entrada a “los Fortificados” en Muelle Vergara en Viña del Mar.
#5.- Salir.
#Todas las opciones del menú deben estar implementadas mediante funciones separadas del código principal (main).
#Al ingresar a la opción 1.- Comprar entrada a “los Fortificados” en concepción se debe permitir ingresar nombre de comprador y código de confirmación por separado. Para que la compra sea exitosa se debe cumplir lo siguiente:
#a) el nombre de comprador no debe estar repetido,
#b) el código de confirmación debe tener largo mínimo de 6 caracteres, debe tener al menos 1 letra mayúscula, al menos 1 número y no puede tener espacio en blanco.
#c) Se maneja un Stock de 500 entradas para esta locación
#En caso de cumplir todas las condiciones, la entrada se registra exitosamente.
#Al ingresar a la opción 2.- Comprar entrada a “los Fortificados” en Puente Alto se debe permitir ingresar nombre de comprador y cantidad de entradas por se-parado. Para que la compra sea exitosa se debe cumplir lo siguiente:
#a) el nombre de comprador no debe estar repetido.
#b) esta locación, al ser la más grande, permite hasta comprar un máximo de 3 en-tradas por persona.
#d) Se maneja un Stock de 1300 entradas para esta locación.
#En caso de cumplir todas las condiciones, la entrada se registra exitosamente.
#Al ingresar a la opción 3.- Comprar entrada a “los Fortificados” en Muelle Ba-rón Valparaíso, se debe permitir ingresar nombre de comprador y código de confirmación por separado. Para que la compra sea exitosa se debe cumplir lo siguiente:
#a) el nombre de comprador no debe estar repetido,
#b) el tipo de entrada solo permite “G” (General). A lo cual la entrada por defecto se registra como entrada “G” sin preguntar al comprador.
#d) Se maneja un Stock de 100 entradas para esta locación
#En caso de cumplir todas las condiciones, la entrada se registra exitosamente.
#Al ingresar a la opción 4.- Comprar entrada a “los Fortificados” en Muelle Ver-gara Viña del Mar, se debe permitir ingresar nombre de comprador y tipo de entrada. Para que la compra sea exitosa se debe cumplir lo siguiente:
#a) el nombre de comprador no debe estar repetido,
#b) el tipo de entrada solo permite “Sun” (Sunset) o “Ni” (Night),
#c) Se maneja un Stock de 50 entradas para esta locación
#En caso de cumplir todas las condiciones, la entrada se registra exitosamente.
#Al ingresar la opción 5.- Salir, el programa debe terminar mostrando:
#Programa terminado...
#Si se ingresa una opción distinta (que no sea 1, 2, 3, 4 o 5), debe mostrarse:
#Debe ingresar una opción válida!!
#En cualquier opción seleccionada, debe siempre validar el stock de entradas dis-ponibles.

def menu():
    print("TOTEM AUTOSERVICIO GIRA ROCK AND CHILE IN CHILE")
    print("\t1.- Comprar entrada a “los Fortificados” en Concepción.")
    print("\t2.- Comprar entrada a “los Fortificados” en Puente Alto.")
    print("\t3.- Comprar entrada a “los Fortificados” en Muelle Barón en Valparaíso.")
    print("\t4.- Comprar entrada a “los Fortificados” en Muelle Vergara en Viña del Mar.")
    print("\t5.- Salir.")
    elegir = input("Elija una de las opciones(1-5): ")
    try_except(elegir)

def try_except(input):
    try:
        new_input = int(input)
    except ValueError:
        print("Error: El valor ingresado no es un número entero.")

def comprar_conce():
    return
def comprar_pa():
    return
def comprar_valpo():
    return
def comprar_viña():
    return
def salir():
    print("¡Que tenga buen día!")
    print("Saliendo...")