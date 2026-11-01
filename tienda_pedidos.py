"""
Sistema de Gestión de Pedidos de una Tienda
===========================================

Proyecto de Aula (ACA) - Algoritmos y Programación (54424)
Corporación Unificada Nacional de Educación Superior (CUN)
Autor: Martín Gracia Socha

Programa de consola que permite registrar productos (nombre y precio),
almacenarlos en una lista, mostrarlos y calcular el total de la compra
mediante una función recursiva.

Conceptos aplicados:
- Algoritmo: entradas (nombre y precio), proceso (validar, almacenar y
  sumar) y salidas (listado de productos y total).
- Estructuras de control: condicionales (if/elif/else) y ciclos (while, for).
- Estructura de datos: lista de diccionarios.
- Programación modular: una función por tarea.
- Recursividad: suma de precios con caso base y caso recursivo.
"""

import re

# ---------------------------------------------------------------------------
# Estructura de datos principal
# Cada producto es un diccionario: {"nombre": str, "precio": float}
# ---------------------------------------------------------------------------
productos = []


# ---------------------------------------------------------------------------
# Utilidades de presentación
# ---------------------------------------------------------------------------
def formato_pesos(valor):
    """Devuelve el valor con formato de pesos colombianos, p. ej. $12.500."""
    if valor == int(valor):
        texto = f"{valor:,.0f}"
    else:
        texto = f"{valor:,.2f}"
    # Python usa coma para miles y punto para decimales; en Colombia es al revés.
    texto = texto.replace(",", "_").replace(".", ",").replace("_", ".")
    return f"${texto}"


def linea(caracter="-", ancho=50):
    """Imprime una línea separadora."""
    print(caracter * ancho)


# ---------------------------------------------------------------------------
# Módulo 1: entrada y validación de datos
# ---------------------------------------------------------------------------
def convertir_precio(texto):
    """
    Convierte el texto escrito por el usuario en un número.
    Acepta formatos como 2500, 2.500, $2.500 o 2500,50.
    Devuelve None si el texto no es un precio válido.
    """
    limpio = texto.strip().replace("$", "").replace(" ", "")
    # "2.500" o "1.250.000": los puntos son separadores de miles.
    if re.fullmatch(r"\d{1,3}(\.\d{3})+(,\d+)?", limpio):
        limpio = limpio.replace(".", "")
    limpio = limpio.replace(",", ".")
    try:
        precio = float(limpio)
    except ValueError:
        return None
    if precio <= 0:
        return None
    return precio


def leer_nombre():
    """Pide el nombre del producto hasta que no esté vacío (ciclo while)."""
    while True:
        nombre = input("Nombre del producto: ").strip()
        if nombre:
            return nombre
        print("  El nombre no puede estar vacío. Intente de nuevo.")


def leer_precio():
    """Pide el precio hasta que sea un número mayor que cero (ciclo while)."""
    while True:
        precio = convertir_precio(input("Precio del producto: "))
        if precio is not None:
            return precio
        print("  Precio no válido. Escriba un número mayor que cero, p. ej. 2500.")


# ---------------------------------------------------------------------------
# Módulo 2: operaciones sobre la estructura de datos
# ---------------------------------------------------------------------------
def registrar_producto(lista, nombre, precio):
    """Crea el producto y lo agrega al final de la lista con append()."""
    producto = {"nombre": nombre, "precio": precio}
    lista.append(producto)
    return producto


def mostrar_productos(lista):
    """Recorre la lista con un ciclo for y muestra cada producto."""
    if len(lista) == 0:
        print("No hay productos registrados todavía.")
        return
    linea()
    print(f"{'N.º':<5}{'Producto':<28}{'Precio':>17}")
    linea()
    for numero, producto in enumerate(lista, start=1):
        print(f"{numero:<5}{producto['nombre']:<28}{formato_pesos(producto['precio']):>17}")
    linea()
    print(f"Productos registrados: {len(lista)}")


