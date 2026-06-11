# Pedimos al usuario que escriba una frase
frase = input("Escribe una frase: ")

# Inicializamos un contador de vocales
contador = 0

for letra in frase:
    # Verificamos si la letra es una vocal (minúscula o mayúscula)
    if letra.lower() in "aeiou":
        contador += 1  # Si es vocal, aumentamos el contador

# Mostramos el resultado
print(f"La frase tiene {contador} vocales.")
