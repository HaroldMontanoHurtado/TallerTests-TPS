from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'models/key.json'
# ID del doc
SPREADSHEET_ID = '1fVnfna2mmYxpfsn0UjnbXTzeJPGnhDfqgFVGhiN-2mY'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

def aplanar_listas(lista):
    # Usando comprensión de listas
    lista_aplanada = [item for sublist in lista for item in sublist]
    print(lista_aplanada)

def consultar(hoja, startIndex, endIndex):
    #Llamar la api. Con get() es la funcion para leer u obtener datos
    try:
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=f'{hoja}!{startIndex}:{endIndex}').execute()
        # extraemos values del resultado
        values = aplanar_listas(result.get('values', [])) # result.get('values', [])
        print(values)
    except Exception as ex:
        print('Error al consultar: ' + ex)

def agregar(hoja, values):
    try:
        request = sheet.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=hoja,
            valueInputOption='USER_ENTERED',
            body={"values": values}
        )
        request.execute()
    except Exception as ex:
        print('Error al agregar: ' + ex)

def modificar(hoja, index, values):
    try:
        #Debe ser una matriz, y por eso el doble [[]]
        # Llamar la api. Con append() podemos agregar datos al final de la columna.
        result = sheet.values().update(
            spreadsheetId=SPREADSHEET_ID, range=f'{hoja}!{index}',
            valueInputOption='USER_ENTERED',
            body={'values':values})
        result.execute()
    except Exception as ex:
        print('Error al modificar: ' + ex)

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
        request = sheet.batchUpdate(spreadsheetId=SPREADSHEET_ID, body=request_body)
        request.execute()
    except Exception as ex:
        print('Error al eliminar: ' + ex)

#consultar('pruebas', 'F5', 'F5')
#agregar('pruebas', [['Cactus', 'Doroteo', 'Bibliotecario', 'Dormir', 'X', 'Y', 'Hernesto', 'Perez']])
#modificar('pruebas', 'H7',[['CAMBIO_2!!']])
'''
hojas = ['423776484', '', '']
eliminar(15, hojas[0])
'''