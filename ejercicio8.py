'''
Programa que pida dos números 'nota' y 'edad' y un carácter 'sexo' 
y muestre el mensaje 'ACEPTADA' si la nota es mayor o igual a cinco, 
la edad es mayor o igual a dieciocho y el sexo es 'F'. 
En caso de que se cumpla lo mismo, pero el sexo sea 'M', debe imprimir 'POSIBLE'. 
Si no se cumplen dichas condiciones se debe mostrar 'NO ACEPTADA'.
'''
nota=float(input(f"Ingresa el valor de tu nota: "))
edad=int(input(f"Ingresa tu edad: "))
sexo=str(input(f"digita F si tu sexo es femenino o M si tu sexo masculino: "))

if nota >= 5 and edad >= 18 and sexo == "f":
    print(f"aceptada")
elif nota >= 5 and edad >= 18 and sexo == "m":
    print(f"posible")
else:
    print(f"no aceptada")