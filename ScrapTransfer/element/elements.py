elements = {
    "logIn": [
        "//a[@aria-label='Acceso']",
        "//iframe[@class='access__iframe']",
        "//select[@id='select_doc']",
        "//option[@value='V']",
        "//option[@value='E']",
        "//option[@value='P']",
        "//input[@name='cedula']",
        "//input[@name='password']",
        "//button[@class='btn boton-submit boton']"
    ],
    "Dashboard_Get_Saldo": [
        "//table[@id='lstCuentasBuscador']//strong",
    ],

    "MismoBancoTransfer": [
        "//span[contains(text(),'0108')]//..//button",
        "//a[text()='Realizar transferencias']",
        "//a[@id='clickOtrosTitulares']",
        "//input[@name='numCuenta']",
        "//form//button[@id='wizardNext']",
        "//input[@name='monto']",
        "//input[@id='concepto']",
        "//input[@id='cvv-input']",
        "//div[@class='col-xs-6 col-sm-6 col-md-4 col-lg-4']//*[@id='month-to-cvv']",
        "//div[@class='col-xs-6 col-sm-6 col-md-4 col-lg-4']//input[@id='year-to-cvv']",
        "//input[@name='clave-segura']",
        "//input[@id='claveDigital']",
        "//button[@class='btn primary right']"
    ],

    "OtrosBancosTransfer": [
        "//span[contains(text(),'0108')]//..//button",
        "//a[text()='Realizar transferencias']",
        "//a[@id='clickOtrosBancos']"
        "//input[@name='beneficiario']",
        "//div[@class='nombreBenefTOB-Resp']//input[@name='beneficiario']",
        "//input[@name='numIdentificacion']",
        "//div[@class='ctaDestinoTOB-Resp']//input[@name='numCuenta']",
        "//button[@class='btn arrow-right next pull-right wizardNext']",
        "//form//button[@id='wizardNext']",
        "//input[@name='monto']",
        "//input[@id='concepto']",
        "//input[@id='cvv-input']",
        "//label[text()='Mes:']//..//input[@id='month-to-cvv']",
        "//input[@id='year-to-cvv']",
        "//input[@name='clave-segura']"

    ],

    "Logout": [
        "//a[@class='btn small warning logout-btn']"
    ]

}
