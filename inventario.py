# Solicitar el nombre del producto
nombre = input("Ingrese el nombre del producto: ")

# Solicitar el precio
precio = input("Ingrese el precio del producto: ")

# Validar si el precio es numérico
if precio.replace('.', '', 1).isdigit():
    precio = float(precio)
else:
    print("Error: el precio debe ser un número.")
    precio = float(input("Ingrese nuevamente el precio: "))

# Solicitar la cantidad
cantidad = input("Ingrese la cantidad del producto: ")

# Validar si la cantidad es un número entero
if cantidad.isdigit():
    cantidad = int(cantidad)
else:
    print("Error: la cantidad debe ser un número entero.")
    cantidad = int(input("Ingrese nuevamente la cantidad: "))

# Calcular el costo total
costo_total = precio * cantidad

# Mostrar resultados
print("Producto:", nombre, "| Precio:", precio, "| Cantidad:", cantidad, "| Total:", costo_total)

# Este programa solicita el nombre, precio y cantidad de un producto,
# verifica que los datos numéricos sean válidos, calcula el costo total
# multiplicando el precio por la cantidad y muestra el resultado.