import os
import csv

def confirm_action(message):
    """
    Solicita confirmación del usuario para una acción.
    
    Args:
        message (str): Mensaje a mostrar al usuario
    
    Returns:
        bool: True si el usuario confirma, False en caso contrario
    """
    while True:
        response = input(f"{message} (s/n): ").lower().strip()
        if response in ['s', 'si', 'sí', 'yes', 'y']:
            return True
        elif response in ['n', 'no', 'nop', 'nope']:
            return False
        else:
            print("Por favor, responde 's' para sí o 'n' para no.")

def ensure_directory_exists(directory_path, ask_confirmation=True):
    """
    Verifica si un directorio existe y lo crea si es necesario.
    
    Args:
        directory_path (str): Ruta del directorio a verificar/crear
        ask_confirmation (bool): Si debe solicitar confirmación al usuario
    
    Returns:
        bool: True si el directorio existe o se creó, False en caso contrario
    """
    if os.path.exists(directory_path):
        if os.path.isdir(directory_path):
            print(f"✓ El directorio '{directory_path}' ya existe.")
            return True
        else:
            print(f"❌ Error: '{directory_path}' existe pero no es un directorio.")
            return False
    
    # El directorio no existe
    print(f"📁 El directorio '{directory_path}' no existe.")
    
    if ask_confirmation:
        if confirm_action(f"¿Deseas crear el directorio '{directory_path}'?"):
            try:
                os.makedirs(directory_path)
                print(f"✓ Directorio '{directory_path}' creado exitosamente.")
                return True
            except PermissionError:
                print(f"❌ Error: No tienes permisos para crear el directorio '{directory_path}'.")
                return False
            except Exception as e:
                print(f"❌ Error inesperado al crear el directorio: {e}")
                return False
        else:
            print(f"⏹️ Operación cancelada por el usuario.")
            return False
    else:
        # Crear el directorio sin confirmación
        try:
            os.makedirs(directory_path)
            print(f"✓ Directorio '{directory_path}' creado automáticamente.")
            return True
        except Exception as e:
            print(f"❌ Error al crear el directorio: {e}")
            return False

def read_csv(filename):
    """
    Lee un archivo CSV y devuelve su contenido como lista de diccionarios.
    
    Args:
        filename (str): Ruta al archivo CSV
    
    Returns:
        list: Lista de diccionarios representando las filas CSV
        None: Si el archivo no puede ser leído
    """
    try:
        # Verificar si el archivo existe
        if not os.path.exists(filename):
            raise FileNotFoundError(f"El archivo '{filename}' no fue encontrado.")
        
        # Verificar si el archivo está vacío
        if os.path.getsize(filename) == 0:
            raise ValueError(f"El archivo '{filename}' está vacío.")
        
        # Leer archivo CSV
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            rows = list(csv_reader)
            
            if not rows:
                print(f"⚠️ Advertencia: El archivo CSV '{filename}' solo contiene encabezados o está vacío.")
                return []
            
            print(f"✓ Se leyeron exitosamente {len(rows)} filas de '{filename}'")
            return rows
            
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        return None
    except PermissionError as e:
        print(f"❌ Error: Permiso denegado - {e}")
        return None
    except csv.Error as e:
        print(f"❌ Error: Error de parsing CSV - {e}")
        return None
    except Exception as e:
        print(f"❌ Error inesperado al leer el archivo: {e}")
        return None

