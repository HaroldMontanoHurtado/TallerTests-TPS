import pytest
from src.models.ConnectionDB import agregar, consultar_libro

'''
El pytest busca y reconoce los archivos y funciones que empiecen por 'test_'
'''

'''
def test_agregar_libros():
    #agregamos un libro
    libro=[]
    libro.append(['tituloX', 'autorY', 7, 0])
    agregar('Libros', libro)
    #consultamos si el libro existe o no
    libros=consulta_total('Libros')
    
    assert libro in libros # si existe entonces se agregó correctamente
'''

@pytest.mark.parametrize(
    "searched, expected",
    [
        ('odisea', True), ('gabriel', True), ('x', True),
        ('titulo', False), ('dam', False), ('loco', False)
    ]
)
def test_consultar_libro(searched, expected):
    assert (not consultar_libro(searched) == []) == expected

