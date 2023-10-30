try:
    from models.ConnectionDB import consultar_tablas, agregar, eliminar, prestar_libros, devolver_libros, consultar_libro, hallar_fila, hojas_google_sheet
except:
    from src.models.ConnectionDB import consultar_tablas, agregar, eliminar, prestar_libros, devolver_libros, consultar_libro, hallar_fila, hojas_google_sheet
from tabulate import tabulate

# el llamado 'models.ConnectionDB' genera conflico con el pytest
# pide hacer 'src.models.ConnectionDB' para que no tenga problema

def preguntar_opciones(text):
    
    while(True):
        eleccion = input(text)
        try: # intento volver numero el valor de entrada
            eleccion = int(eleccion)
        except:
            print('\nIngreso de un valor no valido.')
        # pregunto si el valor es un numero
        if(isinstance(eleccion, int)):
            break
    
    return eleccion

def imprimir_hoja(table_hoja):
    table = consultar_tablas(table_hoja)
    encabezados = table.pop(0)
    print(tabulate(table, headers=encabezados))

def funciones_bibliotecario(user):
    # funciones de gestion de los libros
    def agregar_libros():
        libro=[]
        
        texto='\n\t**Bibliotecario**\nVamos a agregar el libro en dos pasos.\nPrimero ingresa el titulo del libro: '
        dato=input(texto)
        libro.append(dato) # add titulo del libro
        
        texto='\n\t**Bibliotecario**\nY ahora vamos a agregar el nombre del autor: '
        dato=input(texto)
        libro.append(dato) # add nombre del autor
        
        libro.append(0) # add cantidad de libros prestados
        
        agregar('Libros', [libro])
    
    def eliminar_libros():
        texto = '\n\t**Bibliotecario**\nVamos a eliminar un libro.\nDigita el titulo exacto del libro: '
        busqueda = input(texto)
        libros = consultar_tablas('Libros')
        encabezados = libros.pop(0)
        fila=0
        eliminado=[]
        
        for libro in libros:
            if busqueda in libro:
                eliminado.append(libro)
                fila=hallar_fila(eliminado[0][0],'Libros')
                break
            
        if not eliminado==[]:
            print(f'\n¿Seguro deseas eliminar el libro, de la fila: {fila}?')
            print(tabulate(eliminado, encabezados))
            texto='\'si\' para aceptar o, cualquier cosa para recharzar,\nEscribe: '
            decision = input(texto)
            if decision=='si':
                eliminar(fila, hojas_google_sheet['Libros'])
            else:
                print('No se elimino el libro.')
        else:
            print('-xXx- Libro NO encontrado -xXx-')
    
    while True:
        texto='\n\t**Bibliotecario**\nPuedes gestionar los libros.\n(1) Consultar libro.\n(2) Agregar libro.\n(3) Eliminar libro.\n(4) Regresar al menu.\nDigita el numero de las opciones: '
        eleccion = preguntar_opciones(text=texto)
        if eleccion==1:
            buscado = input('\n\t**Consulta libro**\nDigita el titulo o el autor del\nlibro: ')
            consultar_libro(buscado)
        elif eleccion==2:
            agregar_libros()
        elif eleccion==3:
            eliminar_libros()
        elif eleccion==4:
            break

def funciones_cliente(user):    
    while True:
        texto='\n\t**Cliente**\nBienvenido cliente.\n(1) Consultar libro.\n(2) Prestar libro.\n(3) Devolver libro.\n(4) Regresar al menu.\nDigita el numero de tu peticion: '
        eleccion = preguntar_opciones(text=texto)
        if eleccion==1:
            buscado = input('\n\t**Consulta libro**\nDigita el titulo o el autor del\nlibro: ')
            consultar_libro(buscado)
        elif eleccion==2:
            texto = '\n\t**Cliente**\nPrestacion de libros.\nDigita el titulo o autor exacto del libro: '
            busqueda = input(texto)
            prestar_libros(user, busqueda)
        elif eleccion==3:
            texto = '\n\t**Cliente**\nDevolver el libro.\nDigita el titulo o autor exacto del libro: '
            busqueda = input(texto)
            devolver_libros(user, busqueda)
        elif eleccion==4:
            break

def crear_usuario():
    user=[]
    
    texto='\n\t**Crear usuario**\nVamos a agregar el usuario en dos pasos.\nPrimero ingresa tu nombre: '
    dato=input(texto)
    user.append(dato) # add nombre de usuario
    
    texto='\n\t**Bibliotecario**\nY ahora vamos a agregar el tipo de usuario\n(1) Cliente.\n(2) Bibliotecario.\nDigita la opcion: '
    dato=preguntar_opciones(texto)
    if dato == 1:
        dato='Cliente'
    else:
        dato='Bibliotecario'
    user.append(dato) # add tipo de usuaio
    
    agregar('Usuarios', [user])

def opciones_usuario(tipo_user, comando, texto):
    
    def verificar_existe_user(user, tipo_user):
        table = consultar_tablas('Usuarios')
        table.pop(0) #elimino los encabezados
        return ([user, tipo_user] in table)
    
    while True:
        respuesta = input(texto)
        if verificar_existe_user(respuesta, tipo_user):
            comando(respuesta) # comando deberá ser una funcion, por obligación
            break
        elif (respuesta == 'atras'):
            break
        else:
            print('-xXx- Usuario erroneo, prueba de nuevo. -xXx-')

def menu():
    try:
        while True:
            texto = '\n\t**Menu**\nBienvenido al gestor de biblioteca.\nTipos de usuarios:\n(1) Bibliotecario.\n(2) Cliente.\n(3) Crear Usuario.\n(4) Salir.\nDigita el numero de la opcion: '
            
            eleccion = preguntar_opciones(text=texto)
            if(eleccion==1):
                texto = '\n\t**Bibliotecario**\nIngresa tu usuario o \'atras\'para regresar\nal menu: '
                opciones_usuario('Bibliotecario', funciones_bibliotecario, texto)
            elif(eleccion==2):
                texto = '\n\t**Cliente**\nIngresa tu usuario o \'atras\' para regresar: '
                opciones_usuario('Cliente', funciones_cliente, texto)
            elif(eleccion==3):
                crear_usuario()
            elif(eleccion==4):
                #sys.exit() # se finaliza la ejecucion
                break # break no dispara la bandera del except
            else:
                print('Debe elegir un numero de las opciones')
    except Exception as ex:
        print('Fallo en el menu:\n', ex)

menu()
