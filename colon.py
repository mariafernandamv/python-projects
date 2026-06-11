import tkinter as tk

# Tasas de conversión
tasa_dolar_colon = 550    # 1 USD = 550 colones
tasa_euro_colon = 600     # 1 EUR = 600 colones

# Función para convertir
def convertir():
    try:
        cantidad = float(pantalla.get())
        origen = moneda_origen.get()
        destino = moneda_destino.get()

        # Convertir todo a colones primero
        if origen == "USD":
            cantidad_en_colones = cantidad * tasa_dolar_colon
        elif origen == "EUR":
            cantidad_en_colones = cantidad * tasa_euro_colon
        else:  # COL
            cantidad_en_colones = cantidad

        # Convertir de colones a la moneda destino
        if destino == "USD":
            resultado = cantidad_en_colones / tasa_dolar_colon
        elif destino == "EUR":
            resultado = cantidad_en_colones / tasa_euro_colon
        else:  # COL
            resultado = cantidad_en_colones

        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(round(resultado, 2)))

    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "ERROR")

def limpiar_pantalla():
    pantalla.delete(0, tk.END)

# Ventana principal
ventana = tk.Tk()
ventana.title("Convertidor de monedas")

# Entry para la cantidad
pantalla = tk.Entry(ventana, width=20, font=("arial", 16))
pantalla.grid(row=0, column=0, columnspan=3, pady=10)

# Menús desplegables para elegir monedas
moneda_origen = tk.StringVar(ventana)
moneda_origen.set("USD")
tk.OptionMenu(ventana, moneda_origen, "USD", "EUR", "COL").grid(row=1, column=0)

moneda_destino = tk.StringVar(ventana)
moneda_destino.set("COL")
tk.OptionMenu(ventana, moneda_destino, "USD", "EUR", "COL").grid(row=1, column=1)

# Botón convertir
tk.Button(ventana, text="Convertir", width=10, command=convertir).grid(row=1, column=2)

# Botón limpiar
tk.Button(ventana, text="C", width=10, command=limpiar_pantalla).grid(row=2, column=1, pady=10)

ventana.mainloop()