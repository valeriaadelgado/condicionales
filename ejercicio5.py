'''
Escribe un programa que pida un nombre de usuario y una contraseña 
y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
sino se da un error.
'''
user = str(input(f"ingresa tu nombre de usuario: "))
password = str(input(f"ingresa tu contraseña: "))

if user == "pepe" and password == "asdasd" :
    print(f"Bienvenido Pepe, has entrado al sistema")
elif user != "pepe" and password != "asdasd":
    print(f"Lo sentimos {user}, tu usuario y contraseñas son incorrectos")
else:
    print(f"Ingresa tus datos")