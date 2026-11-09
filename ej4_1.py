# Variable que indica si encontramos el libro.
encontrado = False

print("\n--- BÚSQUEDA CORREGIDA ---")

# Recorremos los libros.
for libro in libros:

    # Comprobamos si el ISBN coincide.
    if libro["isbn"] == isbn_buscar:

        # Indicamos que encontramos el libro.
        encontrado = True

        # Mostramos todos sus datos.
        print("\nISBN:", libro["isbn"])
        print("Título:", libro["titulo"])
        print("Autor:", libro["autor"])
        print("Disponible:", libro["disponible"])

        # Detenemos el recorrido porque ya encontramos el registro.
        break

# Este if se ejecuta después de terminar la búsqueda.
if encontrado == False:

    print("Libro no encontrado")