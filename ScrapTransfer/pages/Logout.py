from ScrapTransfer.element.elements import elements
from _pom.front.front import functions
from selenium.webdriver.common.by import By


class CerrarSesion(functions):

    def logout(self):
        functions.click_Field(self,By.XPATH, elements['Logout'][0])
