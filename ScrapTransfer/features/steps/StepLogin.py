import json
import os

from ScrapTransfer.pages.GetSaldo import GetSaldo
from ScrapTransfer.pages.Login import InicioSesion
from ScrapTransfer.pages.Logout import CerrarSesion
from behave import given, when, then
from code_Api.routes.get_Account_Data_Api import client_data_global

@given('Iniciar Sesion.')
def step_impl(context):
    client_data_list = client_data_global  # Acceder a la variable global
    if not client_data_list:
        raise AssertionError("client_data_global está vacío.")
    try:
        for client_data in client_data_list:
            TipoCuenta = client_data['tipo_cuenta']
            TipoDoc = client_data['tipo_doc']
            documento = client_data['documento']
            password = client_data['password']
            InicioSesion.log(context, TipoCuenta, TipoDoc, documento, password)
    except Exception as e:
        raise AssertionError(f"Error al Iniciar Sesion: {str(e)}")

@when('Dirigirse a cuenta.')
def step_impl(context):
    try:
        GetSaldo.Saldo(context)
    except Exception as e:
        assert False, "Error al Obtener Saldo: " + str(e)

@then('Obtener Saldo')
def step_impl(context):
    try:
        CerrarSesion.logout(context)
    except Exception as e:
        assert False, "Error al Cerrar Sesion: " + str(e)
