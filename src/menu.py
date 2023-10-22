from models.ConnectionDB import consulta_total, agregar, eliminar, modificar
from tabulate import tabulate
from re import compile, IGNORECASE

hojas_google_sheet={
    'Usuarios':'0', 'Libros':'2102902917',
    'Prestamos':'2023029017', 'pruebas':'423776484'}
#print(hojas_google_sheet['pruebas']) #return -> '423776484'

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

# no se ha usado
def existe_en_tabla(key, type_table):
    tabla=consulta_total(type_table)
    objeto=[]
    
    for fila in tabla:
        if key in fila:
            objeto.append(fila)
    
    return not objeto==[]

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
    libros_coincidentes=[]
    
    for libro in libros:
        if existe_coincidencia(libro, busqueda):
            libros_coincidentes.append(libro)
    # todo libro con coincidencias se agrega
    if not libros_coincidentes==[]:
        print()
        print(tabulate(libros_coincidentes, encabezados))
    else:
        print('-xXx- Libro NO encontrado -xXx-')

def funciones_bibliotecario():
    # funciones de gestion de los libros
    def agregar_libros():
        libro=[]
        
        texto='\n\t**Bibliotecario**\nVamos a agregar el libro en tres pasos.\nPrimero ingresa el titulo del libro: '
        dato=input(texto)
        libro.append(dato) # add titulo del libro
        
        texto='\n\t**Bibliotecario**\nAhora vamos a agregar el nombre del autor: '
        dato=input(texto)
        libro.append(dato) # add nombre del autor
        
        texto='\n\t**Bibliotecario**\nPor ultimo vamos a agregar la cantidad de libros nuevos: '
        dato=input(texto)
        libro.append(dato) # add cantidad de libros añadidos
        
        libro.append(0) # add cantidad de libros prestados
        
        agregar('Libros', [libro])
    
    def eliminar_libros():
        texto = '\n\t**Bibliotecario**\nVamos a eliminar un libro.\nDigita el titulo exacto del libro: '
        busqueda = input(texto)
        libros = consulta_total('Libros')
        encabezados = libros.pop(0)
        fila=1
        eliminado=[]
        
        for libro in libros:
            fila+=1
            if busqueda in libro:
                eliminado.append(libro)
                break
        # todo libro con coincidencias se agrega
        if not eliminado==[]:
            print(f'\n¿Seguro deseas eliminar el libro de la fila:{fila}?')
            print(tabulate(eliminado, encabezados))
            texto='\'si\' para aceptar o, cualquier cosa para recharzar,\Escribe: '
            decision = input(texto)
            if decision=='si':
                eliminar(fila, hojas_google_sheet['pruebas'])
            else:
                print('No se elimino el libro.')
        else:
            print('-xXx- Libro NO encontrado -xXx-')
    
    while True:
        texto='\n\t**Bibliotecario**\nPuedes gestionar los libros.\n(1) Consultar libro.\n(2) Agregar libro.\n(3) Eliminar libro.\n(4) Regresar al menu.\nDigita el numero de las opciones: '
        eleccion = preguntar_opciones(text=texto)
        if eleccion==1:
            consultar_libros()
        elif eleccion==2:
            agregar_libros()
        elif eleccion==3:
            eliminar_libros()
        elif eleccion==4:
            break

def funciones_cliente():
    def prestar_libros():
        texto='\n\t**Cliente**\nPrestamos de libros.\nIngresar el titulo o autor exacto, del libro: '
        respuesta=input(texto)
        
        if existe_en_tabla(respuesta,'Libros'):
            texto='\'si\' para aceptar o, cualquier cosa para recharzar,\Escribe: '
            respuesta=input(texto)
            if respuesta=='si':
                pass
                #eliminar(fila, hojas_google_sheet['pruebas'])
            else:
                print('No se elimino el libro.')
    
    def devolver_libros():
        pass
    
    while True:
        texto='\n\t**Cliente**\nBienvenido cliente.\n(1) Consultar libro.\n(2) Prestar libro.\n(3) Devolver libro.\n(4) Regresar al menu.\nDigita el numero de tu peticion: '
        eleccion = preguntar_opciones(text=texto)
        if eleccion==1:
            consultar_libros()
        elif eleccion==2:
            prestar_libros()
        elif eleccion==3:
            devolver_libros()
        elif eleccion==4:
            break

def opciones_usuario(tipo_user, comando, texto):
    
    def verificar_existe_user(user, tipo_user):
        table = consulta_total('Usuarios')
        table.pop(0) #elimino los encabezados
        return ([user, tipo_user] in table)
    
    while True:
        respuesta = input(texto)
        if verificar_existe_user(respuesta, tipo_user):
            comando() # comando deberá ser una funcion, por obligación
            break
        elif (respuesta == 'atras'):
            break
        else:
            print('-xXx- Usuario erroneo, prueba de nuevo. -xXx-')

def menu():
    try:
        while True:
            texto = '\n\t**Menu**\nBienvenido al gestor de biblioteca.\nTipos de usuarios:\n(1) Bibliotecario.\n(2) Cliente.\n(3) Salir.\nDigita el numero de tu tipo: '
            
            eleccion = preguntar_opciones(text=texto)
            if(eleccion==1):
                texto = '\n\t**Bibliotecario**\nIngresa tu usuario o \'atras\'para regresar\nal menu: '
                opciones_usuario('Bibliotecario', funciones_bibliotecario, texto)
                
            elif(eleccion==2):
                texto = '\n\t**Cliente**\nIngresa tu usuario o \'atras\' para regresar: '
                opciones_usuario('Cliente', funciones_cliente, texto)
                
            elif(eleccion==3):
                #sys.exit() # se finaliza la ejecucion
                break # break no dispara la bandera del except
            else:
                print('Debe elegir un numero de las opciones')
    except:
        print('Fallo en el menu')

menu()

