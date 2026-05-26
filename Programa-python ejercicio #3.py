
# Descripción:
# Este programa permite auditar el inventario de una empresa de tecnologia y determinar qué artículos necesitan ser reabastecidos.

# La información se almacena en una matriz con:
# [Código, Nombre del Artículo, Stock Actual, Stock Mínimo]
#
# Reglas de negocio:
# - Si el stock actual es menor al stock mínimo,
#   se calcula la cantidad exacta a pedir.
# - Si el stock actual es suficiente,
#   no se realiza pedido.
# ---------------------------------------------------------


# MATRIZ DE INVENTARIO

# [Código, Nombre, Stock Actual, Stock Mínimo Requerido]

inventario = [
    [1001, "Teclado Gamer", 5, 15],
    [1002, "Mouse Inalámbrico", 15, 15],
    [1003, "Monitor LED 32 pulgadas", 20, 15],
    [1004, "Silla Gamer", 7, 10],
    [1005, "Auriculares Bluetooth", 10, 30]
]


# Función para calcular la cantidad exacta a pedir

def calcular_pedido(stock_actual, stock_minimo):
    """
    Calcula la cantidad exacta que debe solicitarse
    para reabastecer un artículo.
    """

    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0

    return cantidad



print("......................................")
print(" SISTEMA DE AUDITORÍA DE INVENTARIO")
print("......................................")



print("INVENTARIO ACTUAL\n")

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    print(f"Código: {codigo}")
    print(f"Artículo: {nombre}")
    print(f"Stock Actual: {stock_actual}")
    print(f"Stock Mínimo Requerido: {stock_minimo}")
    print("--------------------------------------")


print("......................................")
print("  LISTA DE REABASTECIMIENTO")
print("......................................")


for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    # Llamado al módulo
    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    # Verificación del stock
    if cantidad_pedir > 0:

        print(f"Artículo: {nombre}")
        print(f"Código: {codigo}")
        print(f"Stock Actual: {stock_actual}")
        print(f"Stock Mínimo Requerido: {stock_minimo}")
        print(f"Cantidad Exacta a Pedir: {cantidad_pedir}")
        print("Estado: REQUIERE REABASTECIMIENTO")
        print("--------------------------------------")

    else:

        print(f"Artículo: {nombre}")
        print(f"Código: {codigo}")
        print("Cantidad Exacta a Pedir: 0")
        print("Estado: STOCK SUFICIENTE")
        print("--------------------------------------")



print("\nAuditoría de inventario finalizada correctamente.")