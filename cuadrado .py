# 1. Definimos la clase Cuadrado
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

# Definimos la clase Triangulo
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

# Definimos una función objeto con el método calcular_area
def imprimir_area(objeto):
    area = objeto.calcular_area()
    print(f"El área es: {area}")

#Le damos valores 
cuadrado = Cuadrado(4)
triangulo = Triangulo(6, 3)

# Llamamos a la función
imprimir_area(cuadrado)   
imprimir_area(triangulo)  
