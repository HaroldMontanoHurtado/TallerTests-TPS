from models.ConnectionDB import consulta_total
from tabulate import tabulate
from re import compile, IGNORECASE

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

def verificar_existe_user(user, tipo_user):
    table = consulta_total('Usuarios')
    table.pop(0) #elimino los encabezados
    #print(([user, tipo_user] in table))
    return ([user, tipo_user] in table)

def existe_coincidencia(lista, valor):
    # Compila una expresión regular que coincide con el valor en cualquier parte de la cadena,
    patron = compile(valor, IGNORECASE) # sin tener en cuenta mayúsculas y minúsculas
    # Busca el valor en la lista
    coincidencias = [x for x in lista if patron.search(x)]
    
    return not coincidencias==[] # Pregunta si existe alguna coincidencia

def consultar_libros():
    texto = '\n\t**Consulta libro**\nDigita el titulo o el autor del\nlibro: '
    
    busqueda = input(texto)
    libros = consulta_total('Libros')
    encabezados = libros.pop(0)
    coincidencias=[]
    for libro in libros:
        if existe_coincidencia(libro, busqueda):
            coincidencias.append(libro)
            
    if not coincidencias==[]:
        print('\n', tabulate(coincidencias, encabezados))
    else:
        print('Libro NO encontrado')

# aun falta configurar las funciones de gestionar_libros()
def opc_bibliotecario(): 
    #Primero debe ingresar usuario
    texto = '\n\t**Bibliotecario**\nIngresa tu usuario o \'atras\'para regresar\nal menu: '
    #sub-funcion de opc_bibliotecario()
    def gestionar_libros():
        #sub-funciones de gestionar_libros()
        def agregar_libros():
            pass
        def elimininar_libros():
            pass
        
        while True:
            texto = '\n\t**Bibliotecario**\nPuedes gestionar los libros.\n(1) Consultar libro.\n(2) Agregar libro.\n(3) Eliminar libro.\n(4) Regresar al menu.\nDigita el numero de las opciones: '
            eleccion = preguntar_opciones(text=texto)
            if eleccion==1:
                consultar_libros()
            elif eleccion==2:
                agregar_libros()
            elif eleccion==3:
                elimininar_libros()
            elif eleccion==4:
                break
    
    while True:
        respuesta = input(texto)
        if verificar_existe_user(respuesta, 'Bibliotecario'):
            gestionar_libros()
            break
        elif (respuesta == 'atras'):
            break
        else:
            print('-X- Usuario erroneo, prueba de nuevo. -X-')

# aun falta configurar las funciones de funciones_cliente()
def opc_cliente(): 
    #Primero debe ingresar usuario
    texto = '\n\t**Cliente**\nIngresa tu usuario o \'atras\' para regresar: '
    #sub-funcion de opc_cliente()
    def funciones_cliente():
        #sub-funciones de funciones_cliente()
        def prestar_libros():
            pass
        def devolver_libros():
            pass
        
        while True:
            texto = '\n\t**Cliente**\nBienvenido cliente.\n(1) Consultar libro.\n(2) Prestar libro.\n(3) Devolver libro.\n(4) Regresar al menu.\nDigita el numero de tu peticion: '
            eleccion = preguntar_opciones(text=texto)
            if eleccion==1:
                consultar_libros()
            elif eleccion==2:
                prestar_libros()
            elif eleccion==3:
                devolver_libros()
            elif eleccion==4:
                break
    
    while True:
        respuesta = input(texto)
        if verificar_existe_user(respuesta, 'Cliente'):
            funciones_cliente()
            break
        elif (respuesta == 'atras'):
            break
        else:
            print('-X- Usuario erroneo, prueba de nuevo. -X-')

def menu():
    try:
        while True:
            texto = '\n\t\t**Menu**\nBienvenido al gestor de biblioteca.\nTipos de usuarios:\n(1) Bibliotecario.\n(2) Cliente.\n(3) Salir.\nDigita el numero de tu tipo: '
            
            eleccion = preguntar_opciones(text=texto)
            if(eleccion==1):
                opc_bibliotecario()
            elif(eleccion==2):
                opc_cliente()
            elif(eleccion==3):
                #exit() # se finaliza la ejecucion
                break # break no dispara la bandera del except
            else:
                print('Debe elegir un numero de las opciones')
    except:
        print('Fallo en el menu')

menu()

