import unittest
import pytest 
from newmath.string import contar_vocales,multiplicacion_vocales,porcentaje_vocales
#python -m unittest tests/newmath/test_string.py -v para correr en consola
# instalar biblioteca  pytest pip install pytest en consola ejecutar pytest
# comandos pytest -h
# informe html pip install pytest-html
#  pytest tests/newmath/test_string.py --html=reporttchfgh.html
# navegador live server extension , correr en go live
# decorador @pytest.mark.parametrize = arriba de la funcion para que autocomplete con los parametros ingresados pasar parametros a las funciones
# informe pytest --html=reporte_sexy.html llamar informe en consola

class TestContarVocales(unittest.TestCase):

    #@unittest.skip(reason='Por razones de clase')
    # python -m unittest discover -v -s tests -p "tests_ " * .py

   
    def test_contar_vocales_texto_normal(self):
        """Prueba contar vocales en un texto común"""
        resultado = contar_vocales(text="hola")
        esperado = 2
        self.assertEqual(first=resultado, second=esperado)

    @pytest.mark.skip("A la espera de implementacion de HU DATA 3354")
    @pytest.mark.parametrize(
         "texto , numero_esperado, mensaje",
         [
             ("hola", 12, "Deberia ser 2"),
             ("murcielago", 5 "soy batman")
   
         ]
           
    )
    def test_contar_vocales_sin_vocales(texto , numero_esperado, mensaje):
        """Prueba contar vocales en un texto sin vocales"""
        assert contar_vocales(text=texto) == numero_esperado, mensaje

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

    
