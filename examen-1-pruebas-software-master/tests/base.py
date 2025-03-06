from typing import Any

from rich.console import Console


console = Console()

def assert_equal(esperado: Any, resultado: Any, nombre_prueba: str) -> None:
    """
    Verifica la igualdad entre dos valores y muestra un mensaje en la consola indicando el resultado de la comparación.

    Esta función compara el valor "esperado" con el "resultado" obtenido. Si ambos valores son iguales,
    se imprime un mensaje de éxito en color verde, confirmando que la prueba fue satisfactoria. En caso
    de que los valores sean diferentes, se muestra un mensaje de error en color rojo que detalla tanto
    el valor esperado como el valor obtenido.

    Es útil para realizar pruebas unitarias o verificaciones rápidas en entornos interactivos, aprovechando
    la biblioteca Rich para resaltar visualmente los resultados en la terminal.

    Parámetros
    ----------
    esperado : Any
        El valor que se espera obtener en la prueba.
    resultado : Any
        El valor real obtenido, que se comparará con el valor esperado.
    nombre_prueba : str
        El nombre de la prueba que se esta evaluando.

    Retorna
    -------
    None
        La función no retorna ningún valor; su propósito es imprimir el resultado de la comparación en consola.

    Ejemplos
    --------
    >>> assert_equal(10, 10)
    [green]OK: Both values are equal.[/green]

    >>> assert_equal("hola", "adiós")
    [red]ERROR: Expected 'hola' but got 'adiós'.[/red]
    """
    try:
        assert esperado == resultado
        console.print(f"[green][bold]OK: [ {nombre_prueba} ][/bold][/green]")
    except AssertionError:
        console.print(f"[red][bold]ERROR: [{nombre_prueba}][/bold]\n\n  Valor Esperado:\n    {esperado!r}\n\n  Valor Obtenido:\n    {resultado!r}.[/red]")


