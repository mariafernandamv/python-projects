# Pedimos al usuario que ingrese el primer número 
num1 = float(input("Ingrese un número: "))

# Pedimos al usuario que ingrese el segundo número 
num2 = float(input("Ingrese otro número: "))

# Definimos una función para sumar los dos números
def suma(num1, num2):
    print(f"La suma de sus números es {num1 + num2}")

# Definimos una función para restar el segundo número al primero
def resta(num1, num2):
    print(f"El resultado de la resta es {num1 - num2}")

# Definimos una función para multiplicar los dos números
def multipli(num1, num2):
    print(f"El resultado de la multiplicación es {num1 * num2}")

# Definimos una función para dividir el primer número entre el segundo
def divisi(num1, num2):
    # Verificamos que el segundo número no sea cero para evitar error
    if num2 != 0:
        print(f"El resultado de la división es {num1 / num2}")
    else:
        print("No se puede dividir entre cero.")

# Mostramos las opciones disponibles al usuario
print("Elija 1 para sumar")
print("Elija 2 para restar")
print("Elija 3 para multiplicar")
print("Elija 4 para dividir")

# Pedimos al usuario que seleccione una opción
opcion = input("Seleccione la opción: ")

# Usamos condicionales para ejecutar la operación correspondiente
if opcion == "1":
    suma(num1, num2)
elif opcion == "2":
    resta(num1, num2)
elif opcion == "3":
    multipli(num1, num2)
elif opcion == "4":
    divisi(num1, num2)
else:
    # Si el usuario ingresa una opción inválida
    print("Opción no válida.")