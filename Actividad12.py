try:
    def quick_sort(lista):
        if len(lista) <= 1:
            return lista

        pivote = lista[0]
        menores = [x for x in lista if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista if x > pivote]

        return quick_sort(menores) + iguales + quick_sort(mayores)


    repartidores = {}
    cantidad = int(input("¿Cuántos repartidores desea ingresar? "))

    for i in range(cantidad):
        print(f"\nRepartidor #{i + 1}")
        while True:
            nombre = input("Ingrese el nombre del Repartidor: ")
            if nombre in repartidores:
                print("El nombre del Repartidor ya existe")
            else:
                break
        while True:
            entregas = int(input("El número de paquetes entregados: "))
            if entregas < 0:
                print("No puede ingresar entregas de forma negativa")
            else:
                break
        zona = input("La zona en la que trabaja el Repartidor: ")

        repartidores[nombre] = {
            'zona': zona,
            'entregas': entregas
        }

    resultado = quick_sort(list(repartidores.keys()))

    print("\n--- Repartidores ordenados por entregas ---")
    for nombre in resultado:
        repartidor = repartidores[nombre]
        print(f"\nNombre: {nombre}")
        print(f"Paquetes entregados: {repartidor['entregas']}")
        print(f"Zona: {repartidor['zona']}")


except:
    print("Hubo un error")