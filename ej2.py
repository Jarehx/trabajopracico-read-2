# Catálogo de repuestos representados mediante diccionarios.
repuestos = [
    {"codigo": 101, "descripcion": "SSD Kingston 480 GB", "categoria": "Almacenamiento", "marca": "Kingston", "precio": 45000, "stock": 5},
    {"codigo": 102, "descripcion": "SSD Crucial 1 TB", "categoria": "Almacenamiento", "marca": "Crucial", "precio": 80000, "stock": 3},
    {"codigo": 103, "descripcion": "Memoria RAM DDR4 8 GB", "categoria": "Memoria", "marca": "Kingston", "precio": 30000, "stock": 0},
    {"codigo": 104, "descripcion": "Fuente 600W", "categoria": "Alimentación", "marca": "Corsair", "precio": 65000, "stock": 4},
    {"codigo": 105, "descripcion": "Mouse óptico USB", "categoria": "Periféricos", "marca": "Logitech", "precio": 12000, "stock": 8},
    {"codigo": 106, "descripcion": "Teclado mecánico", "categoria": "Periféricos", "marca": "Redragon", "precio": 35000, "stock": 2},
    {"codigo": 107, "descripcion": "Disco rígido 1 TB", "categoria": "Almacenamiento", "marca": "Seagate", "precio": 55000, "stock": 0},
    {"codigo": 108, "descripcion": "Placa de video GTX 1660", "categoria": "Video", "marca": "Nvidia", "precio": 180000, "stock": 1}
]

# Solicitamos el texto que se desea buscar.
busqueda = input("Ingrese el nombre o parte del repuesto: ").lower()

# Contadores de resultados.
total_coincidencias = 0
disponibles = 0

print("\n--- RESULTADOS DE LA BÚSQUEDA ---")

# Recorremos todos los repuestos.
for repuesto in repuestos:

    # Convertimos la descripción a minúsculas.
    descripcion = repuesto["descripcion"].lower()

    # Comprobamos si el texto ingresado aparece en la descripción.
    if busqueda in descripcion:

        # Contamos la coincidencia.
        total_coincidencias += 1

        print("\nCódigo:", repuesto["codigo"])
        print("Descripción:", repuesto["descripcion"])
        print("Categoría:", repuesto["categoria"])
        print("Marca:", repuesto["marca"])
        print("Precio: $", repuesto["precio"])
        print("Stock:", repuesto["stock"])

        # Comprobamos si el repuesto tiene unidades disponibles.
        if repuesto["stock"] > 0:
            print("Disponibilidad: Disponible")
            disponibles += 1
        else:
            print("Disponibilidad: Sin stock")

# Mostramos los resultados finales.
print("\n--- RESUMEN ---")
print("Total de coincidencias:", total_coincidencias)
print("Repuestos disponibles:", disponibles)

# Si no hubo coincidencias, mostramos un mensaje.
if total_coincidencias == 0:
    print("La búsqueda no produjo resultados.")