
from UI import mensajes as mjs
from UI import interfaz as ui

def modo_automatico(activo="n"):
    try:
        if hasattr(mjs, "modo_automatico") and activo in mjs.modo_automatico:
            if activo == "si":
                ui.mostrar_mensaje("Modo automatico ACTIVADO", "linea")
            elif activo == "no":
                ui.mostrar_mensaje("Modo automatico DESACTIVADO", "linea")
        else:
            ui.mostrar_mensaje(f"[ERROR] Valor '{activo}' invalido", "linea")
    except AttributeError:
        ui.mostrar_mensaje(f"[ERROR] Valor '{activo}' invalido", "linea")

def pedir_datos(pregunta="Aqui va lo que ira en el imput", tipo_de_dato="texto"):
    try:
        if hasattr(mjs, "tipo_de_dato") and tipo_de_dato in mjs.tipo_de_dato:
            if tipo_de_dato == "entero":
                while True:
                    try:
                        respuesta = int(input(pregunta))
                        return respuesta
                    except ValueError:
                            print("[ERROR] Por favor, introduce un numero entero valido")
            elif tipo_de_dato == "texto":
                return input(pregunta)
        else:
            ui.mostrar_mensaje(f"[ERROR] Tipo de dato '{tipo_de_dato}' invalido", "linea")
    except AttributeError:
        ui.mostrar_mensaje(f"[ERROR] Valor '{tipo_de_dato}' invalido", "linea")

def hacer_calculo(numero1, tipo_de_cuenta, numero2):
    if tipo_de_cuenta in mjs.tipo_de_cuenta:
        if tipo_de_cuenta == "sum":
            return numero1 + numero2
        elif tipo_de_cuenta == "res":
            return numero1 - numero2
        elif tipo_de_cuenta == "div":
            if numero2 == 0:
                raise ValueError("[ERROR] Division por cero no permitida")
            return numero1 / numero2
        elif tipo_de_cuenta == "mul":
            return numero1 * numero2
    else:
        raise ValueError(f"[ERROR] Tipo de cuenta '{tipo_de_cuenta}' no valida")

def calculo_automatico(numero):
    ui.mostrar_mensaje("BIEN COMENCEMOS")
    
    suma = hacer_calculo(numero, "sum", 3)
    ui.mostrar_mensaje(f"{numero} mas 3 es {round(suma)}")
    
    multi = hacer_calculo(suma, "mul", 2)
    ui.mostrar_mensaje(f"{suma} multiplicado por 2 es {round(multi)}")
    
    suma2 = hacer_calculo(multi, "sum", 4)
    ui.mostrar_mensaje(f"{multi} mas 4 es {round(suma2)}")
    
    div = hacer_calculo(suma2, "div", 2)
    ui.mostrar_mensaje(f"{suma2} divido 2 es {round(div)}")
    
    resultado = hacer_calculo(div, "res", numero)
    ui.mostrar_mensaje(f"Por ultimo {round(div)} menos {numero} es {round(resultado)}")
    ui.mostrar_mensaje(f"Numero '{numero}' convertido a '{round(resultado)}'", "linea")

def validar_respuesta(numero, frase, comparacion):
    while True:
        try:
            respuesta = int(pedir_datos(f"cuanto es {numero} {frase}?: "))
            ui.separador("espacio")
            if respuesta == comparacion:
                ui.mostrar_mensaje("Correcto", "linea")
                break
            else:
                ui.mostrar_mensaje("Valor incorrecto, intenta de nuevo")
        except ValueError:
            ui.mostrar_mensaje("Entrada no valida, ingrese un numero entero")

def calculo_manual(numero):
    suma = hacer_calculo(numero, "sum", 3)
    validar_respuesta(numero, "mas 3", suma)
    
    multi = hacer_calculo(suma, "mul", 2)
    validar_respuesta(suma, "duplicado por 2", multi)
    
    suma2 = hacer_calculo(multi, "sum", 4)
    validar_respuesta(multi, "mas 4", suma2)
    
    div = hacer_calculo(suma2, "div", 2)
    validar_respuesta(suma2, "dividido por 2", div)
    
    resultado = hacer_calculo(div, "res", numero)
    validar_respuesta(round(div), f"menos {numero}", resultado)