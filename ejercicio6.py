'''
Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
'''
# Solicitar al usuario que ingrese una cadena
cadena = input("Ingrese una letra: ")

# Verificar si la cadena es una letra mayúscula
if len(cadena) == 1 and cadena.isalpha() and cadena.isupper():
    print("Es una letra mayúscula")
else:
    print("No es una letra mayúscula")