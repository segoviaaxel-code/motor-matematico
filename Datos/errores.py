
class ErrorDeValidacion(Exception):
    pass

modulo_invalido = {
    "error-no-tiene-atributo": "[ERROR] El modulo no tiene el atributo solicitado",
    "error-no-existe": "[ERROR] El error no existe en el modulo",
    "error-no-es-texto": "[ERROR] El valor proporcionado no es un texto",
    "error-contiene-espacios": "[ERROR] El texto contiene espacios no permitidos",
    "error-desconocido": "[ERROR] Ha ocurrido un error desconocido",
}

sin_definir = {
    "error_en_el_separador": "[ERROR] En el tipo de separador elegido no existe",
}

error_de_calculo = {
    "error-de-division-por-cero": "[ERROR] Division por cero invalida",
}
