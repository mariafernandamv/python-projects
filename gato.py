#  Definimos la clase base llamada Animal
class Animal:
    def comer(self):
        print("El animal está comiendo.")

# Definimos la clase derivada Gato que hereda de Animal
class Gato(Animal):
    
    #  Método Gato
    def maullar(self):
        print("Miau, miau.")

#  Creamos una instancia de Gato
mi_gato = Gato()

# Invocamos el método heredado de Animal
mi_gato.comer()

# Invocamos el método propio de Gato
mi_gato.maullar()
