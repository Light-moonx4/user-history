# servicios.py

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario.
    """
    inventario.append({
        "nombre": nombre.lower(),
        "precio": precio,
        "cantidad": cantidad
    })


def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario.
    """
    if not inventario:
        print("Inventario vacío.")
        return

    for p in inventario:
        print(f"Nombre: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre.
    Retorna el producto o None.
    """
    for p in inventario:
        if p["nombre"] == nombre.lower():
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza precio y/o cantidad de un producto.
    """
    producto = buscar_producto(inventario, nombre)
    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        return True
    return False


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario.
    """
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        return True
    return False


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario.
    Retorna un diccionario.
    """
    if not inventario:
        return None

    subtotal = lambda p: p["precio"] * p["cantidad"]

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_mayor_stock": (producto_mayor_stock["nombre"], producto_mayor_stock["cantidad"])
    }