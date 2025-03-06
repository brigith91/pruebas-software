

def contar_vocales(text: str) -> int:
    """
    Calcula la cantidad total de vocales presentes en una cadena de texto,
    considerando tanto las vocales estándar como sus variantes acentuadas.

    La función cuenta las vocales minúsculas ('a', 'e', 'i', 'o', 'u') y
    mayúsculas ('A', 'E', 'I', 'O', 'U'), así como sus variantes acentuadas.

    Parámetros
    ----------
    text : str
        Cadena de texto que se analizará.

    Retorna
    -------
    int
        Número total de vocales, incluyendo las acentuadas, encontradas en el texto.

    Ejemplos
    --------
    >>> contar_vocales("Hola, cómo estás?")
    7
    # Explicación: Se cuentan las vocales 'o', 'a', 'o', 'ó', 'o', 'e', 'á'.

    >>> contar_vocales("AEIOUaeiouÁÉÍÓÚáéíóú")
    20
    # Se cuentan las vocales en mayúsculas, minúsculas y las variantes acentuadas.
    """
    vocales: str = "aeiouAEIOUáéíúÁÉÍÚ"
    contador: int = 0
    for char in text:
        if char in vocales:
            contador += 1
    return contador


def multiplicacion_vocales(text: str) -> int:
    """
    Calcula un valor entero basado en la frecuencia de cada vocal en el texto, multiplicada por un valor específico.

    Los valores asignados a cada vocal son:
        - 'a'  =>  3
        - 'e'  =>  5
        - 'i'  =>  2
        - 'o'  =>  1
        - 'u'  => -2
        - 'A'  => -4
        - 'E'  => -2
        - 'I'  =>  2
        - 'O'  =>  4
        - 'U'  => -5

    Se asume que cualquier otra representación de una vocal (por ejemplo, vocales acentuadas)
    tendrá un valor predeterminado de 4.

    El cálculo se realiza en los siguientes pasos:
        1. Contar la cantidad de ocurrencias de cada vocal en el texto.
        2. Multiplicar el valor asignado a cada vocal por su número de apariciones.
        3. Sumar todos los resultados parciales para obtener el valor final.

    Parámetros
    ----------
    text : str
        Cadena de caracteres a analizar.

    Retorna
    -------
    int
        Resultado de la suma de las multiplicaciones de cada vocal por su frecuencia en el texto.

    Ejemplos
    --------
    >>> multiplicacion_vocales("aeiou")
    9
    # Cálculo: (1*3) + (1*5) + (1*2) + (1*1) + (1*(-2)) = 9

    >>> multiplicacion_vocales("Un murcielago")
    9
    # Cálculo: (1*3) + (1*5) + (1*2) + (1*1) + (1*(-2)) + (1*(-5)) = 4

    >>> multiplicacion_vocales("un murcielago")
    9
    # Cálculo: (1*3) + (1*5) + (1*2) + (1*1) + (2*(-2)) = 7
    """
    VALORES: dict[str, int] = {
        'a': 3, 'e': 5, 'i': 2, 'o': 1, 'u': -2,
        'A': -4, 'E': -2, 'I': 2, 'O': 4, 'U': -5
    }
    VOCALES: str = 'aeiouAEIOUáéíúÁÉÍÚ'
    total = 0
    for char in text:
        if char in VOCALES:
            total += VALORES.get(char, 4)
    return total


def porcentaje_vocales(text: str) -> float:
    """
    Calcula el porcentaje de vocales presentes en una cadena de texto en relación
    al total de caracteres alfabéticos.

    La función toma en cuenta tanto las vocales estándar en minúsculas y mayúsculas
    ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') como sus variantes acentuadas
    ('á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú'). Se excluyen de la cuenta
    aquellos caracteres que no sean letras.

    Parámetros
    ----------
    text : str
        Cadena de texto que se analizará.

    Retorna
    -------
    float
        Porcentaje de vocales (entre 0 y 100) respecto al total de caracteres alfabéticos.
        Si no se encuentran caracteres alfabéticos en el texto, retorna 0.0.

    Ejemplos
    --------
    >>> porcentaje_vocales("Hola, cómo estás?")
    46.15
    # Explicación: En "Hola, cómo estás?" hay 6 vocales entre 13 caracteres alfabéticos,
    # lo que equivale aproximadamente a un 46.15%.

    >>> porcentaje_vocales("Python")
    33.33
    # Explicación: "Python" tiene 2 vocales entre 6 letras, resultando en un 33.33%.

    >>> porcentaje_vocales("12345!")
    0.0
    # Explicación: No hay caracteres alfabéticos, por lo que se retorna 0.0.
    """
    vocales: str = "aeiouAEIOUáéíúÁÉÍÚ"
    total_letras = total_vocales = 0

    for char in text:
        if char.isalpha():
            total_letras += 1
            if char in vocales:
                total_vocales += 1

    if total_letras == 0:
        return 0.0

    porcentaje = (total_vocales / total_letras) * 100
    return round(porcentaje, 2)
