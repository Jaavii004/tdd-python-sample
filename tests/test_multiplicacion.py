# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import multiplicacion

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación multiplicacion
    def test_multiplicacion(self):
        assert multiplicacion(4,5) == 20
        assert multiplicacion(-7,9) == -63
        assert multiplicacion(0,9) == 0
        assert multiplicacion(0,0) == 0
