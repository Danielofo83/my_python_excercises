class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Precio: ${self.precio:.2f}"


# Lista para almacenar los productos
productos = []

# Variable para generar IDs automáticos
contador_id = 1


# Crear un producto
def crear_producto():
    global contador_id

    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))

    producto = Producto(contador_id, nombre, precio)
    productos.append(producto)

    contador_id += 1

    print("✅ Producto agregado exitosamente.")


# Leer todos los productos
def leer_productos():
    if len(productos) == 0:
        print("⚠ No hay productos registrados.")
    else:
        print("\n📜 Lista de productos:")
        for producto in productos:
            print(producto)


# Actualizar un producto
def actualizar_producto():
    id_buscar = int(input("Ingrese el ID del producto a actualizar: "))

    for producto in productos:
        if producto.id == id_buscar:
            producto.nombre = input("Nuevo nombre: ")
            producto.precio = float(input("Nuevo precio: "))
            print("✅ Producto actualizado.")
            return

    print("⚠ Producto no encontrado.")


# Eliminar un producto
def eliminar_producto():
    id_buscar = int(input("Ingrese el ID del producto a eliminar: "))

    for producto in productos:
        if producto.id == id_buscar:
            productos.remove(producto)
            print("✅ Producto eliminado.")
            return

    print("⚠ Producto no encontrado.")


# Programa principal
def main():
    while True:
        print("\n=== CRUD de Productos ===")
        print("1. Crear producto")
        print("2. Leer productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            crear_producto()
        elif opcion == "2":
            leer_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida.")


# Ejecutar el programa
if __name__ == "__main__":
    main()
    