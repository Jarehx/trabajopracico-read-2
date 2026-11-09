# Lista de órdenes de reparación.
ordenes = [
    {"numero": 101, "cliente": "Juan Perez", "equipo": "Notebook", "falla": "No enciende", "estado": "Pendiente", "costo": 45000},
    {"numero": 102, "cliente": "Maria Lopez", "equipo": "PC", "falla": "Problema de RAM", "estado": "En reparación", "costo": 30000},
    {"numero": 103, "cliente": "Pedro Gomez", "equipo": "Monitor", "falla": "Pantalla dañada", "estado": "Finalizada", "costo": 60000},
    {"numero": 104, "cliente": "Ana Torres", "equipo": "Notebook", "falla": "Batería defectuosa", "estado": "Pendiente", "costo": 25000},
    {"numero": 105, "cliente": "Lucas Diaz", "equipo": "PC", "falla": "Problema de fuente", "estado": "En reparación", "costo": 35000},
    {"numero": 106, "cliente": "Sofia Ruiz", "equipo": "Impresora", "falla": "No imprime", "estado": "Finalizada", "costo": 20000},
    {"numero": 107, "cliente": "Mateo Silva", "equipo": "Notebook", "falla": "Disco dañado", "estado": "Pendiente", "costo": 55000},
    {"numero": 108, "cliente": "Camila Rios", "equipo": "PC", "falla": "Sobrecalentamiento", "estado": "En reparación", "costo": 40000}
]


# Función que busca una orden por su número.
def buscar_orden(numero):

    # Recorremos todas las órdenes.
    for orden in ordenes:

        # Comprobamos si el número coincide.
        if orden["numero"] == numero:

            # Devolvemos la orden encontrada.
            return orden

    # Si termina el recorrido sin encontrarla, devuelve None.
    return None


# Función que muestra las órdenes según su estado.
def filtrar_por_estado(estado):

    # Variable para contar los resultados.
    cantidad = 0

    # Recorremos las órdenes.
    for orden in ordenes:

        # Comprobamos si el estado coincide.
        if orden["estado"].lower() == estado.lower():

            # Mostramos los datos de la orden.
            print("\nNúmero:", orden["numero"])
            print("Cliente:", orden["cliente"])
            print("Equipo:", orden["equipo"])
            print("Falla:", orden["falla"])
            print("Estado:", orden["estado"])
            print("Costo: $", orden["costo"])

            cantidad += 1

    # Si no hubo coincidencias, mostramos un mensaje.
    if cantidad == 0:
        print("No existen órdenes con ese estado.")


# Función que filtra las órdenes según su costo.
def filtrar_por_costo(limite):

    # Contador de resultados.
    cantidad = 0

    # Recorremos las órdenes.
    for orden in ordenes:

        # Comprobamos si el costo no supera el límite.
        if orden["costo"] <= limite:

            print("\nNúmero:", orden["numero"])
            print("Cliente:", orden["cliente"])
            print("Equipo:", orden["equipo"])
            print("Falla:", orden["falla"])
            print("Estado:", orden["estado"])
            print("Costo: $", orden["costo"])

            cantidad += 1

    # Comprobamos si encontramos resultados.
    if cantidad == 0:
        print("No existen órdenes dentro de ese presupuesto.")


# Función para mostrar todas las órdenes.
def mostrar_todas():

    print("\n--- TODAS LAS ÓRDENES ---")

    # Comprobamos si la lista tiene registros.
    if len(ordenes) == 0:
        print("No hay órdenes registradas.")
        return

    # Recorremos y mostramos todas las órdenes.
    for orden in ordenes:

        print("\nNúmero:", orden["numero"])
        print("Cliente:", orden["cliente"])
        print("Equipo:", orden["equipo"])
        print("Falla:", orden["falla"])
        print("Estado:", orden["estado"])
        print("Costo: $", orden["costo"])


# Menú principal del programa.
opcion = 0

# El menú se repite mientras el usuario no seleccione salir.
while opcion != 5:

    print("\n========== SISTEMA DE REPARACIONES ==========")
    print("1. Buscar orden por número")
    print("2. Filtrar órdenes por estado")
    print("3. Filtrar órdenes por costo")
    print("4. Mostrar todas las órdenes")
    print("5. Salir")

    opcion = int(input("\nSeleccione una opción: "))

    # Opción 1: búsqueda por número.
    if opcion == 1:

        numero = int(input("Ingrese el número de orden: "))

        # Guardamos el resultado que devuelve la función.
        resultado = buscar_orden(numero)

        # Comprobamos si se encontró la orden.
        if resultado != None:

            print("\n--- ORDEN ENCONTRADA ---")
            print("Número:", resultado["numero"])
            print("Cliente:", resultado["cliente"])
            print("Equipo:", resultado["equipo"])
            print("Falla:", resultado["falla"])
            print("Estado:", resultado["estado"])
            print("Costo: $", resultado["costo"])

        else:
            print("No se encontró ninguna orden con ese número.")

    # Opción 2: filtro por estado.
    elif opcion == 2:

        estado = input("Ingrese el estado (Pendiente, En reparación o Finalizada): ")

        filtrar_por_estado(estado)

    # Opción 3: filtro por costo.
    elif opcion == 3:

        limite = float(input("Ingrese el costo máximo: $"))

        filtrar_por_costo(limite)

    # Opción 4: mostrar todas las órdenes.
    elif opcion == 4:

        mostrar_todas()

    # Opción 5: salir del programa.
    elif opcion == 5:

        print("Saliendo del sistema...")

    # Si el usuario ingresa una opción incorrecta.
    else:

        print("Opción inválida. Intente nuevamente.")