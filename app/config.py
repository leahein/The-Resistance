import os

import yaml
from services.google_sheet import google_sheet_client

######################################################################
# Paths
######################################################################
PATH_ROOT = os.path.dirname(os.path.abspath(__file__))
PATH_INSTANCE = os.path.join(PATH_ROOT, 'instance')

PATH_SECURE = os.path.join(PATH_INSTANCE, 'secure.yaml')
PATH_GOOGLE_SHEETS_SECURE = os.path.join(PATH_INSTANCE, 'google-sheets.json')


######################################################################
# Secure Credentials
######################################################################

with open(PATH_SECURE, 'r') as PATH_SECURE_FILE_OBJ:
    SECURE_CONFIG = yaml.load(PATH_SECURE_FILE_OBJ.read())

AWS = SECURE_CONFIG['aws']
GS_BOOK_CODE = GS_BOOK_CODE['google_sheet']['book_code']

######################################################################
# Clients
######################################################################

GS_CLIENT = google_sheet_client(PATH_GOOGLE_SHEETS_SECURE)
