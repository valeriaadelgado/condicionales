'''
Juego Piedra Papel y Tijera
Programa que lea las opciones de 2 jugadores, y muestra el resultado
Empate, gana jugador 1 o gana jugador 2
Si introducimos una opción que no coindica con piedra, papel o tijera
Diga que opción Incorrecta
'''
def resultado_juego(opcion1, opcion2):
    """Determina el resultado del juego entre dos opciones."""
    if opcion1 == opcion2:
        return "Empate"
    elif (opcion1 == "piedra" and opcion2 == "tijera") or \
         (opcion1 == "tijera" and opcion2 == "papel") or \
         (opcion1 == "papel" and opcion2 == "piedra"):
        return "Gana jugador 1"
    else:
        return "Gana jugador 2"

# Solicitar las opciones de los jugadores
jugador1 = input("Jugador 1, elige: piedra, papel o tijera: ").lower()
jugador2 = input("Jugador 2, elige: piedra, papel o tijera: ").lower()

# Verificar que las opciones sean válidas
opciones_validas = ["piedra", "papel", "tijera"]

if jugador1 not in opciones_validas or jugador2 not in opciones_validas:
    print("Opción incorrecta. Por favor, elige piedra, papel o tijera.")
else:
    # Mostrar el resultado del juego
    resultado = resultado_juego(jugador1, jugador2)
    print(f"Resultado: {resultado}")