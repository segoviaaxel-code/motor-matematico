
from UI import interfaz as ui
from UI import mensajes as mjs
from Gestion import gestor

ui.separador("linea")
ui.mostrar_mensaje(mjs.mensaje_de_bienvenida, "linea")

usuario = gestor.pedir_datos("Quieres probar? (si/no): ", "texto")
ui.separador("linea")
if usuario == "si":
    automatico = gestor.pedir_datos("Quieres que haga la cuenta automaticamente?: ", "texto")
    ui.separador("espacio")
    gestor.modo_automatico(automatico)
    if automatico == "si":
        numero = int(gestor.pedir_datos("Dame un numero: "))
        ui.separador("linea")
        gestor.calculo_automatico(numero)
    
    elif automatico == "no":
        while True:
            try:
                numero = int(gestor.pedir_datos("Dame un numero: "))
                ui.separador("espacio")
                gestor.calculo_manual(numero)
                ui.mostrar_mensaje(f"Numero {numero} comvertido a 5", "linea")
                break
            except ValueError:
                ui.mostrar_mensaje("[ERROR] Valor invalido ingrese un numero valido")
                break

elif usuario == "no":
    ui.mostrar_mensaje("Bueno nos vemos luego...", "linea")