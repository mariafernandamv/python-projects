nombre_conductor= input("Ingrese el nombre del conductor ")
distancia_km= float(input("Ingrese la distancia en km ") )
tiempo_horas = float(input("ingrese el tiempo en horas "))

#2. Calcular la velocidad

velocidad = distancia_km/tiempo_horas

#3. preparar mensajes con caracteres de escape \ y replicacion

separador="-"*15
mensaje_final = "\n"+"REPORTE"+"\n"+separador
detalles = "\nConductor: "+nombre_conductor+"\nVelocidad: "+str(velocidad)

#4. Resultados

print(mensaje_final)
print(detalles)
print(separador)
print("n Precione Enter para cerrar el programa")
input()
