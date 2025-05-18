
from UI import interfaz as ui
from Gestion import gestor
from Gestion import automatico as auto
from Gestion import calculo as cal

ui.mostrar_bienvenida()

usuario = gestor.pedir_confirmacion("probar")
ui.mostrar_separador("linea")

if usuario == "si":
    automatico = gestor.pedir_confirmacion("modo_automatico")
    ui.mostrar_separador("espacio")
    auto.modo_automatico(automatico)
    
    if automatico == "si":
        numero = gestor.pedir_numero()
        ui.mostrar_separador("linea")
        cal.calculo_automatico(numero)
        ui.mostrar_mensaje(f"Numero {numero} convertido a 5", "linea")
    
    elif automatico == "no":
        numero = gestor.pedir_numero()
        ui.mostrar_separador("linea")
        cal.calculo_manual(numero)
        ui.mostrar_mensaje(f"Numero {numero} convertido a 5", "linea")
    
    else:
        ui.mostrar_error("error", "modo_automatico", "linea")
elif usuario == "no":
    ui.mostrar_despedida()