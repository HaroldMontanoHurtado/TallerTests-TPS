from src.menu import funciones_bibliotecario
from src.models.ConnectionDB import agregar

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

def test_consultar():
    libros=consulta_total('Libros')
    libro=[['tituloX2', 'autorY2', 2, 0]]
    
    assert not libro in libros # si no existe entonces consultó correctamente
'''

def test_sum():
    assert sum([1,3]) == 4
