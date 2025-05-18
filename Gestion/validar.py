
from Datos.errores import ErrorDeValidacion
from Datos import errores as error
from Gestion import buscar
from UI import interfaz as ui

def _validar_texto_sin_espacios(valor, mensaje_tipo, mensaje_espacios):
    if not isinstance(valor, str):
        raise ErrorDeValidacion(mensaje_tipo)
    if " " in valor:
        raise ErrorDeValidacion(mensaje_espacios)

def validar_error(tipo_de_error, codigo_de_error):
    try:
        return buscar.buscar_error(tipo_de_error, codigo_de_error)
    except AttributeError:
        raise ErrorDeValidacion(error.modulo_invalido["error-no-tiene-atributo"])

def validar_separador(tipo_de_separador):
    try:
        return buscar.buscar_separador(tipo_de_separador)
    except AttributeError:
        raise ErrorDeValidacion(error.sin_definir["error_en_el_separador"])

def validar_confirmacion(texto):
    _validar_texto_sin_espacios(texto, error.modulo_invalido["error-no-es-texto"], error.modulo_invalido["error-contiene-espacios"])
    if texto.lower() not in ["si", "no"]:
        raise ErrorDeValidacion("El valor no es 'si' o 'no'")
    return texto.lower()

def validar_numero(numero):
    _validar_texto_sin_espacios(numero, error.modulo_invalido["error-no-es-texto"], error.modulo_invalido["error-contiene-espacios"])
    try:
        return int(numero)
    except ValueError:
        raise ErrorDeValidacion("No se puede convertir a numero entero")

def validar_respuesta(respuesta, resultado):
    return respuesta == resultado