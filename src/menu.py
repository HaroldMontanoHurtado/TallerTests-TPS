from models.ConnectionDB import consulta_total
from tabulate import tabulate

def existe_en_lista(hoja, filtro):
    #Chequear si el valor existe en la lista
    lista = consulta_total(hoja)
    return filtro in lista

def preguntar_opciones(text):
    
    while(True):
        eleccion = input(text)
        try: # intento volver numero el valor de entrada
            eleccion = int(eleccion)
        except:
            print('\nIngreso un valor no valido.')
        # pregunto si el valor es un numero
        if(isinstance(eleccion, int)):
            break
    
    return eleccion

def imprimir_hoja(table_hoja):
    table = consulta_total(table_hoja)
    encabezados = table.pop(0)
    print(tabulate(table, headers=encabezados))

def opc_bibliotecario(): 
    #Primero debe ingresar usuario
    texto = '''\n\t Bibliotecario
    Ingresa tu usuario: '''
    user = input(texto)
    
    imprimir_hoja('Usuarios')
    
    texto = '''\n\t\Bibliotecario
        Puedes gestionar los libros.
        (1) Consultar.
        (2) Agregar.
        (3) Eliminar.
        Digita el numero de tu tipo: '''

def menu():
    texto = '''\n\t\t Menu
    Bienvenido al gestor de biblioteca.
    Tipos de usuarios:
    (1) Bibliotecario.
    (2) Cliente.
    Digita el numero de tu tipo: '''
    
    eleccion = preguntar_opciones(text=texto)
    if(eleccion==1):
        opc_bibliotecario()
        pass
    elif(eleccion==2):
        pass
    else:
        print('Debe elegir un numero de las opciones')

menu()
'''
print(tabulate(
    [['Alice', 24], ['Bob', 19]],
    headers=['Name', 'Age']))'''
