
from Gestion import validar as val
from Gestion import calculo as cal
from Gestion import gestor
from UI import interfaz as ui
from Datos import mensajes as mjs

def modo_automatico(automatico):
    val.validar_confirmacion(automatico)
    if automatico == "si":
        ui.mostrar_mensaje(mjs.modo_automatico["si"], "linea")
        numero = gestor.pedir_numero()
        ui.mostrar_separador("espacio")
        cal.calculo_automatico(numero)
    elif automatico == "no":
        ui.mostrar_mensaje(mjs.modo_automatico["no"], "linea")