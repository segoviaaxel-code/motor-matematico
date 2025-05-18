
from Datos import errores as error
from Datos import configuracion as config

def buscar_error(tipo_de_error, codigo_de_error):
    if tipo_de_error in config:
        return error.tipo_de_error[codigo_de_error]
    else:
        return error.valor_invalido["error-no-existe"]

def buscar_separador(tipo_de_separador):
    if tipo_de_separador in config.separadores:
        return config.separadores[tipo_de_separador]
    else:
        return error.sin_definir["error_en_el_separador"]