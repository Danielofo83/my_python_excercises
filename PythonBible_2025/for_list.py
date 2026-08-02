
lista_pacientes = [
    {
        'Nombre': 'Juan',
        'Apellido': 'Pérez',
        'Edad': 35,
        'Peso': 70.5,
        'Telefono': '5551234567',
        'Correo': 'juan.perez@example.com',
        'NSS': '12345678901',
        'CURP': 'PEMJ800101HDFRRN01'
    },
    {
        'Nombre': 'María',
        'Apellido': 'Gómez',
        'Edad': 28,
        'Peso': 62.3,
        'Telefono': '5559876543',
        'Correo': 'maria.gomez@example.com',
        'NSS': '98765432109',
        'CURP': 'GOML920515MDFMSR02'
    },{
        'Nombre': 'Alicia',
        'Apellido': 'Martinez',
        'Edad': 33,
        'Peso': 72.5,
        'Telefono': '55531234567',
        'Correo': 'alicia.Martinezz@example.com',
        'NSS': '123433333901',
        'CURP': 'LICHAMA800101HDFRRN01'
    }
]

# Para agregar otro paciente manualmente
nuevo_paciente = {
    'Nombre': 'Carlos',
    'Apellido': 'López',
    'Edad': 42,
    'Peso': 85.0,
    'Telefono': '5555678912',
    'Correo': 'carlos.lopez@example.com',
    'NSS': '45678901234',
    'CURP': 'LOCA750620HDFPPS03'
}

lista_pacientes.append(nuevo_paciente)

# Para mostrar los pacientes
for paciente in lista_pacientes:
    print("\nDatos del paciente:")
    for clave, valor in paciente.items():
        print(f"{clave}: {valor}")


# Uso de defaultdict para valores por defecto
from collections import defaultdict

contador = defaultdict(int)
palabras = ["manzana", "banana", "manzana", "naranja"," manzana", "banana", "manzana", "banana"]

for palabra in palabras:
    contador[palabra] += 1

print(contador)  # Salida: defaultdict(<class 'int'>, {'manzana': 2, 'banana': 1, 'naranja': 1})


