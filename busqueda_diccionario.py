# Creamos un diccionario con códigos de productos como claves y precios como valores
productos = {
    'P001': 15.50,
    'P002': 22.00,
    'P003': 9.75,
    'P004': 18.30
}

# Solicitamos al usuario que ingrese un código de producto
codigo = input("Ingresa el código del producto en mayuscula : ")

# Verificamos si el código existe
if codigo in productos:
    # Si existe, mostramos el precio 
    print(f"El precio del producto {codigo} es: ${productos[codigo]}")
else:
    # Si no existe, mostramos un mensaje de error
    print("Código de producto no encontrado.")
