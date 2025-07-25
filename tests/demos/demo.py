import sys
import os

# Agregar el directorio raíz al path para importar las clases
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Teclado import Teclado

def demo_validaciones_salvadorenas():
    """Demostración específica de validaciones salvadoreñas"""
    
    print("🇸🇻 SISTEMA DE VALIDACIONES SALVADOREÑAS")
    print("=" * 50)
    print("Este programa demuestra las validaciones específicas para El Salvador:")
    print("- DUI (Documento Único de Identidad)")
    print("- Teléfonos (celular y fijo)")
    print("- Fechas de nacimiento")
    print("=" * 50)
    
    try:
        # Información personal básica
        print("\n📋 INFORMACIÓN PERSONAL")
        print("-" * 25)
        
        nombre = Teclado.read_text("Ingresa tu nombre completo:", min_length=2, max_length=50)
        print(f"Nombre registrado: {nombre}")
        
        dui = Teclado.read_dui("Ingresa tu DUI:")
        print(f"DUI registrado: {dui}")
        
        # Información de contacto
        print("\n📞 INFORMACIÓN DE CONTACTO")
        print("-" * 30)
        
        email = Teclado.read_email("Ingresa tu correo electrónico:")
        print(f"Email registrado: {email}")
        
        print("\nTipos de teléfono en El Salvador:")
        print("- Celular: Inicia con 6 o 7")
        print("- Fijo: Inicia con 2")
        
        telefono = Teclado.read_phone("Ingresa tu número de teléfono:", strict_prefix=True)
        tipo_telefono = "Celular" if telefono[0] in ['6', '7'] else "Fijo"
        print(f"Teléfono {tipo_telefono} registrado: {telefono}")
        
        # Fecha de nacimiento
        print("\n🎂 FECHA DE NACIMIENTO")
        print("-" * 25)
        
        fecha_nacimiento = Teclado.read_date("Ingresa tu fecha de nacimiento", "dd/mm/yyyy")
        print(f"Fecha de nacimiento registrada: {fecha_nacimiento}")
        
        # Resumen final
        print("\n" + "=" * 50)
        print("✅ REGISTRO COMPLETADO EXITOSAMENTE")
        print("=" * 50)
        print("RESUMEN DE DATOS INGRESADOS:")
        print(f"Nombre: {nombre}")
        print(f"DUI: {dui}")
        print(f"Email: {email}")
        print(f"Teléfono ({tipo_telefono}): {telefono}")
        print(f"Fecha de nacimiento: {fecha_nacimiento}")
        print("=" * 50)
        print("Todos los datos han sido validados correctamente 🎉")
        
    except KeyboardInterrupt:
        print("\n\n❌ Proceso cancelado por el usuario.")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")

def demo_validaciones_flexibles():
    """Demostración de validaciones más flexibles"""
    
    print("\n\n🔧 VALIDACIONES FLEXIBLES")
    print("=" * 40)
    print("Ahora probaremos validaciones con configuraciones más flexibles:")
    
    try:
        # Teléfono sin restricción de prefijo
        print("\n📞 Teléfono internacional o especial")
        print("(Sin restricción de prefijo salvadoreño)")
        telefono_flexible = Teclado.read_phone("Ingresa cualquier teléfono (formato: 0000-0000):", strict_prefix=False)
        print(f"Teléfono registrado: {telefono_flexible}")
        
        # Fecha en formato americano
        print("\n📅 Fecha en formato americano")
        fecha_us = Teclado.read_date("Ingresa una fecha", "mm/dd/yyyy")
        print(f"Fecha en formato americano: {fecha_us}")
        
        # Número con rangos específicos
        print("\n🔢 Número con validaciones específicas")
        edad = Teclado.read_integer("Ingresa tu edad:", min_value=0, max_value=150)
        print(f"Edad registrada: {edad} años")
        
        # Número con cantidad de dígitos específica
        codigo = Teclado.read_integer("Ingresa un código de 4 dígitos:", min_digits=4, max_digits=4)
        print(f"Código registrado: {codigo}")
        
        print("\n✅ Validaciones flexibles completadas!")
        
    except KeyboardInterrupt:
        print("\n❌ Proceso cancelado por el usuario.")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")

def main():
    """Función principal del demo"""
    print("¡Bienvenido al Demo de Validaciones!")
    print("\nEste programa te permitirá probar el sistema de validaciones completo.")
    
    while True:
        print("\n" + "=" * 50)
        print("MENÚ DE DEMOSTRACIÓN")
        print("=" * 50)
        print("1. Demo de validaciones salvadoreñas")
        print("2. Demo de validaciones flexibles")
        print("0. Salir")
        print("=" * 50)
        
        try:
            opcion = Teclado.read_integer("Selecciona una opción:", min_value=0, max_value=2)
            
            if opcion == 0:
                print("\n¡Gracias por usar el sistema de validaciones! 👋")
                break
            elif opcion == 1:
                demo_validaciones_salvadorenas()
            elif opcion == 2:
                demo_validaciones_flexibles()
            
            input("\nPresiona Enter para continuar...")
            
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego! 👋")
            break
        except Exception as e:
            print(f"\nError: {e}")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
