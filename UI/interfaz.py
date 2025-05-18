
from Gestion import validar as val
from Datos import mensajes as mjs
from Datos import configuracion as config
from Gestion import gestor
from Gestion import calculo as cal
import time as tm

def mostrar_separador(tipo_de_separador):
    print(gestor.separador(tipo_de_separador), end="")
    tm.sleep(0.5)

def mostrar_mensaje(frase, tipo_de_separador):
    print(frase)
    tm.sleep(0.3)
    mostrar_separador(tipo_de_separador)

def mostrar_error(tipo_de_error, codigo_de_error, tipo_de_separador):
    val.validar_error(tipo_de_error, codigo_de_error)
    mostrar_separador(tipo_de_separador)

def mostrar_bienvenida():
    mostrar_separador("linea")
    mostrar_mensaje(mjs.bienvenida, "linea")

def mostrar_despedida():
    mostrar_mensaje(mjs.despedida, "linea")

def mostrar_calculo(tipo_de_calculo, numero1, numero2, tipo_de_separador):
    resultado = cal.hacer_calculo(tipo_de_calculo, numero1, numero2)
    mostrar_mensaje(f"El resultado de la operación es: {resultado}", tipo_de_separador)

def mostrar_calculo(numero, suma, multi, suma2, div, resultado):
    mostrar_mensaje(config.preguntas["suma"](numero, suma), "espacio")
    mostrar_mensaje(config.preguntas["multi"](suma, multi), "espacio")
    mostrar_mensaje(config.preguntas["suma2"](multi, suma2), "espacio")
    mostrar_mensaje(config.preguntas["div"](suma2, div), "espacio")
    mostrar_mensaje(config.preguntas["resultado"]((div, numero), resultado), "linea")