import json
import os
import time

import pytest
from ScrapTransfer.pages.GetSaldo import GetSaldo
from ScrapTransfer.pages.Login import InicioSesion
from ScrapTransfer.pages.Logout import CerrarSesion

# Obtener la ruta principal (subir tres niveles desde el archivo actual)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Definir la ruta específica para guardar los archivos .json
DATA_DIR = os.path.join(BASE_DIR, 'data')
USER_DATA_FILE = os.path.join(DATA_DIR, 'user_data.json')

class UserContext:
    def __init__(self):
        self.user_data = self.load_user_data()

    @staticmethod
    def load_user_data():
        # Lee los datos del usuario desde un archivo JSON
        with open(USER_DATA_FILE, 'r') as f:
            return json.load(f)

@pytest.fixture(scope="module")
def context():
    return UserContext()

@pytest.mark.usefixtures("context")
class TestScrapTransfer:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, context):
        # Configuración de inicio de sesión
        TipoCuenta = context.user_data['tipo_cuenta']
        TipoDoc = context.user_data['tipo_doc']
        documento = context.user_data['documento']
        password = context.user_data['password']

        self.inicio_sesion = InicioSesion()
        self.inicio_sesion.log(TipoCuenta, TipoDoc, documento, password)
        time.sleep(10)  # Ajusta el tiempo de espera según sea necesario

        # Realiza el teardown (cierre de sesión) después de las pruebas
        yield
        cierre_sesion = CerrarSesion()
        cierre_sesion.logout()

    def test_full_process(self):
        # Obtener saldo
        saldo = GetSaldo.obtener_saldo()
        assert saldo is not None  # Verifica que el saldo no sea None

        # Aquí puedes agregar más operaciones y aserciones si es necesario
        # por ejemplo, validar ciertos valores o realizar otras operaciones
