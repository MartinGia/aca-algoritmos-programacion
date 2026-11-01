# Sistema de Gestión de Pedidos de una Tienda

Proyecto de Aula (ACA) de **Algoritmos y Programación (54424)**, Ingeniería de Software, Corporación Unificada Nacional de Educación Superior (CUN).

- **Estudiante:** Martín Gracia Socha
- **Docente:** Juan Esteban Caicedo Palacio
- **Lenguaje:** Python 3 (sin librerías externas)

## Problema

En una tienda pequeña los pedidos se anotan a mano y el total se suma con calculadora, lo que produce errores de cálculo, productos olvidados y demoras al cobrar.

## Objetivo general

Desarrollar un programa de consola en Python que permita registrar los productos de un pedido (nombre y precio), almacenarlos en una lista, mostrarlos y calcular el total de la compra mediante una función recursiva.

## Cómo se cumple cada punto del ACA

| Punto | Dónde está en el código |
|---|---|
| 1. Sistema y objetivo | Este README y el encabezado de `tienda_pedidos.py` |
| 2. Algoritmo (entradas, proceso, salidas) con condicionales y ciclos | `main()`, `leer_nombre()`, `leer_precio()` |
| 3. Estructura de datos (lista): agregar y recorrer | `productos = []`, `registrar_producto()` (append), `mostrar_productos()` (for) |
| 4. Organización en funciones | Cuatro módulos: entrada y validación, operaciones sobre la lista, recursividad y menú |
| 5. Función recursiva para el total | `calcular_total_recursivo()` y su traza `mostrar_traza_recursiva()` |
| 6. Menú en consola | `mostrar_menu()` y `main()` |

## Ejecución

**En el computador:**

```bash
python tienda_pedidos.py        # abre el menú
python test_tienda_pedidos.py   # ejecuta las pruebas automáticas
```

**En Google Colab:** abra `ACA_Algoritmos_y_Programacion.ipynb` y elija *Entorno de ejecución > Ejecutar todas*. La última celda abre el menú interactivo.

## Menú

```
==================================================
   TIENDA - SISTEMA DE GESTIÓN DE PEDIDOS
==================================================
1. Registrar producto
2. Mostrar productos
3. Calcular total de la compra
4. Ver cómo funciona la recursividad
5. Salir
==================================================
```

## La función recursiva

```python
def calcular_total_recursivo(lista, indice=0):
    if indice == len(lista):                       # caso base
        return 0
    return lista[indice]["precio"] + calcular_total_recursivo(lista, indice + 1)
```

- **Caso base:** cuando el índice llega al final de la lista no quedan productos y se devuelve 0.
- **Caso recursivo:** el precio del producto actual más el total del resto de la lista.
- **Complejidad:** O(n) en tiempo y en memoria (una llamada por producto).

## Archivos

| Archivo | Contenido |
|---|---|
| `tienda_pedidos.py` | Programa principal |
| `test_tienda_pedidos.py` | Pruebas automáticas (unittest) |
| `ACA_Algoritmos_y_Programacion.ipynb` | Cuaderno para Google Colab con explicación por secciones |
