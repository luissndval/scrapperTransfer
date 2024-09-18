import json
import os

from ScrapTransfer.element.elements import elements
from _pom.front.front import functions
from selenium.webdriver.common.by import By

# Obtener la ruta principal (subir dos niveles desde el archivo actual)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA_DIR = os.path.join(BASE_DIR, 'data')
SALDO_FILE = os.path.join(DATA_DIR, 'saldo.json')

class GetSaldo(functions):

    def Saldo(self):
        saldo = functions.get_text(self,By.XPATH, elements['Dashboard_Get_Saldo'][0])
        # Almacenar el saldo en un archivo JSON
        with open(SALDO_FILE, 'w') as f:
            json.dump({'saldo': f"{saldo}"}, f)