# ---------------------------------------------------------------------------
# Módulo 3: cálculo del total con recursividad
# ---------------------------------------------------------------------------
def calcular_total_recursivo(lista, indice=0):
    """
    Suma los precios de la lista de forma recursiva.

    Caso base: si el índice llegó al final de la lista, no quedan
    productos por sumar y la función devuelve 0.
    Caso recursivo: precio del producto actual + total del resto de la lista.

    Ejemplo con precios [2500, 4000, 1500]:
        total(0) = 2500 + total(1)
        total(1) = 4000 + total(2)
        total(2) = 1500 + total(3)
        total(3) = 0                      <- caso base
    Complejidad: O(n) en tiempo y O(n) en memoria (una llamada por producto).
    """
    if indice == len(lista):                       # caso base
        return 0
    return lista[indice]["precio"] + calcular_total_recursivo(lista, indice + 1)


def calcular_total_iterativo(lista):
    """Versión con ciclo for, usada solo para comprobar el resultado recursivo."""
    total = 0
    for producto in lista:
        total += producto["precio"]
    return total


def mostrar_traza_recursiva(lista, indice=0):
    """
    Hace el mismo cálculo que calcular_total_recursivo, pero imprime cada
    llamada (ida) y cada retorno (vuelta) para ver cómo funciona la recursión.
    """
    sangria = "   " * indice
    if indice == len(lista):
        print(f"{sangria}total({indice}) -> caso base: no quedan productos, devuelve $0")
        return 0
    precio = lista[indice]["precio"]
    print(f"{sangria}total({indice}) = {formato_pesos(precio)} "
          f"({lista[indice]['nombre']}) + total({indice + 1})")
    resto = mostrar_traza_recursiva(lista, indice + 1)
    resultado = precio + resto
    print(f"{sangria}total({indice}) devuelve {formato_pesos(precio)} + "
          f"{formato_pesos(resto)} = {formato_pesos(resultado)}")
    return resultado


# ---------------------------------------------------------------------------
# Módulo 4: menú e interacción con el usuario
# ---------------------------------------------------------------------------
def opcion_registrar(lista):
    """Opción 1 del menú: pide los datos y registra el producto."""
    print("\nREGISTRAR PRODUCTO")
    nombre = leer_nombre()
    precio = leer_precio()
    producto = registrar_producto(lista, nombre, precio)
    print(f"Producto registrado: {producto['nombre']} - {formato_pesos(producto['precio'])}")


def opcion_calcular_total(lista):
    """Opción 3 del menú: calcula el total de la compra con recursividad."""
    if len(lista) == 0:
        print("No hay productos registrados. El total es $0.")
        return
    total = calcular_total_recursivo(lista)
    print(f"\nTotal de la compra ({len(lista)} productos): {formato_pesos(total)}")


def opcion_traza(lista):
    """Opción 4 del menú: muestra paso a paso las llamadas recursivas."""
    if len(lista) == 0:
        print("Registre al menos un producto para ver la traza.")
        return
    print("\nTRAZA DE LA FUNCIÓN RECURSIVA")
    total = mostrar_traza_recursiva(lista)
    print(f"Resultado final: {formato_pesos(total)}")


def mostrar_menu():
    """Imprime las opciones disponibles."""
    print()
    linea("=")
    print("   TIENDA - SISTEMA DE GESTIÓN DE PEDIDOS")
    linea("=")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Calcular total de la compra")
    print("4. Ver cómo funciona la recursividad")
    print("5. Salir")
    linea("=")


def main():
    """Ciclo principal: repite el menú hasta que el usuario elija salir."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()
        if opcion == "1":
            opcion_registrar(productos)
        elif opcion == "2":
            mostrar_productos(productos)
        elif opcion == "3":
            opcion_calcular_total(productos)
        elif opcion == "4":
            opcion_traza(productos)
        elif opcion == "5":
            print("Gracias por usar el sistema. Hasta pronto.")
            break
        else:
            print("Opción no válida. Escriba un número del 1 al 5.")


if __name__ == "__main__":
    main()
