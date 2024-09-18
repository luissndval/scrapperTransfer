import time

from ScrapTransfer.element.elements import elements
from _pom.front.front import functions
from code_Api.routes.catcher_Mails import get_token_from_gmail
from selenium.webdriver.common.by import By


class GoToTransfer(functions):

    def TransferMoney(self,NumeroCuenta,Monto,Concepto,Cvv,MesV,YearV,ClaveEspecial):
        time.sleep(2)
        functions.click_Field(self,By.XPATH,elements['MismoBancoTransfer'][0])
        functions.click_Field(self, By.XPATH, elements['MismoBancoTransfer'][1])
        functions.click_Field(self, By.XPATH, elements['MismoBancoTransfer'][2])
        time.sleep(3)
        functions.input_Texto(self, By.XPATH, elements['MismoBancoTransfer'][3],NumeroCuenta)
        functions.click_Field(self,By.XPATH,elements['MismoBancoTransfer'][4])#Siguiente
        functions.input_Texto(self, By.XPATH, elements['MismoBancoTransfer'][5],Monto)
        functions.input_Texto(self, By.XPATH, elements['MismoBancoTransfer'][6],Concepto)
        functions.click_Field(self, By.XPATH, elements['MismoBancoTransfer'][4])# Siguiente        functions.input_Texto(self, By.XPATH, elements['MismoBancoTransfer'][7], Cvv)
        functions.click_Field(self, By.XPATH, elements['MismoBancoTransfer'][4])# Siguiente
        functions.input_Texto(self, By.XPATH, elements['MismoBancoTransfer'][7], Cvv)
        functions.input_Texto(self, By.XPATH, elements['MismoBancoTransfer'][8], MesV)
        functions.input_Texto(self, By.XPATH, elements['MismoBancoTransfer'][9], YearV)
        functions.click_Field(self, By.XPATH, elements['MismoBancoTransfer'][4])# Siguiente
        functions.input_Texto(self, By.XPATH, elements['MismoBancoTransfer'][10], ClaveEspecial)
        functions.click_Field(self, By.XPATH, elements['MismoBancoTransfer'][4])# Siguiente
        username = "luisllaneton@gmail.com"
        password = "kzkw ecgu dbvj hssd"
        # //vxup fcsg xrnf igxe
        search_subject = "Clave Digital - BBVA Provincial"
        token = get_token_from_gmail(username, password, search_subject)
        functions.input_Texto(self, By.XPATH, elements['MismoBancoTransfer'][11],token)# Siguiente





