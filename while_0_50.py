# Inicializamos la variable 'hasta50' en 1, que será nuestro contador
hasta50 = 1

# Inicializamos la variable 'suma' en 0, donde acumularemos la suma total
suma = 0

# Usamos un bucle while que se ejecuta mientras 'hasta50' sea menor o igual a 50
while hasta50 <= 50:
    # Sumamos el valor actual de 'hasta50' a 'suma'
    suma += hasta50
    # Incrementamos 'hasta50' en 1 para avanzar al siguiente número
    hasta50 += 1

# Imprimimos el resultado final de la suma
print(f"La suma de los números del 1 al 50 es: {suma}")

