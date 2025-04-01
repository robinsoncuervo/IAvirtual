productos = {
    "001": {"nombre": "Procesador", "precio": 200, "cantidad": 5},
    "002": {"nombre": "Tarjeta de video", "precio": 300, "cantidad": 3},
    "003": {"nombre": "Memoria RAM", "precio": 100, "cantidad": 10},
    "004": {"nombre": "Disco SSD", "precio": 120, "cantidad": 6},
    "005": {"nombre": "Disco HDD", "precio": 80, "cantidad": 7},
    "006": {"nombre": "Fuente de poder", "precio": 75, "cantidad": 4},
    "007": {"nombre": "Placa base", "precio": 150, "cantidad": 3},
    "008": {"nombre": "Gabinete", "precio": 90, "cantidad": 5},
    "009": {"nombre": "Monitor", "precio": 180, "cantidad": 2},
    "010": {"nombre": "Teclado", "precio": 25, "cantidad": 9},
    "011": {"nombre": "Mouse", "precio": 20, "cantidad": 12},
    "012": {"nombre": "Ventilador", "precio": 15, "cantidad": 8}
}
bandera = True
while bandera:
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Mostrar todos los productos")
    print("4. Salir del programa")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        codigo = input("Ingrese el código del producto: ")
        if codigo in productos:
            print("Ya existe un producto con este codigo")
        else: 
             nombre = input("Ingrese el nombre del producto: ")
             precio = float(input("Ingrese el precio del producto: "))
             cantidad = int(input("Ingrese la cantidad del producto: "))             
             productos[codigo] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
             print("Producto agregado")
    elif opcion == 2:          
                criterio = input("¿Desea buscar por 'codigo' o por 'nombre'?: ").lower()
                if criterio == "codigo":
                    codigo = input("Ingrese el código del producto: ")
                    if codigo in productos:
                        print(productos[codigo])
                    else:
                        print("Producto no encontrado por código")
                elif criterio == "nombre":
                    nombre = input("Ingrese el nombre del producto: ").lower()
                    codigos = list(productos.keys())
                    i = 0
                    encontrado = False
                    while i < len(codigos):
                        codigo_actual = codigos[i]
                        producto_actual = productos[codigo_actual]
                        if producto_actual["nombre"].lower() == nombre:
                            print(f"Código: {codigo_actual} -> {producto_actual}")
                            encontrado = True
                        i += 1
                    if not encontrado:
                        print("Producto no encontrado por nombre")
                else:
                    print("Criterio no válido. Use 'codigo' o 'nombre'")
    elif opcion == 3:
            print(productos)
    elif opcion == 4:
            bandera = False
    else:
            print("Opción no válida")
    print("Fin del programa")