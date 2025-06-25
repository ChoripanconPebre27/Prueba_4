#Haga un programa que permita generar un menú de gestión de entradas para la gira de Rock “los Fortificados” que realizará por distintas locaciones de Chile.
#El menú principal debe permitir mostrar 5 opciones:
#TOTEM AUTOSERVICIO GIRA ROCK AND CHILE IN CHILE
#1.- Comprar entrada a “los Fortificados” en Concepción.
#2.- Comprar entrada a “los Fortificados” en Puente Alto.
#3.- Comprar entrada a “los Fortificados” en Muelle Barón en Valparaíso.
#4.- Comprar entrada a “los Fortificados” en Muelle Vergara en Viña del Mar.
#5.- Salir.
#Todas las opciones del menú deben estar implementadas mediante funciones separadas del código principal (main).
#Al ingresar a la opción 1.- Comprar entrada a “los Fortificados” en concepción se debe permitir ingresar nombre de comprador y código de confirmación por separado.
#Para que la compra sea exitosa se debe cumplir lo siguiente:
#a) el nombre de comprador no debe estar repetido,
#b) el código de confirmación debe tener largo mínimo de 6 caracteres, debe tener al menos 1 letra mayúscula, al menos 1 número y no puede tener espacio en blanco.
#c) Se maneja un Stock de 500 entradas para esta locación
#En caso de cumplir todas las condiciones, la entrada se registra exitosamente.
#Al ingresar a la opción 2.- Comprar entrada a “los Fortificados” en Puente Alto se debe permitir ingresar nombre de comprador y cantidad de entradas por se-parado. Para que la compra
#sea exitosa se debe cumplir lo siguiente:
#a) el nombre de comprador no debe estar repetido.
#b) esta locación, al ser la más grande, permite hasta comprar un máximo de 3 entradas por persona.
#d) Se maneja un Stock de 1300 entradas para esta locación.
#En caso de cumplir todas las condiciones, la entrada se registra exitosamente.
#Al ingresar a la opción 3.- Comprar entrada a “los Fortificados” en Muelle Barón Valparaíso, se debe permitir ingresar nombre de comprador
#y código de confirmación por separado. Para que la compra sea exitosa se debe cumplir lo siguiente:
#a) el nombre de comprador no debe estar repetido,
#b) el tipo de entrada solo permite “G” (General). A lo cual la entrada por defecto se registra como entrada “G” sin preguntar al comprador.
#d) Se maneja un Stock de 100 entradas para esta locación
#En caso de cumplir todas las condiciones, la entrada se registra exitosamente.
#Al ingresar a la opción 4.- Comprar entrada a “los Fortificados” en Muelle Ver-gara Viña del Mar, se debe permitir ingresar nombre de comprador y tipo de entrada.
#Para que la compra sea exitosa se debe cumplir lo siguiente:
#a) el nombre de comprador no debe estar repetido,
#b) el tipo de entrada solo permite “Sun” (Sunset) o “Ni” (Night),
#c) Se maneja un Stock de 50 entradas para esta locación
#En caso de cumplir todas las condiciones, la entrada se registra exitosamente.
#Al ingresar la opción 5.- Salir, el programa debe terminar mostrando:
#Programa terminado...
#Si se ingresa una opción distinta (que no sea 1, 2, 3, 4 o 5), debe mostrarse:
#Debe ingresar una opción válida!!
#En cualquier opción seleccionada, debe siempre validar el stock de entradas dis-ponibles.

los_fortificados = {
    "Concepción": {"nombres": [], "codigo": [], "entradas": 500},
    "Puente Alto": {"nombres": [], "entradas_pedidas": [], "entradas": 1300},
    "Muelle Barón Valparaíso": {"nombres": [], "codigo": [], "tipo_entrada": [], "entradas": 100},
    "Muelle Vergara Viña del Mar": {"nombres": [], "tipo_entrada": [], "entradas": 100}
}
uso = 0
prohibido = []
# Función del Menú

def menu(dict, uso):
    while True:
        print("TOTEM AUTOSERVICIO GIRA ROCK AND CHILE IN CHILE")
        print("\t1.- Comprar entrada a “los Fortificados” en Concepción.")
        print("\t2.- Comprar entrada a “los Fortificados” en Puente Alto.")
        print("\t3.- Comprar entrada a “los Fortificados” en Muelle Barón en Valparaíso.")
        print("\t4.- Comprar entrada a “los Fortificados” en Muelle Vergara en Viña del Mar.")
        print("\t5.- Salir.")
        elegir = input("Elija una de las opciones(1-5): ")
        elegir = try_except(elegir)
        if elegir == 1:
            comprar_conce(dict)
        elif elegir == 2:
            comprar_pa(dict, uso)
        elif elegir == 3:
            comprar_valpo(dict)
        elif elegir == 4:
            comprar_viña(dict)
        elif elegir == 5:
            salir()
            break
        else:
            print("Error: solo se permiten números entre 1 y 5")
        print(los_fortificados)

# Funciones para Try-Except

def try_except(input):
    try:
        new_input = int(input)
    except ValueError:
        print("Error: El valor ingresado no es un número entero.")
        return None
    return new_input

def try_except2(input):
    try:
        len(input) == 6
        mayuscula = None
        numero = None
        espacio = None
        for i in range(len(input)):
            if input[i] != input[i].lower():
                mayuscula = input[i]
            elif input[i].isdigit() == True:
                numero = input[i]
            elif input[i] == " ":
                espacio = " "
        if mayuscula != None and numero != None and espacio == None:
            return "validado"
        else:
            print("Error: código de confirmación inválido.")
            return None
    except ValueError:
        print("Error: código de confirmación inválido.")
        return None

