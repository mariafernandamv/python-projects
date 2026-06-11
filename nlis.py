ciudades = ["San José", "Heredia", "Cartago", "Limón"]
print("Cantidad de ciudades", len(ciudades))
print("¿Londres está en la lista?", "Londres" in ciudades)
print("¿Tokio está en la lista?", "Tokio" in ciudades) 

mixta =[4, 3.46, "Botas", False]
print(mixta)
for elementos in mixta: 
    print(type(elementos))
