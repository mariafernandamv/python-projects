# Pedimos al usuario que ingrese la altura del rectángulo
altura = int(input("Agrega la altura: "))

# Pedimos al usuario que ingrese la base del rectángulo
base = int(input("Agrega la base: "))

# Definimos una función llamada 'rectangulo' 
def rectangulo(base, altura):
    # Calculamos el área multiplicando base por altura 
    print(f"El área del rectángulo es {base * altura}")

# Llamamos a la función 'rectangulo'
rectangulo(base, altura)
