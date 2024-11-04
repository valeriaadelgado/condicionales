'''
Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba el dí­a correspondiente. 
Si introducimos otro número nos da un error
'''
def dia_de_la_semana(dia):
    """Devuelve el día de la semana correspondiente al número ingresado."""
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    return dias.get(dia, "ERROR: número incorrecto")

# Solicitar el día de la semana
numero_dia = int(input("Introduce un número del 1 al 7 para el día de la semana: "))

# Mostrar el día correspondiente o un mensaje de error
resultado = dia_de_la_semana(numero_dia)
print(resultado)