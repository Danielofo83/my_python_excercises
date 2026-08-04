

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

with open ("usuario.txt","a") as f:
    f.write(f"Nombre: {nombre}, Edad: {edad}\n")    
    f.write("-" * 30 + "\n")


def leer_archivo():
    with open ("usuario.txt","r") as f:
        contenido = f.read()
        print(contenido)

