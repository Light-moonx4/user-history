# app.py

from servicios import *
from archivos import *


def pedir_float(mensaje):
    valido = False

    while not valido:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("No puede ser negativo.")
            else:
                valido = True
        except:
            print("Ingrese un número válido.")

    return valor


def pedir_int(mensaje):
    valido = False

    while not valido:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("No puede ser negativo.")
            else:
                valido = True
        except:
            print("Ingrese un entero válido.")

    return valor


inventario = []
opcion = 0

while opcion != 9:

    print("\n--- MENÚ ---")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    try:
        opcion = int(input("Seleccione opción: "))
    except:
        print("Opción inválida.")
        continue

    # AGREGAR
    if opcion == 1:
        nombre = input("Nombre: ")
        precio = pedir_float("Precio: ")
        cantidad = pedir_int("Cantidad: ")

        agregar_producto(inventario, nombre, precio, cantidad)
        print("Producto agregado.")

    # MOSTRAR
    elif opcion == 2:
        mostrar_inventario(inventario)

    # BUSCAR
    elif opcion == 3:
        nombre = input("Nombre a buscar: ")
        p = buscar_producto(inventario, nombre)

        if p:
            print(p)
        else:
            print("No encontrado.")

    # ACTUALIZAR
    elif opcion == 4:
        nombre = input("Nombre a actualizar: ")

        precio = input("Nuevo precio (enter para omitir): ")
        cantidad = input("Nueva cantidad (enter para omitir): ")

        try:
            nuevo_precio = float(precio) if precio else None
            if nuevo_precio is not None and nuevo_precio < 0:
                print("Precio inválido.")
                nuevo_precio = None
        except:
            print("Precio inválido.")
            nuevo_precio = None

        try:
            nueva_cantidad = int(cantidad) if cantidad else None
            if nueva_cantidad is not None and nueva_cantidad < 0:
                print("Cantidad inválida.")
                nueva_cantidad = None
        except:
            print("Cantidad inválida.")
            nueva_cantidad = None

        if actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad):
            print("Actualizado.")
        else:
            print("No encontrado.")

    # ELIMINAR
    elif opcion == 5:
        nombre = input("Nombre a eliminar: ")

        if eliminar_producto(inventario, nombre):
            print("Eliminado.")
        else:
            print("No encontrado.")

    # ESTADÍSTICAS
    elif opcion == 6:
        stats = calcular_estadisticas(inventario)

        if stats:
            print("\n--- ESTADÍSTICAS ---")
            print("Unidades:", stats["unidades_totales"])
            print("Valor total:", stats["valor_total"])
            print("Más caro:", stats["producto_mas_caro"])
            print("Mayor stock:", stats["producto_mayor_stock"])
        else:
            print("Inventario vacío.")

    # GUARDAR CSV
    elif opcion == 7:
        ruta = input("Ruta archivo (ej: datos.csv): ")
        guardar_csv(inventario, ruta)

    # CARGAR CSV
    elif opcion == 8:
        ruta = input("Ruta archivo: ")
        nuevos, errores = cargar_csv(ruta)

        if nuevos:
            decision = input("¿Sobrescribir inventario? (S/N): ").lower()

            if decision == "s":
                inventario = nuevos
                accion = "Reemplazado"
            else:
                # FUSIÓN
                for nuevo in nuevos:
                    existente = buscar_producto(inventario, nuevo["nombre"])
                    if existente:
                        existente["cantidad"] += nuevo["cantidad"]
                        existente["precio"] = nuevo["precio"]
                    else:
                        inventario.append(nuevo)
                accion = "Fusionado"

            print(f"{accion}. {len(nuevos)} productos cargados.")
            print(f"{errores} filas inválidas omitidas.")
        else:
            print("No se cargaron datos.")

    elif opcion == 9:
        print("Saliendo...")

    else:
        print("Opción inválida.")