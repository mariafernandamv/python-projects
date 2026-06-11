# Definimos una función  que recibe un texto
def invertir_cadena(texto):
    # Usamos slicing [::-1] para invertir el orden de los caracteres
    return texto[::-1]

# Pedimos al usuario que escriba una palabra 
cadena = input("Escribe una palabra ")

# Llamamos a la función 
resultado = invertir_cadena(cadena)

# Mostramos la cadena invertida 
print(f"Cadena invertida: {resultado}")
