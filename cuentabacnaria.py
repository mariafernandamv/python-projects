# Definimos la clase CuentaBancaria
class CuentaBancaria:
    
    #  Atributo de clase: compartido por todas las instancias
    tasa_interes = 0.05

    # Constructor con atributo de instancia: único para cada objeto
    def __init__(self):
        self.saldo = 0

# Creamos dos instancias de CuentaBancaria
cuenta1 = CuentaBancaria()
cuenta2 = CuentaBancaria()

#  Imprimimos el atributo de clase directamente desde la clase
print(f"Tasa de interés: {CuentaBancaria.tasa_interes}")

# Modificamos el saldo de cuenta1 y lo imprimimos
cuenta1.saldo = 1000
print(f"Saldo de cuenta1: {cuenta1.saldo}")

# También podemos mostrar que cuenta2 sigue con saldo 0
print(f"Saldo de cuenta2: {cuenta2.saldo}")
