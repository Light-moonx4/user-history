coders = {
    "1": {
        "id": 1025436,
        "nombre": "jonathan",
        "apellido": "escorcia",
        "lvl_english": "A-1",
        "edad": 20,
    },
    "2": {
        "id": 1022563,
        "nombre": "zero",
        "apellido": "night",
        "lvl_english": "A-2",
        "edad": 24,
    },
    "3": {
        "id": 1236445,
        "nombre": "solomon",
        "apellido": "kane",
        "lvl_english": "B-2",
        "edad": 29,
    },
    "4": {
        "id": 1356459,
        "nombre": "cid",
        "apellido": "de la luz",
        "lvl_english": "C-1",
        "edad": 25,
    },
}


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debes ingresar un número válido.")


nice = False

while not nice:
    print("\n--- MENÚ ---")
    print("1. Agregar coder")
    print("2. Eliminar coder")
    print("3. Buscar coder por ID")
    print("4. Ver todos los coders")
    print("5. Salir")

    select = leer_entero("Digite que desea hacer (1-5): ")

    # 🔹 AGREGAR
    if select == 1:
        id = leer_entero("Digite su número de ID: ")
        nombre = input("Digite un nombre: ")
        apellido = input("Digite un apellido: ")
        edad = leer_entero("Digite su edad: ")
        ingles = input("Digite su nivel de inglés: ")

        # evitar claves repetidas
        nueva_coder = str(max([int(k) for k in coders.keys()]) + 1)

        coders[nueva_coder] = {
            "id": id,
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "lvl_english": ingles,
        }

        print("✅ Coder agregado correctamente\n")

    # 🔹 ELIMINAR
    elif select == 2:
        numero = input("Digite el número del coder a eliminar: ")

        if numero in coders:
            nombre = coders[numero]["nombre"]
            del coders[numero]
            print(f"✅ Eliminaste a {nombre}")
        else:
            print("❌ Ese coder no existe")

    # 🔹 BUSCAR
    elif select == 3:
        busqueda = leer_entero("Digite el ID del coder que desea buscar: ")

        coder_encontrado = None

        for llave, datos in coders.items():
            if datos["id"] == busqueda:
                coder_encontrado = datos

        if coder_encontrado:
            print("\n🔎 Coder encontrado:")
            print(coder_encontrado)
        else:
            print("❌ Coder no encontrado")

    # 🔹 VER TODOS
    elif select == 4:
        print("\n📋 LISTA DE CODERS:")
        for clave, datos in coders.items():
            print(f"\nClave: {clave}")
            print(f"ID: {datos['id']}")
            print(f"Nombre: {datos['nombre']} {datos['apellido']}")
            print(f"Edad: {datos['edad']}")
            print(f"Inglés: {datos['lvl_english']}")

    # 🔹 SALIR
    elif select == 5:
        print("👋 Gracias por usar el sistema")
        nice = True

    else:
        print("❌ Opción inválida")
