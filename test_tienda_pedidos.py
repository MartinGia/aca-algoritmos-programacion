"""Pruebas automáticas del sistema de pedidos. Ejecutar con: python test_tienda_pedidos.py"""

import unittest

from tienda_pedidos import (
    calcular_total_iterativo,
    calcular_total_recursivo,
    convertir_precio,
    formato_pesos,
    registrar_producto,
)


class PruebasTienda(unittest.TestCase):
    def test_lista_vacia_es_caso_base(self):
        self.assertEqual(calcular_total_recursivo([]), 0)

    def test_registrar_agrega_al_final(self):
        lista = []
        registrar_producto(lista, "Arroz", 4200)
        registrar_producto(lista, "Leche", 3800)
        self.assertEqual(len(lista), 2)
        self.assertEqual(lista[-1], {"nombre": "Leche", "precio": 3800})

    def test_recursivo_igual_a_iterativo(self):
        lista = []
        for nombre, precio in [("Arroz", 4200), ("Leche", 3800), ("Pan", 2500), ("Huevos", 14900)]:
            registrar_producto(lista, nombre, precio)
        self.assertEqual(calcular_total_recursivo(lista), 25400)
        self.assertEqual(calcular_total_recursivo(lista), calcular_total_iterativo(lista))

    def test_convertir_precio(self):
        self.assertEqual(convertir_precio("2500"), 2500)
        self.assertEqual(convertir_precio("$2.500"), 2500)
        self.assertEqual(convertir_precio("1.250.000"), 1250000)
        self.assertEqual(convertir_precio("2500,50"), 2500.5)
        self.assertIsNone(convertir_precio("abc"))
        self.assertIsNone(convertir_precio("-300"))
        self.assertIsNone(convertir_precio("0"))

    def test_formato_pesos(self):
        self.assertEqual(formato_pesos(25400), "$25.400")
        self.assertEqual(formato_pesos(1250000), "$1.250.000")
        self.assertEqual(formato_pesos(2500.5), "$2.500,50")


if __name__ == "__main__":
    unittest.main(verbosity=2)
