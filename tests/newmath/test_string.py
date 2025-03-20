import unittest
from newmath.string import contar_vocales,multiplicacion_vocales,porcentaje_vocales
#python -m unittest tests/newmath/test_string_unittest.py -v para correr en consola

class TestContarVocales(unittest.TestCase):

    @unittest.skip(reason='Por razones de clase')

    def test_deberia_contar_vocales(self):
        resultado = contar_vocales("Hola, cómo estás?")
        esperado = 7
        self.assert_equal(esperado, resultado, "test_contar_vocales_1")
    
        resultado = contar_vocales("AEIOUaeiouÁÉÍÓÚáéíóú")
        esperado = 20
        self.assert_equal(esperado, resultado, "test_contar_vocales_2")
    
        resultado = contar_vocales("xyz")
        esperado = 0
        self.assert_equal(esperado, resultado, "test_contar_vocales_3")

    def test_deberia_hacer_una_multiplicacion_de_vocales(self):
        resultado = multiplicacion_vocales("aeiou")
        esperado = 9
        self.assert_equal(esperado, resultado, "test_multiplicacion_vocales_1")
    
        resultado = multiplicacion_vocales("Un murcielago")
        esperado = 9
        self.assert_equal(esperado, resultado, "test_multiplicacion_vocales_2")
    
        resultado = multiplicacion_vocales("xyz")
        esperado = 0
        self.assert_equal(esperado, resultado, "test_multiplicacion_vocales_3")

    def test_deberia_realizar_el_porcentaje_de_vocales(self):
        resultado = porcentaje_vocales("Hola, cómo estás?")
        esperado = 46.15
        self.assert_equal(esperado, resultado, "test_porcentaje_vocales_1")
    
        resultado = porcentaje_vocales("Python")
        esperado = 33.33
        self.assert_equal(esperado, resultado, "test_porcentaje_vocales_2")
    
        resultado = porcentaje_vocales("12345!")
        esperado = 0.0
        self.assert_equal(esperado, resultado, "test_porcentaje_vocales_3")



#class TestFunciones(unittest.TestCase):
#    def test_contar_vocales(self):
#        self.assertEqual(contar_vocales("Hola, cómo estás?"), 7)
#        self.assertEqual(contar_vocales("AEIOUaeiouÁÉÍÓÚáéíóú"), 20)
#        self.assertEqual(contar_vocales("xyz"), 0)

unittest.main()