from tests.base import assert_equal

from newmath.factor import multiplicador_factor, factor_fibonacci


def test_deberia_validar_un_numero_negativo():
    restultado:float = 58.0
    esperado: float = multiplicador_factor(5, -3, 15)
    assert_equal(esperado, restultado, "test_deberia_validar_un_numero_negativo")
    
def test_deberia_validar_si_el_numero_negativo_cambia_resultado():
    restultado: int = multiplicador_factor(-3, 2, 15)
    esperado: float = 52.0
    assert_equal(esperado, restultado, "test_deberia_validarsi_el_numero_negativo_cambia_resultado")
    
def test_deberia_validar_si_el_numero_aplica_al_rango_3():
    restultado: int = multiplicador_factor(-3, 101, 15)
    esperado:float = 452.0
    assert_equal(esperado, restultado, "test_deberia_validar_si_el_numero_aplica_al_rango_3")
    

def test_deberia_validar_la_posicion_4_de_fibonacci_iniciando_desde_0():
    restultado: int = factor_fibonacci(4)
    esperado: float = 0.75
    assert_equal(esperado, restultado, "test_deberia_validar_la_posicion_4_de_fibonacci_iniciando_desde_0")
    
def test_deberia_validar_la_posicion_3_de_fibonacci_iniciando_desde_3_y_5():
    restultado: int = factor_fibonacci(3,5)
    esperado: float = 2.33
    assert_equal(esperado, restultado, "test_deberia_validar_la_posicion_3_de_fibonacci_iniciando_desde_3_y_5():")