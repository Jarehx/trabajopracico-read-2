# Lista de equipos del laboratorio.
# Cada equipo se representa mediante un diccionario.
inventario = [
    {"inventario": 101, "tipo": "Computadora", "marca": "HP", "estado": "Disponible", "anio": 2022},
    {"inventario": 102, "tipo": "Monitor", "marca": "Samsung", "estado": "Disponible", "anio": 2020},
    {"inventario": 103, "tipo": "Teclado", "marca": "Logitech", "estado": "En reparación", "anio": 2021},
    {"inventario": 104, "tipo": "Mouse", "marca": "Genius", "estado": "Disponible", "anio": 2023},
    {"inventario": 105, "tipo": "Notebook", "marca": "Lenovo", "estado": "Baja", "anio": 2019},
    {"inventario": 106, "tipo": "Computadora", "marca": "Dell", "estado": "Disponible", "anio": 2024},
    {"inventario": 107, "tipo": "Impresora", "marca": "Epson", "estado": "Disponible", "anio": 2018},
    {"inventario": 108, "tipo": "Proyector", "marca": "ViewSonic", "estado": "En reparación", "anio": 2022}
]

# Solicitamos el año mínimo al usuario.
anio_minimo = int(input("Ingrese el año mínimo: "))

# Variable para contar los equipos que cumplen ambas condiciones.
cantidad = 0

print("\n--- EQUIPOS DISPONIBLES QUE CUMPLEN EL AÑO ---")

# Recorremos el inventario una sola vez.
for equipo in inventario:

    # Comprobamos que esté disponible y que su año sea igual o posterior.
    if equipo["estado"] == "Disponible" and equipo["anio"] >= anio_minimo:

        # Mostramos los datos del equipo encontrado.
        print("\nNúmero de inventario:", equipo["inventario"])
        print("Tipo:", equipo["tipo"])
        print("Marca:", equipo["marca"])
        print("Estado:", equipo["estado"])
        print("Año:", equipo["anio"])

        # Aumentamos el contador.
        cantidad += 1

# Mostramos la cantidad total de resultados.
print("\nCantidad de equipos encontrados:", cantidad)

# Comprobamos si hubo resultados.
if cantidad == 0:
    print("No existen equipos disponibles que cumplan con ese año.")