# Solicita al usuario un número 
num = int(input("Agrega el número: "))

# Define la función que verifica si un número es primo
def es_primo(num):
    # Los números menores que 2 no son primos
    if num < 2:
        return False
    # Recorre desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(num ** 0.5) + 1):
        # Si encuentra un divisor exacto, no es primo
        if num % i == 0:
            return False
    # Si no encuentra divisores, es primo
    return True

# Llama a la función y muestra el resultado
if es_primo(num):
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")
