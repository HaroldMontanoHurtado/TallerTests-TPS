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
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=f'{hoja}!{startIndex}:{endIndex}').execute()
    # extraemos values del resultado
    values = aplanar_listas(result.get('values', [])) # result.get('values', [])
    print(values)

consultar('Cliente', 'A1', 'A1')