def write_file(filename, content, mode='w'):
    """
    Escribe contenido en un archivo con manejo de errores.
    
    Args:
        filename (str): Ruta al archivo de salida
        content (str/bytes/list): Contenido a escribir
        mode (str): Modo de escritura ('w' para sobrescribir, 'a' para añadir)
    
    Returns:
        bool: True si es exitoso, False en caso contrario
    """
    try:
        # Validación de entrada
        if not filename or not isinstance(filename, str):
            raise ValueError("El nombre del archivo debe ser una cadena no vacía")
        
        if content is None:
            raise ValueError("El contenido no puede ser None")
        
        # Crear directorio si no existe
        directory = os.path.dirname(filename)
        if directory:
            if not ensure_directory_exists(directory, ask_confirmation=True):
                return False
        
        # Escribir contenido en el archivo
        with open(filename, mode, encoding='utf-8') as file:
            if isinstance(content, list):
                file.writelines(content)
            else:
                file.write(str(content))
        
        # Obtener tamaño del archivo
        file_size = os.path.getsize(filename)
        print(f"✓ Se escribieron exitosamente {file_size} bytes en '{filename}'")
        return True
        
    except ValueError as e:
        print(f"❌ Error: Entrada inválida - {e}")
        return False
    except PermissionError as e:
        print(f"❌ Error: Permiso denegado - {e}")
        return False
    except OSError as e:
        print(f"❌ Error: Error del sistema operativo - {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado al escribir el archivo: {e}")
        return False

def create_sample_csv(filename):
    """
    Crea un archivo CSV de ejemplo para demostración.
    
    Args:
        filename (str): Ruta donde crear el archivo CSV
    
    Returns:
        bool: True si es exitoso, False en caso contrario
    """
    try:
        # Verificar y crear el directorio si es necesario
        directory = os.path.dirname(filename)
        if directory:
            print(f"\n📁 Preparando para crear archivo CSV en '{directory}'...")
            if not ensure_directory_exists(directory, ask_confirmation=True):
                print("⏹️ No se creará el archivo CSV.")
                return False
        
        # Datos de ejemplo
        headers = ['Nombre', 'Edad', 'País', 'Ocupación']
        data = [
            ['Alice Johnson', '28', 'USA', 'Ingeniera'],
            ['Bob Smith', '35', 'Canadá', 'Diseñador'],
            ['Carlos García', '42', 'México', 'Profesor'],
            ['Diana Patel', '31', 'India', 'Médica'],
            ['Elena Kim', '28', 'Corea del Sur', 'Desarrolladora']
        ]
        
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(headers)
            csv_writer.writerows(data)
        
        print(f"✓ Archivo CSV de ejemplo creado exitosamente: '{filename}'")
        print(f"  - {len(data)} registros creados")
        return True
        
    except Exception as e:
        print(f"❌ Error al crear archivo CSV de ejemplo: {e}")
        return False

def display_csv_content(rows, max_display=5):
    """
    Muestra el contenido del CSV en formato tabular.
    
    Args:
        rows (list): Lista de diccionarios del CSV
        max_display (int): Número máximo de filas a mostrar
    """
    if not rows:
        print("No hay datos para mostrar.")
        return
    
    print("\n" + "="*80)
    print("CONTENIDO DEL CSV")
    print("="*80)
    
    # Mostrar encabezados
    headers = rows[0].keys() if rows else []
    header_line = " | ".join(f"{h:20}" for h in headers)
    print(header_line)
    print("-"*80)
    
    # Mostrar filas
    display_count = min(len(rows), max_display)
    for i, row in enumerate(rows[:display_count]):
        row_values = [f"{row.get(h, ''):20}" for h in headers]
        print(" | ".join(row_values))
    
    if len(rows) > max_display:
        print(f"... y {len(rows) - max_display} filas más")
    
    print("="*80)

def analyze_csv_data(rows):
    """
    Realiza análisis básico de los datos CSV.
    
    Args:
        rows (list): Lista de diccionarios del CSV
    """
    if not rows:
        return
    
    print("\n" + "="*80)
    print("ANÁLISIS DE DATOS")
    print("="*80)
    
    # Contar total de filas
    print(f"📊 Total de Registros: {len(rows)}")
    
    # Si existe la columna Edad, calcular estadísticas
    if 'Edad' in rows[0]:
        edades = []
        for row in rows:
            try:
                edad = int(row['Edad'])
                edades.append(edad)
            except (ValueError, TypeError):
                pass
        
        if edades:
            print(f"📈 Estadísticas de Edad:")
            print(f"   - Promedio: {sum(edades)/len(edades):.1f} años")
            print(f"   - Mínima: {min(edades)} años")
            print(f"   - Máxima: {max(edades)} años")
    
    # Contar países únicos
    if 'País' in rows[0]:
        paises = [row['País'] for row in rows if row.get('País')]
        paises_unicos = set(paises)
        print(f"🌍 Países: {len(paises_unicos)} únicos")
        print(f"   - {', '.join(sorted(paises_unicos))}")
    
    # Distribución de ocupaciones
    if 'Ocupación' in rows[0]:
        ocupaciones = [row['Ocupación'] for row in rows if row.get('Ocupación')]
        from collections import Counter
        contador_ocupaciones = Counter(ocupaciones)
        print(f"💼 Distribución de Ocupaciones:")
        for oc, count in contador_ocupaciones.most_common():
            print(f"   - {oc}: {count} persona(s)")
    
    print("="*80)

