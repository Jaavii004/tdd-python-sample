# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import division

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación division
    def test_division(self):
        assert division(4,2) == 2
        assert division(-7,5) == -1.4
        assert division(0,9) == 0
        assert division(0,0) == "No se puede dividir por cero"