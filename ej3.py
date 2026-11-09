# Lista de alumnos con sus respectivos datos.
alumnos = [
    {"nombre": "Juan", "curso": "4°3°", "promedio": 8.5, "trabajos": 8},
    {"nombre": "Martina", "curso": "4°3°", "promedio": 9.2, "trabajos": 10},
    {"nombre": "Lucas", "curso": "4°3°", "promedio": 6.5, "trabajos": 7},
    {"nombre": "Sofia", "curso": "4°3°", "promedio": 7.8, "trabajos": 9},
    {"nombre": "Mateo", "curso": "4°3°", "promedio": 9.8, "trabajos": 10},
    {"nombre": "Camila", "curso": "4°3°", "promedio": 5.5, "trabajos": 6},
    {"nombre": "Pedro", "curso": "4°3°", "promedio": 8.9, "trabajos": 9},
    {"nombre": "Valentina", "curso": "4°3°", "promedio": 7.0, "trabajos": 8},
    {"nombre": "Tomas", "curso": "4°3°", "promedio": 9.5, "trabajos": 7},
    {"nombre": "Lucia", "curso": "4°3°", "promedio": 6.8, "trabajos": 10}
]

# Solicitamos los criterios mínimos.
promedio_minimo = float(input("Ingrese el promedio mínimo requerido: "))
trabajos_minimos = int(input("Ingrese la cantidad mínima de trabajos entregados: "))

# Contadores.
cumplen = 0
no_cumplen = 0

# Variable auxiliar para guardar al mejor alumno.
mejor_alumno = None

print("\n--- ALUMNOS QUE CUMPLEN LOS CRITERIOS ---")

# Recorremos la lista de alumnos.
for alumno in alumnos:

    # Comprobamos que cumpla ambas condiciones.
    if alumno["promedio"] >= promedio_minimo and alumno["trabajos"] >= trabajos_minimos:

        print("\nNombre:", alumno["nombre"])
        print("Promedio:", alumno["promedio"])
        print("Trabajos entregados:", alumno["trabajos"])

        # Contamos los alumnos que cumplen.
        cumplen += 1

        # Comprobamos si es el alumno con mayor promedio.
        if mejor_alumno is None or alumno["promedio"] > mejor_alumno["promedio"]:

            # Guardamos el alumno con el promedio más alto.
            mejor_alumno = alumno

    else:

        # Contamos los alumnos que no cumplen.
        no_cumplen += 1

# Mostramos las cantidades finales.
print("\n--- RESUMEN ---")
print("Alumnos que cumplen:", cumplen)
print("Alumnos que no cumplen:", no_cumplen)

# Comprobamos si existen alumnos que cumplen.
if cumplen > 0:

    print("\n--- MEJOR PROMEDIO ---")
    print("Nombre:", mejor_alumno["nombre"])
    print("Promedio:", mejor_alumno["promedio"])

else:
    print("\nNingún alumno cumple con los criterios solicitados.")