# Solicita al usuario que ingrese una temperatura en grados Celsius y la convierte a entero
temperatura = int(input("Ingresa la temperatura en Celsius: "))

# Aplica la fórmula de conversión de Celsius a Fahrenheit
conversion = temperatura * (9/5) + 32

# Muestra el resultado en pantalla
print(f"La temperatura en Fahrenheit es {conversion:.2f}")