# Funciones para Opciones del Menú

def comprar_conce(dict):
    valido = None
    if dict["Concepción"]["entradas"] < 0:
        print("Error: Entradas agotadas.")
        return
    print("-- Compra en Concepción --")
    name_comprador = input("Nombre del comprador: ")
    if len(dict["Concepción"]["nombres"]) == 0:
        valido = "valido"
    else:
        for i in range(len(dict["Concepción"]["nombres"])):
            if name_comprador == dict["Concepción"]["nombres"][i]:
                print("Error: Esta nombre ya aparece en el sistema.")
                return
    codigo_confirm = input("Código de confirmación: ")
    validar = try_except2(codigo_confirm)
    if valido == "valido" and validar == "validado":
        dict["Concepción"]["nombres"].append(name_comprador)
        dict["Concepción"]["entradas"] -= 1
        print(f"¡Entrada registrada! Stock restante: {dict["Concepción"]["entradas"]}")
        return

def comprar_pa(dict, uso):
    if dict["Puente Alto"]["entradas"] < 0:
        print("Error: Entradas agotadas.")
        return
    valido = None
    print("-- Compra en Puente Alto --")
    name_comprador = input("Nombre del comprador: ")
    if len(dict["Puente Alto"]["nombres"]) == 0:
        valido = "valido"
    else:
        for i in range(len(dict["Puente Alto"]["nombres"])):
            if name_comprador == dict["Puente Alto"]["nombres"][i]:
                print("Error: Esta nombre ya aparece en el sistema.")
                return
        valido = "valido"
    codigo_confirm = input("Código de confirmación: ")
    validar = try_except2(codigo_confirm)
    if codigo_confirm in prohibido:
        print("Error: Ya no se puede utilizar este código.")
        return
    if valido == "valido" and validar == "validado":
        entradas = try_except(input("Cantidad de entradas (máx 3): "))
        if entradas < 1 and entradas > 3:
            print("Error: solo se permiten entre 1 y 3 entradas por persona")
            return
        dict["Puente Alto"]["nombres"].append(name_comprador)
        dict["Puente Alto"]["entradas"] -= entradas
        uso += 1
        if uso == 3:
            prohibido.append(codigo_confirm)
            uso = 0
        print(f"¡Entradas registradas! Stock restante: {dict["Puente Alto"]["entradas"]}")
        return

def comprar_valpo(dict):
    if dict["Muelle Barón Valparaíso"]["entradas"] < 0:
        print("Error: Entradas agotadas.")
        return
    valido = None
    print("-- Compra en Muelle Barón Valparaíso --")
    name_comprador = input("Nombre del comprador: ")
    if len(dict["Muelle Barón Valparaíso"]["nombres"]) == 0:
        valido = "valido"
    else:
        for i in range(len(dict["Muelle Barón Valparaíso"]["nombres"])):
            if name_comprador == dict["Muelle Barón Valparaíso"]["nombres"][i]:
                print("Error: Esta nombre ya aparece en el sistema.")
                return
        valido = "valido"
    codigo_confirm = input("Código de confirmación: ")
    validar = try_except2(codigo_confirm)
    if valido == "valido" and validar == "validado":
        print("Tipo de entrada asignado: G")
        dict["Muelle Barón Valparaíso"]["nombres"].append(name_comprador)
        dict["Muelle Barón Valparaíso"]["tipo_entrada"].append("G")
        dict["Muelle Barón Valparaíso"]["entradas"] -= 1
        print(f"¡Entrada registrada! Stock restante: {dict["Muelle Barón Valparaíso"]["entradas"]}")
        return

def comprar_viña(dict):
    if dict["Muelle Vergara Viña del Mar"]["entradas"] < 0:
        print("Error: Entradas agotadas.")
        return
    valido = None
    print("-- Compra en Muelle Vergara Viña del Mar --")
    name_comprador = input("Nombre del comprador: ")
    if len(dict["Muelle Vergara Viña del Mar"]["nombres"]) == 0:
        valido = "valido"
    else:
        for i in range(len(dict["Muelle Vergara Viña del Mar"]["nombres"])):
            if name_comprador == dict["Muelle Vergara Viña del Mar"]["nombres"][i]:
                print("Error: Esta nombre ya aparece en el sistema.")
                return
    codigo_confirm = input("Código de confirmación: ")
    validar = try_except2(codigo_confirm)
    if valido == "valido" and validar == "validado":
        tipo_entrada = input("Tipo de entrada (Sun=Sunset, Ni=Night): ")
        if tipo_entrada != "Sun" and tipo_entrada != "Ni":
            print("Error: tipo de entrada inválido.")
            return
        dict["Muelle Vergara Viña del Mar"]["nombres"].append(name_comprador)
        dict["Muelle Vergara Viña del Mar"]["tipo_entrada"].append(tipo_entrada)
        dict["Muelle Vergara Viña del Mar"]["entradas"] -= 1
        print(f"¡Entrada registrada! Stock restante: {dict["Muelle Vergara Viña del Mar"]["entradas"]}")
        return

def salir():
    print("¡Que tenga buen día!")
    print("Saliendo...")

# Desarrollo

menu(los_fortificados, uso)