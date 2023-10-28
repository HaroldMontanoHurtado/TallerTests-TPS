try:
    from models.ConnectionDB import consulta_total, agregar, eliminar, consultar_libros
except:
    from src.models.ConnectionDB import consulta_total, agregar, eliminar, consultar_libros
from tabulate import tabulate

# el llamado 'models.ConnectionDB' genera conflico con el pytest
# pide hacer 'src.models.ConnectionDB' para que no tenga problema

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

def funciones_bibliotecario(user):
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
        
        try:
            agregar('Libros', [libro])
        except Exception as ex:
            print(f'Error al agregar libro.\n{ex}')
    
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
                print('Eliminacion exitosa.\n')
                break
            
        if not eliminado==[]:
            print(f'\n¿Seguro deseas eliminar el libro, de la fila:{fila}?')
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
            consultar_libros(buscado)
        elif eleccion==2:
            agregar_libros()
        elif eleccion==3:
            eliminar_libros()
        elif eleccion==4:
            break

def funciones_cliente(user):
    def prestar_libros():
        texto = '\n\t**Cliente**\nPrestacion de libros.\nDigita el titulo o autor exacto del libro: '
        busqueda = input(texto)
        libros = consulta_total('Libros')
        encabezados = libros.pop(0)
        fila=1
        prestamo=[]
        
        for libro in libros:
            fila+=1
            if busqueda in libro:
                prestamo = libro
                break
        copias_totales=int(prestamo[2])
        prestados=int(prestamo[3])
        #print(f'prestados:{prestados} ; copias totales:{copias_totales}')
        if not prestamo==[]:
            if prestados < copias_totales:
                print(f'\n¿Seguro deseas prestar este libro, de la fila:{fila}?')
                print(tabulate([prestamo], encabezados))
                texto='\'si\' para aceptar o, cualquier cosa para recharzar,\nEscribe: '
                decision = input(texto)
                if decision=='si':
                    agregar('Prestamos', [[user, prestamo[0]]])
                    print('Se realizó el prestamo correctamente.')
                else:
                    print('No se elimino el libro.')
            else:
                print('No hay libros disponibles')
    
    def devolver_libros():
        texto = '\n\t**Cliente**\nDevolver el libro.\nDigita el titulo o autor exacto del libro: '
        busqueda = input(texto)
        prestamos = consulta_total('Prestamos')
        encabezados = prestamos.pop(0)
        fila=1
        regreso=[]
        user_libro=[user, busqueda]
        
        if user_libro in prestamos:
            for prestamo in prestamos:
                fila+=1
                if user_libro==prestamo:
                    regreso.append(prestamo)
                    eliminar(fila, hojas_google_sheet['Prestamos'])
                    print(f'Regreso exitoso del libro:\n{tabulate(regreso, encabezados)}\n')
                    break
        else:
            print(f'El usuario \'{user}\' no ha prestado el\nlibro \'{busqueda}\'.')
    
    while True:
        texto='\n\t**Cliente**\nBienvenido cliente.\n(1) Consultar libro.\n(2) Prestar libro.\n(3) Devolver libro.\n(4) Regresar al menu.\nDigita el numero de tu peticion: '
        eleccion = preguntar_opciones(text=texto)
        if eleccion==1:
            buscado = input('\n\t**Consulta libro**\nDigita el titulo o el autor del\nlibro: ')
            consultar_libros(buscado)
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
            comando(respuesta) # comando deberá ser una funcion, por obligación
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
