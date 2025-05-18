
from Gestion import validar as val
from Datos import mensajes as mjs
from Datos import configuracion as config
from UI import interfaz as ui

def separador(tipo_de_separador="linea"):
    return val.validar_separador(tipo_de_separador)

def obtener_pregunta(tipo, n1, n2):
    return config.preguntas[tipo](n1, n2)

def pedir_numero():
    numero = input(mjs.pedir_numero)
    return val.validar_numero(numero)

def pedir_confirmacion(tipo_de_confirmacion):
    numero = input(mjs.si_o_no[tipo_de_confirmacion])
    return val.validar_confirmacion(numero)

def pedir_respuesta(pregunta):
    return val.validar_numero(input(pregunta + " = "))

def preguntar_hasta_acertar(pregunta, resultado):
    while True:
        respuesta = pedir_respuesta(pregunta)
        if val.validar_respuesta(respuesta, resultado):
            ui.mostrar_separador("espacio")
            ui.mostrar_mensaje("CORRECTO", "linea")
            break
        else:
            ui.mostrar_mensaje("INCORRECTO. Intenta de nuevo.", "linea")