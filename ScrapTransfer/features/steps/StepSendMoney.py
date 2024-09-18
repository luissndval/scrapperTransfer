from ScrapTransfer.pages.GoToTransfer import GoToTransfer
from behave import when


@when(u'Dirigirse a Transferencia.')


def step_impl(context):
    NumeroCuenta='2418410200148087'
    Monto='1'
    Concepto='Pago'
    Cvv='101'
    MesV='02'
    YearV='2025'
    ClaveEspecial='L1234567'
    GoToTransfer.TransferMoney(context,NumeroCuenta,Monto,Concepto,Cvv,MesV,YearV,ClaveEspecial)


