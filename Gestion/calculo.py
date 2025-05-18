
from Datos import configuracion as config
from UI import interfaz as ui
from Gestion import gestor
from Gestion import validar as val

def hacer_calculo(tipo_de_calculo, numero1, numero2):
    return config.operaciones[tipo_de_calculo](numero1, numero2)

def hacer_calculo_manual(tipo_de_calculo, numero1, numero2):
    resultado = hacer_calculo(tipo_de_calculo, numero1, numero2)
    pregunta = gestor.obtener_pregunta(tipo_de_calculo, numero1, numero2)
    gestor.preguntar_hasta_acertar(pregunta, resultado)
    return resultado

def calculo_automatico(numero):
    suma = round(hacer_calculo("sum", numero, 3))
    multi = round(hacer_calculo("mul", suma, 2))
    suma2 = round(hacer_calculo("sum", multi, 4))
    div = round(hacer_calculo("div", suma2, 2))
    resultado = round(hacer_calculo("res", div, numero))
    ui.mostrar_calculo(numero, suma, multi, suma2, div, resultado)
    return resultado

def calculo_manual(numero):
    suma = round(hacer_calculo_manual("sum", numero, 3))
    multi = round(hacer_calculo_manual("mul", suma, 2))
    suma2 = round(hacer_calculo_manual("sum", multi, 4))
    div = round(hacer_calculo_manual("div", suma2, 2))
    resultado = round(hacer_calculo_manual("res", div, numero))
    return resultado