def main():
    """
    Función principal para demostrar manipulación de archivos y manejo de errores.
    """
    print("\n" + "="*80)
    print("   EJERCICIO DE MANIPULACIÓN DE ARCHIVOS Y MANEJO DE ERRORES")
    print("="*80)
    
    # ============================================
    # DEMOSTRACIÓN 1: Verificación de Directorios
    # ============================================
    print("\n📁 DEMOSTRACIÓN 1: Verificación y Creación de Directorios")
    print("-"*80)
    
    # Probar verificación de directorio
    test_dir = 'data'
    print(f"\nVerificando directorio '{test_dir}':")
    if ensure_directory_exists(test_dir, ask_confirmation=True):
        print("✓ Directorio listo para usar")
    
    # ============================================
    # DEMOSTRACIÓN 2: Creación de Archivo CSV
    # ============================================
    print("\n\n📁 DEMOSTRACIÓN 2: Creación de Archivo CSV")
    print("-"*80)
    
    sample_csv = 'data/sample_data.csv'
    
    # Verificar si el archivo ya existe
    if os.path.exists(sample_csv):
        print(f"\nEl archivo '{sample_csv}' ya existe.")
        if confirm_action("¿Deseas sobrescribirlo?"):
            create_sample_csv(sample_csv)
        else:
            print("⏹️ Se mantendrá el archivo existente.")
    else:
        create_sample_csv(sample_csv)
    
    # ============================================
    # DEMOSTRACIÓN 3: Lectura de Archivo CSV
    # ============================================
    print("\n\n📁 DEMOSTRACIÓN 3: Lectura de Archivo CSV")
    print("-"*80)
    
    # Test 1: Leer CSV existente
    print("\n[Test 1] Leyendo archivo CSV existente:")
    rows = read_csv(sample_csv)
    if rows is not None:
        display_csv_content(rows)
        analyze_csv_data(rows)
    
    # Test 2: Leer CSV inexistente (Manejo de errores)
    print("\n[Test 2] Leyendo archivo CSV inexistente:")
    rows = read_csv('data/nonexistent.csv')
    if rows is None:
        print("✓ El error fue capturado y manejado correctamente")
    
    # Test 3: Leer CSV vacío
    print("\n[Test 3] Leyendo archivo CSV vacío:")
    empty_csv = 'data/empty.csv'
    try:
        # Crear archivo vacío
        with open(empty_csv, 'w') as f:
            pass
        rows = read_csv(empty_csv)
        if rows is None:
            print("✓ El error de archivo vacío fue capturado")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # ============================================
    # DEMOSTRACIÓN 4: Escritura de Archivos
    # ============================================
    print("\n\n📁 DEMOSTRACIÓN 4: Escritura de Archivos")
    print("-"*80)
    
    # Test 1: Escribir archivo de texto simple
    print("\n[Test 1] Escribiendo archivo de texto:")
    status = write_file('results/output.txt', '¡Éxito! El archivo fue escrito correctamente.')
    if status:
        print("✓ Escritura de archivo exitosa")
    
    # Test 2: Escribir con nombre de archivo inválido
    print("\n[Test 2] Escribiendo con nombre de archivo inválido:")
    status = write_file('', 'Esto debería fallar')
    if not status:
        print("✓ El error de nombre inválido fue capturado")
    
    # Test 3: Escribir múltiples líneas
    print("\n[Test 3] Escribiendo múltiples líneas:")
    lines = [
        "Línea 1: Esta es la primera línea\n",
        "Línea 2: Esta es la segunda línea\n",
        "Línea 3: Esta es la tercera línea\n"
    ]
    status = write_file('results/multi_line.txt', lines)
    if status:
        print("✓ Escritura de múltiples líneas exitosa")
    
    # Test 4: Añadir a archivo existente
    print("\n[Test 4] Añadiendo a archivo existente:")
    status = write_file('results/output.txt', '\n¡Contenido añadido!', mode='a')
    if status:
        print("✓ Adición a archivo exitosa")
    
    # ============================================
    # DEMOSTRACIÓN 5: Operaciones Combinadas
    # ============================================
    print("\n\n📁 DEMOSTRACIÓN 5: Operaciones Combinadas")
    print("-"*80)
    
    # Leer CSV y escribir análisis
    print("\nLeyendo CSV y escribiendo análisis:")
    rows = read_csv(sample_csv)
    if rows is not None:
        # Generar resumen
        summary = []
        summary.append("="*60 + "\n")
        summary.append("REPORTE DE ANÁLISIS CSV\n")
        summary.append("="*60 + "\n\n")
        summary.append(f"Total de Registros: {len(rows)}\n\n")
        
        if 'País' in rows[0]:
            paises = [row['País'] for row in rows if row.get('País')]
            paises_unicos = set(paises)
            summary.append(f"Países: {', '.join(sorted(paises_unicos))}\n\n")
        
        if 'Edad' in rows[0]:
            edades = []
            for row in rows:
                try:
                    edad = int(row['Edad'])
                    edades.append(edad)
                except (ValueError, TypeError):
                    pass
            if edades:
                summary.append("Estadísticas de Edad:\n")
                summary.append(f"  Promedio: {sum(edades)/len(edades):.1f}\n")
                summary.append(f"  Mínima: {min(edades)}\n")
                summary.append(f"  Máxima: {max(edades)}\n")
        
        # Escribir resumen
        write_file('results/analysis_report.txt', summary)
        
        # Verificar que el archivo fue creado
        if os.path.exists('results/analysis_report.txt'):
            print("\n✓ Reporte de análisis creado exitosamente!")
            print("  - Archivo: 'results/analysis_report.txt'")
    
    # ============================================
    # DEMOSTRACIÓN 6: Listado de Archivos Creados
    # ============================================
    print("\n\n📁 DEMOSTRACIÓN 6: Archivos Creados")
    print("-"*80)
    
    print("\n📂 Archivos creados en el directorio 'data/':")
    if os.path.exists('data'):
        for file in os.listdir('data'):
            if os.path.isfile(os.path.join('data', file)):
                size = os.path.getsize(os.path.join('data', file))
                print(f"  • {file} ({size} bytes)")
    
    print("\n📂 Archivos creados en el directorio 'results/':")
    if os.path.exists('results'):
        for file in os.listdir('results'):
            if os.path.isfile(os.path.join('results', file)):
                size = os.path.getsize(os.path.join('results', file))
                print(f"  • {file} ({size} bytes)")
    
    # ============================================
    # DEMOSTRACIÓN 7: Limpieza Opcional
    # ============================================
    print("\n\n📁 DEMOSTRACIÓN 7: Limpieza Opcional")
    print("-"*80)
    
    if confirm_action("\n¿Deseas eliminar los directorios 'data' y 'results'?"):
        import shutil
        try:
            if os.path.exists('data'):
                shutil.rmtree('data')
                print("✓ Directorio 'data' eliminado")
            if os.path.exists('results'):
                shutil.rmtree('results')
                print("✓ Directorio 'results' eliminado")
        except Exception as e:
            print(f"❌ Error al eliminar directorios: {e}")
    else:
        print("⏹️ Los directorios y archivos se mantienen.")
    
    print("\n" + "="*80)
    print("✅ ¡Todas las demostraciones completadas exitosamente!")
    print("="*80)

# Ejecutar la función principal
if __name__ == "__main__":
    main()