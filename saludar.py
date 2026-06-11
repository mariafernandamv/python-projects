def saludar() :
    saludo = f"!Hola desde  mi primer función"
    print(saludo)
saludar()

def saludar(nom):
    nom= f"Hola,{nom}"
    print(nom)
saludar("Fernanda")

def bienvenida(nombre, idioma="Español"):
    if idioma == "Español":
        print(f"Hola, {nombre}")
    elif idioma == "Inglés":
        print(f"Hello, {nombre}")
    elif idioma == "Portugués":
        print(f"Olá, {nombre}")
    else:
        print("Opción no válida")

bienvenida("Daniel",idioma="Inglés")
bienvenida("Damiam",idioma="Portugués")
bienvenida("Roxinia")
#sac area de un circulo pi * radio elevado a dos 
#para sacar una biblioteca con la palabra import  math # en este caso es para mate 
#math. pi 
#funcion area de circulo recibir radio de parametro y se la,a la funcion 
#elevado **