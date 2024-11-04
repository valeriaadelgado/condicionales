'''
Para trabajar con condicionales utilizamos la instruccion if
if exp_bool:
      instrucciones
if exp_bool:
      instrucciones
else:
     instrucciones
if exp_bool:
    inst
elif exp_bool:
    inst
else:
    inst
'''

print('Programa que lee dos numeros')
print('Nos dice cual es mayor')
num1 = int(input('Ingresa un numero: '))
num2 = int(input('Ingresa otro numero: '))
if num1 > num2:
    print(f'El { num1 } es mayor')
else:
    print(f'El { num2 } es mayor')
    