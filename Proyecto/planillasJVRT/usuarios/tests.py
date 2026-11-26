import pytest

from .models import usuario


@pytest.mark.parametrize(
    "nombre, apellido, correo, contraseña, contraseña_confirmada, resultado",
    [
        ("Todos", "los","campos","tienen","valor", True),
        ("", "falta","un","unico","campo", False),
        (" ", "falta","un","unico","campo", False),
        ("falta", "","un","campo","en otro lugar", False),
        ("falta", "un","","campo","en otro lugar", False),
        ("falta", "un","campo","","en otro lugar", False),
        ("falta", "un","campo","en otro lugar","", False),
        ("", "","","","", False),
        ("", "","falta","mas de un","campo", False),
        ("", "falta mas de un","","campo","", False),
        (" ", "falta mas de un"," ","campo","", False),
    ]
)

def test_verificar_registro_campos_obligatorios(nombre, apellido, correo, contraseña, contraseña_confirmada, resultado):
    assert validar_obligatoriedad([nombre, apellido, correo, contraseña, contraseña_confirmada]) == resultado
