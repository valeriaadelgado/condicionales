'''
Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.
Si introducimos otro número nos da un error.
'''
def dias_del_mes(mes):
    """Devuelve el número de días del mes correspondiente."""
    dias = {
        1: 31,  # Enero
        2: 28,  # Febrero (no considerando años bisiestos)
        3: 31,  # Marzo
        4: 30,  # Abril
        5: 31,  # Mayo
        6: 30,  # Junio
        7: 31,  # Julio
        8: 31,  # Agosto
        9: 30,  # Septiembre
        10: 31, # Octubre
        11: 30, # Noviembre
        12: 31  # Diciembre
    }
    return dias.get(mes, "ERROR: número incorrecto.")

# Solicitar un número entre 1 y 12
numero_mes = int(input("Introduce un número del 1 al 12 para el mes: "))

# Mostrar el número de días o un mensaje de error
resultado = dias_del_mes(numero_mes)
print(resultado)