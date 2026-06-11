# Solicita al usuario que ingrese un número 
numero = int(input("Agrega el número a multiplicar: "))

# Inicia un bucle que va del 1 al 10 
for i in range(1, 11):
    # Calcula el resultado de la multiplicacion
    operacion = numero * i
    # Muestra el resultado en formato de tabla de multiplicar
    print(f"{numero} x {i} = {operacion}")


