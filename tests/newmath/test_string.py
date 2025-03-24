import unittest
from newmath.string import contar_vocales,multiplicacion_vocales,porcentaje_vocales
#python -m unittest tests/newmath/test_string.py -v para correr en consola

class TestContarVocales(unittest.TestCase):

    #@unittest.skip(reason='Por razones de clase')


    
    #  Pruebas para contar_vocales
    def test_contar_vocales_texto_normal(self):
        """Prueba contar vocales en un texto común"""
        resultado = contar_vocales(text="hola")
        esperado = 2
        self.assertEqual(first=resultado, second=esperado)

    def test_contar_vocales_sin_vocales(self):
        """Prueba contar vocales en un texto sin vocales"""
        resultado = contar_vocales(text="bcdfgh")
        esperado = 0
        self.assertEqual(first=resultado, second=esperado)

    def test_contar_vocales_mayusculas(self):
        """Prueba contar vocales en mayúsculas"""
        resultado = contar_vocales(text="HOLA")
        esperado = 2
        self.assertEqual(first=resultado, second=esperado)

    def test_contar_vocales_acentuadas(self):
        """Prueba contar vocales con tildes"""
        resultado = contar_vocales(text="ÁÉÍÓÚ")
        esperado = 5
        self.assertEqual(first=resultado, second=esperado)

    #  Pruebas para multiplicacion_vocales
    def test_multiplicacion_vocales_texto_normal(self):
        """Prueba multiplicación de vocales en un texto común"""
        resultado = multiplicacion_vocales(text="hola")
        esperado = 4
        self.assertEqual(first=resultado, second=esperado)

    def test_multiplicacion_vocales_sin_vocales(self):
        """Prueba multiplicación de vocales sin vocales"""
        resultado = multiplicacion_vocales(text="xyz")
        esperado = 0
        self.assertEqual(first=resultado, second=esperado)

    def test_multiplicacion_vocales_mayusculas(self):
        """Prueba multiplicación de vocales con mayúsculas"""
        resultado = multiplicacion_vocales(text="HOLA")
        esperado = 2
        self.assertEqual(first=resultado, second=esperado)

    def test_multiplicacion_vocales_acentuadas(self):
        """Prueba multiplicación de vocales con tildes"""
        resultado = multiplicacion_vocales(text="ÁÉÍÓÚ")
        esperado = 10
        self.assertEqual(first=resultado, second=esperado)

    #  Pruebas para porcentaje_vocales
    def test_porcentaje_vocales_texto_normal(self):
        """Prueba porcentaje de vocales en un texto común"""
        resultado = porcentaje_vocales(text="hola")
        esperado = 50.0
        self.assertEqual(first=resultado, second=esperado)

    def test_porcentaje_vocales_sin_vocales(self):
        """Prueba porcentaje de vocales sin vocales"""
        resultado = porcentaje_vocales(text="xyz")
        esperado = 0.0
        self.assertEqual(first=resultado, second=esperado)

    def test_porcentaje_vocales_mayusculas(self):
        """Prueba porcentaje de vocales con mayúsculas"""
        resultado = porcentaje_vocales(text="HOLA")
        esperado = 50.0
        self.assertEqual(first=resultado, second=esperado)

    def test_porcentaje_vocales_acentuadas(self):
        """Prueba porcentaje de vocales con tildes"""
        resultado = porcentaje_vocales(text="ÁÉÍÓÚ")
        esperado = 100.0
        self.assertEqual(first=resultado, second=esperado)

if __name__ == '__main__':
    unittest.main()

    
