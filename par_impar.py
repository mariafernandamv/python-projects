# Pedimos al usuario que ingrese un número 
numero = int(input("Ingrese un número: "))

# Verificamos si el número es par 
if numero % 2 == 0:
    # Si el residuo de dividir entre 2 es cero, es par
    print("El número es par.")
else:
    # Si el residuo no es cero, es impar
    print("El número es impar.")
