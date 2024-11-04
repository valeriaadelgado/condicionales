'''
Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
al lanzar un dado de seis caras y muestre por pantalla el número en letras 
(dato cadena) de la cara opuesta al resultado obtenido.
 * Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
 * Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
 se mostrará el mensaje: "ERROR: número incorrecto.".
'''
def numero_a_letras(numero):
    """Convierte un número entero a su representación en letras."""
    letras = {
        1: "uno",
        2: "dos",
        3: "tres",
        4: "cuatro",
        5: "cinco",
        6: "seis"
    }
    return letras.get(numero, "")

def cara_opuesta(resultado):
    """Devuelve el número de la cara opuesta según el resultado del dado."""
    opuestas = {
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return opuestas.get(resultado)

# Solicitar el resultado del dado
resultado = int(input("Introduce el resultado del dado (número del 1 al 6): "))

# Validar el resultado y mostrar el mensaje correspondiente
if resultado < 1 or resultado > 6:
    print("ERROR: número incorrecto.")
else:
    opuesta = cara_opuesta(resultado)
    print(f"La cara opuesta al {resultado} es {numero_a_letras(opuesta)}.")