"""
Ejercicio 2: Lectura de archivos.
Deberas hacer que al usuario se le muestre un menú para que pueda elegir
cual de los "Readme.md" de las carpetas practicas, tests y practicas/Ejercicio1.py
desea leer.
Luego, deberás leer el archivo seleccionado y mostrar su contenido en la consola.
"""
import sys
import os

# Agregar el directorio padre al path para importar las clases auxiliares
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Teclado import Teclado

def mostrar_menu():
    """Muestra el menú de archivos disponibles para leer"""
    print("📚 EJERCICIO 2: LECTURA DE ARCHIVOS")
    print("=" * 40)
    print("Selecciona el archivo que deseas leer:")
    print()
    print("1. README.md principal del proyecto")
    print("2. README.md de la carpeta practicas/")
    print("3. README.md de la carpeta tests/")
    print("4. README.md de tests/unit_tests/")
    print("5. README.md de tests/demos/")
    print("6. Ejercicio1.py (código fuente)")
    print("0. Salir")
    print("=" * 40)

def leer_archivo(ruta_archivo):
    """Lee y muestra el contenido de un archivo"""
    try:
        # Obtener la ruta absoluta del directorio base del proyecto
        directorio_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_completa = os.path.join(directorio_base, ruta_archivo)
        
        # Abrir y leer el archivo seleccionado
        with open(ruta_completa, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            
        # Mostrar el contenido leído en consola
        print(f"\n📄 CONTENIDO DE: {ruta_archivo}")
        print("=" * 60)
        print(contenido)
        print("=" * 60)
        print(f"✅ Archivo leído exitosamente: {ruta_archivo}")
        
    except FileNotFoundError:
        print(f"❌ Error: No se pudo encontrar el archivo {ruta_archivo}")
    except PermissionError:
        print(f"❌ Error: No tienes permisos para leer el archivo {ruta_archivo}")
    except Exception as e:
        print(f"❌ Error inesperado al leer el archivo: {e}")

def ejercicio_lectura_archivos():
    """Función principal del ejercicio de lectura de archivos"""
    
    # Diccionario con las opciones y sus rutas correspondientes
    archivos_disponibles = {
        1: "README.md",
        2: "practicas/README.md", 
        3: "tests/README.md",
        4: "tests/unit_tests/README.md",
        5: "tests/demos/README.md",
        6: "practicas/Ejercicio1.py"
    }
    
    while True:
        try:
            mostrar_menu()
            
            # Leer la opción del usuario usando la clase Teclado
            opcion = Teclado.read_integer("Selecciona una opción:", min_value=0, max_value=6)
            
            if opcion == 0:
                print("\n👋 ¡Gracias por usar el lector de archivos!")
                break
            
            # Verificar si la opción existe en el diccionario
            if opcion in archivos_disponibles:
                ruta_archivo = archivos_disponibles[opcion]
                leer_archivo(ruta_archivo)
            
            # Esperar a que el usuario presione Enter para continuar
            print("\nPresiona Enter para continuar...")
            input()
            
        except KeyboardInterrupt:
            print("\n\n❌ Proceso cancelado por el usuario.")
            break
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            print("Presiona Enter para continuar...")
            input()

# Punto de entrada principal del script
if __name__ == "__main__":
    ejercicio_lectura_archivos()