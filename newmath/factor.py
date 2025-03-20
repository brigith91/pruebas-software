

def multiplicador_factor(a: float, b: float, c: float) -> float:
    """
    Calcula un valor total basado en la multiplicación de cada uno de tres números por un factor
    específico, determinado según el rango en el que se encuentre cada número.

    Los factores asignados son:
        - Si el número es negativo (< 0): factor = -1
        - Si el número está en el rango [0, 10): factor = 2
        - Si el número está en el rango [10, 100): factor = 3
        - Si el número es mayor o igual a 100: factor = 4

    La función multiplica cada número por su respectivo factor y retorna la suma de todos los productos.

    Parámetros
    ----------
    a : int o float
        Primer número a evaluar.
    b : int o float
        Segundo número a evaluar.
    c : int o float
        Tercer número a evaluar.

    Retorna
    -------
    float
        Suma de los productos de cada número por su factor asignado.

    Ejemplos
    --------
    >>> multiplicar_numeros(5, -3, 15)
    58.0
    # Cálculo:
    #   5 está en [0,10)   => 5 * 2 = 10
    #  -3 es negativo     => -3 * (-1) = 3
    #  15 está en [10,100) => 15 * 3 = 45
    # Suma total = 10 + 3 + 45 = 58.0

    >>> multiplicar_numeros(8, 12, 150)
    8 * 2 + 12 * 3 + 150 * 4  # 16 + 36 + 600 = 652.0
    """
    def factor(num: float) -> int:
        if num < 0:
            return -1
        elif 0 <= num < 10:
            return 2
        elif 10 <= num < 100:
            return 3
        else:
            return 4

    return a * factor(a) + b * factor(b) + c * factor(c)


def factor_fibonacci(n: int, a: int = 0, b: int = 1) -> float:
    """
    Calcula recursivamente el n-ésimo número de Fibonacci, usando valores iniciales personalizados,
    y retorna el resultado de dividir ese número por n.

    La secuencia de Fibonacci se define de la siguiente manera:
        F(0) = a
        F(1) = b
        F(n) = F(n-1) + F(n-2) para n > 1

    Parámetros
    ----------
    n : int
        Posición de la secuencia que se desea calcular. Debe ser un entero positivo mayor que 0.
    a : int, opcional
        Valor inicial F(0) de la secuencia (por defecto es 0).
    b : int, opcional
        Valor inicial F(1) de la secuencia (por defecto es 1).

    Retorna
    -------
    float
        El valor de F(n) dividido por n, redondeado a dos decimales.

    Ejemplos
    --------
    >>> factor_fibonacci(5)
    1.0
    # Con los valores por defecto, la secuencia es: [0, 1, 1, 2, 3, 5]
    # F(5) = 5, y 5 / 5 = 1.0.

    >>> factor_fibonacci(6, 2, 3)
    5.67
    # Con a=2 y b=3, la secuencia es: [2, 3, 5, 8, 13, 21, 34]
    # F(6) = 34, y 34 / 6 ≈ 5.67.
    """
    def _fibonacci(k: int) -> int:
        if k == 0:
            return a
        elif k == 1:
            return b
        else:
            return _fibonacci(k - 1) + _fibonacci(k - 2)

    if n <= 0:
        raise ValueError("El valor de n debe ser mayor que 0.")

    resultado = _fibonacci(n) / n
    return round(resultado, 2)
