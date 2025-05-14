
from UI import mensajes as mjs
import time

def separador(tipo="linea"):
    try:
        if hasattr(mjs, "separadores") and tipo in mjs.separadores:
            print(mjs.separadores[tipo])
            time.sleep(0.5)
        else:
            print(f"[ERROR] Valor '{tipo}' es invalido")
    except AttributeError:
        print("[ERROR] El modulo 'mjs' no contiene el atributo 'separadores'")

def mostrar_mensaje(frase="Aqui va la frase que quieres mostrar", tipo_de_separador="espacio"):
    print(frase)
    time.sleep(0.5)
    separador(tipo_de_separador)