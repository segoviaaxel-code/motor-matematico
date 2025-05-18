
from Datos import errores as error

separadores = {
    "linea": "-" * 80 + "\n",
    "espacio": " " + "\n",
}

operaciones = {
    "sum": lambda numero1, numero2: round(numero1 + numero2),
    "res": lambda numero1, numero2: round(numero1 - numero2),
    "mul": lambda numero1, numero2: round(numero1 * numero2),
    "div": lambda numero1, numero2: round(numero1 / numero2) if numero2 != 0 else error.error_de_calculo["error-division-por-cero"],
}

preguntas = {
    "sum": lambda n, x: f"Cuanto es {n} más {x}",
    "mul": lambda n, x: f"Cuanto es {n} por {x}",
    "div": lambda n, x: f"Cuanto es {n} dividido {x}",
    "res": lambda n, x: f"Cuanto es {n} menos {x}",
}