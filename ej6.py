# Creamos la clase que representa los dispositivos de red.
class DispositivoRed:

    # Constructor: inicializa los atributos de cada dispositivo.
    def __init__(self, codigo, tipo, marca, velocidad_mbps, precio, stock):

        self.codigo = codigo
        self.tipo = tipo
        self.marca = marca
        self.velocidad_mbps = velocidad_mbps
        self.precio = precio
        self.stock = stock

    # Método para mostrar todos los datos del dispositivo.
    def mostrar_datos(self):

        print("\nCódigo:", self.codigo)
        print("Tipo:", self.tipo)
        print("Marca:", self.marca)
        print("Velocidad:", self.velocidad_mbps, "Mbps")
        print("Precio: $", self.precio)
        print("Stock:", self.stock)

    # Método que devuelve True si hay stock y False si no hay.
    def hay_stock(self):

        if self.stock > 0:
            return True
        else:
            return False


# Creamos los objetos utilizando la clase DispositivoRed.
dispositivos = [

    DispositivoRed(101, "Router", "TP-Link", 1200, 45000, 5),

    DispositivoRed(102, "Switch", "D-Link", 1000, 35000, 3),

    DispositivoRed(103, "Access Point", "Ubiquiti", 2400, 85000, 2),

    DispositivoRed(104, "Router", "Tenda", 300, 20000, 0),

    DispositivoRed(105, "Switch", "TP-Link", 10000, 120000, 4),

    DispositivoRed(106, "Access Point", "MikroTik", 1200, 65000, 0)

]


# Función que filtra dispositivos por velocidad mínima.
def filtrar_por_velocidad(velocidad_minima):

    cantidad = 0

    print("\n--- DISPOSITIVOS POR VELOCIDAD ---")

    # Recorremos todos los dispositivos.
    for dispositivo in dispositivos:

        # Comprobamos la velocidad y la disponibilidad.
        if dispositivo.velocidad_mbps >= velocidad_minima and dispositivo.hay_stock():

            # Mostramos los datos del dispositivo.
            dispositivo.mostrar_datos()

            cantidad += 1

    # Si no encontramos resultados, mostramos un mensaje.
    if cantidad == 0:

        print("No existen dispositivos disponibles que cumplan esa velocidad.")


# Función que busca un dispositivo por su código.
def buscar_dispositivo(codigo):

    # Recorremos la lista de dispositivos.
    for dispositivo in dispositivos:

        # Comprobamos si el código coincide.
        if dispositivo.codigo == codigo:

            # Devolvemos el objeto encontrado.
            return dispositivo

    # Si no existe, devolvemos None.
    return None


# Función que filtra dispositivos según un presupuesto.
def filtrar_por_presupuesto(presupuesto):

    cantidad = 0

    print("\n--- DISPOSITIVOS DENTRO DEL PRESUPUESTO ---")

    # Recorremos los dispositivos.
    for dispositivo in dispositivos:

        # Comprobamos que tenga stock y no supere el presupuesto.
        if dispositivo.hay_stock() and dispositivo.precio <= presupuesto:

            dispositivo.mostrar_datos()

            cantidad += 1

    # Informamos si no hay resultados.
    if cantidad == 0:

        print("No existen dispositivos disponibles dentro de ese presupuesto.")


# Función para mostrar todos los dispositivos.
def mostrar_catalogo():

    print("\n--- CATÁLOGO COMPLETO ---")

    # Recorremos la lista y mostramos cada objeto.
    for dispositivo in dispositivos:

        dispositivo.mostrar_datos()


# Programa principal.

# Mostramos el catálogo completo.
mostrar_catalogo()


# Consultamos los dispositivos por velocidad.
velocidad = int(input("\nIngrese la velocidad mínima requerida en Mbps: "))

filtrar_por_velocidad(velocidad)


# Buscamos un dispositivo por su código.
codigo = int(input("\nIngrese el código del dispositivo que desea buscar: "))

resultado = buscar_dispositivo(codigo)

# Comprobamos si la búsqueda encontró un objeto.
if resultado != None:

    print("\n--- DISPOSITIVO ENCONTRADO ---")

    resultado.mostrar_datos()

else:

    print("No se encontró ningún dispositivo con ese código.")


# Consultamos los dispositivos según un presupuesto.
presupuesto = float(input("\nIngrese su presupuesto máximo: $"))

filtrar_por_presupuesto(presupuesto)