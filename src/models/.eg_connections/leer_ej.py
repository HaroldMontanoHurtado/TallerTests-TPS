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

#Llamar la api. Con get() es la funcion para leer u obtener datos
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='Bibliotecario!A2:A').execute()
# extraemos values del resultado
values = result.get('values', [])
print(values)
