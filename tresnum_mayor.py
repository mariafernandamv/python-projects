# Solicita al usuario que ingrese tres números decimales
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

# Compara los tres números para encontrar el mayor
if num1 > num2 and num1 > num3:
    print(f"El número mayor es: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"El número mayor es: {num2}")
elif num3 > num1 and num3 > num2:
    print(f"El número mayor es: {num3}")
else:
    # Si no hay un único número mayor, significa que al menos dos son iguales y son los más grandes
    print("Hay al menos dos números iguales y son los mayores.")

