
class Perro:
    
    # Método constructor que recibe nombre y raza
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    #  Método ladrar que imprime un mensaje usando el nombre del perro
    def ladrar(self):
        print(f"{self.nombre} dice ¡Guau!")

# Creamos una instancia de la clase Perro
mi_perro = Perro("Pintas", "Casisagua")

# Invocamos el método ladrar
mi_perro.ladrar()
 

  