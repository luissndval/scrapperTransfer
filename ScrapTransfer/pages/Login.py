import json
import os

from db import Config
from ScrapTransfer.element.elements import elements
from _pom.front.front import functions
from selenium.webdriver.common.by import By


class InicioSesion(functions):

    # def open_credentials(self):
    #     # Obtener la ruta absoluta del archivo de credenciales
    #     project_root = os.path.dirname(os.path.abspath(__file__))  # Obtiene la ruta del archivo actual
    #     credentials_path = os.path.join(project_root, '..', '..', 'credentials.json')  # Ajusta según sea necesario
    #
    #     # Leer los datos del archivo JSON
    #     try:
    #         with open(credentials_path, 'r') as f:
    #             return json.load(f)
    #     except FileNotFoundError:
    #         raise AssertionError(f"El archivo 'credentials.json' no se encontró en {credentials_path}")
    #     except json.JSONDecodeError:
    #         raise AssertionError(f"Error al decodificar 'credentials.json'")

    def log(self, TipoCuenta, TipoDoc, documento, password):
        functions.driver_Chrome_no_Both(self)
        functions.browser(self, Config.Provincial)
        # functions.max(self)

        if TipoCuenta == 'Personas':
            functions.click_Field(self, By.XPATH, elements['logIn'][0])
            functions.Iframe(self, By.XPATH, elements['logIn'][1])
            functions.click_Field(self, By.XPATH, elements['logIn'][2])
            print(f"TipoDoc es: {TipoDoc}")
            if TipoDoc == 'V':
                functions.click_Field(self, By.XPATH, elements['logIn'][3])
            elif TipoDoc == 'E':
                functions.click_Field(self, By.XPATH, elements['logIn'][4])
            elif TipoDoc == 'P':
                functions.click_Field(self, By.XPATH, elements['logIn'][5])
            functions.input_Texto(self, By.XPATH, elements['logIn'][6], documento)
            functions.input_Texto(self, By.XPATH, elements['logIn'][7], password)
            if functions.validates_clickable(self, By.XPATH, elements['logIn'][8]):
                functions.click_Field(self, By.XPATH, elements['logIn'][8])
            functions.Switch_To_Default(self)
