import pytest
from src.models.ConnectionDB import agregar, eliminar, consultar_libro, consultar_tablas, existe_en_tabla, hallar_fila, hojas_google_sheet
# El pytest busca y reconoce los archivos y funciones que empiecen por 'test_'

# Tests de REGISTRO de libros y usuarios
@pytest.mark.parametrize(
    "sheet, objeto, expected",
    [
        ('Libros', [['titulo1', 'autor1', '23']], True),
        ('Usuarios', [['Jaime Altozano', 'Bibliotecario']], True),
        ('Usuarios', [['Migala', 'Cliente']], True),
        ('Libros', [['El alquimista', 'Paulo Coelho']], True),
        ('Usuarios', [['Fabio Duarte', 'Bibliotecario']], True),
        ('Usuarios', [['Joe Arroyo', 'Cliente']], True)
    ]
)
def test_agregar(sheet, objeto, expected):
    # primero se agregan:
    agregar(sheet, objeto)
    # almaceno el comprobante de existencia del agregado
    result=existe_en_tabla(objeto[0][0], sheet)
    # luego se podria eliminar, para no alterar la tabla
    #eliminar(hallar_fila(objeto[0], sheet), hojas_google_sheet[sheet])
    assert result == expected

# Tests de CONSULTAS
@pytest.mark.parametrize(
    "searched, expected",
    [
        ('odisea', True), ('gabriel', True), ('x', True),
        ('tituloX', False), ('dam', False), ('loco', False)
    ]
)
def test_consultar_libros(searched, expected):
    assert (not consultar_libro(searched) == []) == expected

