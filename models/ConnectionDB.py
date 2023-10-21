from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

class ConnetionDB:
    def __init__(self):
        try:
            SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
            KEY = 'key.json'
            # ID del doc
            SPREADSHEET_ID = '1fVnfna2mmYxpfsn0UjnbXTzeJPGnhDfqgFVGhiN-2mY'

            creds = None
            creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

            service = build('sheets', 'v4', credentials=creds)
            sheet = service.spreadsheets()
        except Exception as ex:
            print('FALLO AL CONECTAR DB', f'{ex}.')