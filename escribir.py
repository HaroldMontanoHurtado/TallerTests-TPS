from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
# ID del doc
SPREADSHEET_ID = '1fVnfna2mmYxpfsn0UjnbXTzeJPGnhDfqgFVGhiN-2mY'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

#Debe ser una matriz, y por eso el doble [[]]
values = [['Pruebas!']]
# Llamar la api. Con append() podemos agregar datos al final de la columna.
result = sheet.values().append(
    spreadsheetId=SPREADSHEET_ID, range='Libro!A1',
    valueInputOption='USER_ENTERED',
    body={'values':values}).execute()

# tambien existe update para actualizar datos

print(f"Datos insertados correctamente.\n{(result.get('updates').get('updateCells'))}")
