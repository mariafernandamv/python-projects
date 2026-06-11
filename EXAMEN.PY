# MATRIZ 3x3
parqueo = [["Libre" for c in range(3)] for f in range(3)]

while True:
    print("\n====== MICITT-DRIVE ======")
    print("1. Ver Estado")
    print("2. Parquear Vehículo")
    print("3. Reporte")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    # OPCIÓN 1: VER TABLA
    if opcion == "1":
        print("\nEstado del Parqueo:")
        for f in range(3):
            for c in range(3):
                print(f"{parqueo[f][c]:^10}", end=" ")
            print()

    # OPCIÓN 2: PARQUEAR
    elif opcion == "2":
        try:
            fila = int(input("Fila (1-3): ")) - 1
            columna = int(input("Columna (1-3): ")) - 1

            if 0 <= fila < 3 and 0 <= columna < 3:

                # Si está libre → pide placa
                if parqueo[fila][columna] == "Libre":
                    placa = input("Ingrese la placa: ")
                    parqueo[fila][columna] = placa
                    print("Vehículo parqueado correctamente.")

                # Si está ocupado → avisa
                else:
                    print("Espacio Ocupado.")

                # Mostrar cuántos hay ocupados después de intentar
                ocupados = 0
                for fila2 in parqueo:
                    for espacio in fila2:
                        if espacio != "Libre":
                            ocupados += 1

                print("Espacios ocupados actualmente:", ocupados)

            else:
                print("Fuera de rango.")

        except:
            print("Error en datos.")

    # OPCIÓN 3: REPORTE
    elif opcion == "3":
        ocupados = 0
        for fila in parqueo:
            for espacio in fila:
                if espacio != "Libre":
                    ocupados += 1

        print("\nReporte:")
        print("Ocupados:", ocupados)
        print("Libres:", 9 - ocupados)

    # SALIR
    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")