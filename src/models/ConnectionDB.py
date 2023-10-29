from googleapiclient.discovery import build
from google.oauth2 import service_account
from tabulate import tabulate
from re import compile, IGNORECASE

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'src/models/key.json'
# ID del doc
SPREADSHEET_ID = '1fVnfna2mmYxpfsn0UjnbXTzeJPGnhDfqgFVGhiN-2mY'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

hojas_google_sheet={
    'Usuarios':'0', 'Libros':'2102902917',
    'Prestamos':'2023029017', 'pruebas':'423776484'}

def aplanar_listas(lista):
    # Usando comprensión de listas
    lista_aplanada = [item for sublist in lista for item in sublist]
    print(lista_aplanada)

def consultar_tablas(hoja):
    #Llamar la api. Con get() es la funcion para leer u obtener datos
    try:
        result = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID, 
        range=f'{hoja}!A1:E30').execute()
        # extraemos values del resultado
        values = result.get('values', []) # result.get('values', [])
        return values # aplanar_listas(values)
        #print(values)
    except:
        print('Error al consultar')

def consulta_especifica(hoja, startIndex, endIndex):
    #Llamar la api. Con get() es la funcion para leer u obtener datos
    try:
        result = sheet.values().get(
            spreadsheetId=SPREADSHEET_ID, 
            range=f'{hoja}!{startIndex}:{endIndex}')
        result.execute()
        # extraemos values del resultado
        values = result.get('values', []) # result.get('values', [])
        print(values)
    except:
        print('Error al consultar')

def agregar(hoja, values):
    ''' Tipos:
    Usuario(Name, typeUser)
    Libro(Tittle, Author, #books, #prestados, #total libros)
    '''
    if not existe_en_tabla(values[0][0], hoja):
        try:
            request = sheet.values().append(
                spreadsheetId=SPREADSHEET_ID,
                range=hoja,
                valueInputOption='USER_ENTERED',
                body={"values": values}
            ).execute()
            #print(f'\'{values[0][0]}\' se agregó correctamente')
        except Exception as ex:
            print('Error al agregar.\nError de tipo:', ex)
    else:
        print(f'\n-xXx-\'{values[0][0]}\' ya existe.-xXx-\n')

def modificar(hoja, index, values):
    try:
        #Debe ser una matriz, y por eso el doble [[]]
        # Llamar la api. Con append() podemos agregar datos al final de la columna.
        result = sheet.values().update(
            spreadsheetId=SPREADSHEET_ID, range=f'{hoja}!{index}',
            valueInputOption='USER_ENTERED',
            body={'values':values}).execute()
    except:
        print('Error al modificar')

def eliminar(fila, hoja_id):
    try:
        spreadsheet_data = [
            
            {
                "deleteDimension": {
                "range": {
                    "sheetId": hoja_id, #id del la hoja en especifico
                    "dimension": "ROWS",
                    "startIndex": (fila-1), # solo elimina filas mayores estrictas a startIndex
                    "endIndex": fila # hasta la fila igual al endIndex
                    }
                }
            }
        ]
        request_body = {"requests": spreadsheet_data}
        request = sheet.batchUpdate(
            spreadsheetId=SPREADSHEET_ID,
            body=request_body).execute()
        print('Eliminacion exitosa.\n')
    except Exception as ex:
        print('Error al eliminar:\n', ex)

# no se ha usado
def existe_en_tabla(key, sheet):
    tabla=consultar_tablas(sheet)
    
    for fila in tabla:
        if key in fila:
            return True
    return False

def existe_coincidencia(lista, valor):
    # Compila una expresión regular que coincide con el valor en cualquier parte de la cadena,
    patron = compile(valor, IGNORECASE) # sin tener en cuenta mayúsculas y minúsculas
    # Busca el valor en la lista
    coincidencias = [x for x in lista if patron.search(x)]
    
    return not coincidencias==[] # Pregunta si existe alguna coincidencia

def consultar_libro(buscado):
    libros = consultar_tablas('Libros')
    encabezados = libros.pop(0)
    libros_coincidentes=[]
    
    for libro in libros:
        if existe_coincidencia(libro, buscado):
            libros_coincidentes.append(libro)
    # todo libro con coincidencias se agrega
    if not libros_coincidentes==[]:
        print()
        print(tabulate(libros_coincidentes, encabezados))
    else:
        print('-xXx- Libro NO encontrado -xXx-')
    return libros_coincidentes

def hallar_fila(key, sheet):
    tabla = consultar_tablas(sheet)
    fila=0
    encontrado=[]
    
    for objeto in tabla:
        fila+=1
        if key in objeto:
            encontrado.append(objeto)
            return fila
    return fila
