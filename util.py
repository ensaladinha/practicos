def Mostrar_menu(lista):
    while True:
        try:
            op = int(input("Eliga una opcion entre 1 y 4: "))
            if 1 <= op <= len(lista):
                return lista[op - 1]
        except ValueError:
            pass
        print("Opción inválida. Intente de nuevo.")