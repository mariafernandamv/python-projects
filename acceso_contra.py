# Definimos la contraseña correcta
contra = "123afd"

# Pedimos al usuario que ingrese una contraseña
usuario = input("Ingrese la contraseña: ")

# Comparamos la contraseña ingresada con la contraseña correcta
if usuario == contra:
    # Si coinciden,  accesa
    print("Acceso concedido")
else:
    # Si no coinciden, se no  accesa
    print("Acceso denegado")
