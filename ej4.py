# Lista de libros de la biblioteca.
libros = [
    {"isbn": "1001", "titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "disponible": True},
    {"isbn": "1002", "titulo": "Noches blancas", "autor": "Fiódor Dostoyevski", "disponible": True},
    {"isbn": "1003", "titulo": "1984", "autor": "George Orwell", "disponible": False},
    {"isbn": "1004", "titulo": "El extranjero", "autor": "Albert Camus", "disponible": True},
    {"isbn": "1005", "titulo": "Crimen y castigo", "autor": "Fiódor Dostoyevski", "disponible": False}
]

# Solicitamos el ISBN.
isbn_buscar = input("Ingrese el ISBN del libro: ")

# Esta es una versión intencionalmente incorrecta.
print("\n--- BÚSQUEDA INCORRECTA ---")

for libro in libros:

    if libro["isbn"] == isbn_buscar:

        print("Libro encontrado:", libro["titulo"])

    else:

        # ERROR: se muestra el mensaje por cada libro diferente.
        print("Libro no encontrado")