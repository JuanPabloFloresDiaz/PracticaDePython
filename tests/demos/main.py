import sys
import os

# Agregar el directorio raíz al path para importar las clases
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Teclado import Teclado
from Validaciones import Validaciones

def test_integer_validation():
    """Prueba la validación de números enteros"""
    print("=== PRUEBA DE NÚMEROS ENTEROS ===")
    
    # Entero básico
    numero = Teclado.read_integer("Ingresa un número entero:")
    print(f"Número ingresado: {numero}")
    
    # Entero con rango de dígitos
    numero_digitos = Teclado.read_integer("Ingresa un número de 3 a 5 dígitos:", min_digits=3, max_digits=5)
    print(f"Número con dígitos limitados: {numero_digitos}")
    
    # Entero con rango de valores
    numero_rango = Teclado.read_integer("Ingresa un número entre 10 y 100:", min_value=10, max_value=100)
    print(f"Número en rango: {numero_rango}")
    print()

def test_double_validation():
    """Prueba la validación de números decimales"""
    print("=== PRUEBA DE NÚMEROS DECIMALES ===")
    
    # Decimal básico
    decimal = Teclado.read_double("Ingresa un número decimal:")
    print(f"Decimal ingresado: {decimal}")
    
    # Decimal con rango
    decimal_rango = Teclado.read_double("Ingresa un decimal entre 0.0 y 10.0:", min_value=0.0, max_value=10.0)
    print(f"Decimal en rango: {decimal_rango}")
    print()

def test_text_validation():
    """Prueba la validación de texto"""
    print("=== PRUEBA DE TEXTO ===")
    
    # Texto básico
    texto = Teclado.read_text("Ingresa un texto:")
    print(f"Texto ingresado: {texto}")
    
    # Texto con longitud limitada
    texto_limitado = Teclado.read_text("Ingresa un texto de 5 a 20 caracteres:", min_length=5, max_length=20)
    print(f"Texto con longitud limitada: {texto_limitado}")
    print()

def test_dui_validation():
    """Prueba la validación de DUI"""
    print("=== PRUEBA DE DUI ===")
    
    dui = Teclado.read_dui("Ingresa tu DUI (formato: 00000000-0):")
    print(f"DUI ingresado: {dui}")
    print()

def test_email_validation():
    """Prueba la validación de correo electrónico"""
    print("=== PRUEBA DE CORREO ELECTRÓNICO ===")
    
    email = Teclado.read_email("Ingresa tu correo electrónico:")
    print(f"Email ingresado: {email}")
    print()

def test_phone_validation():
    """Prueba la validación de teléfono"""
    print("=== PRUEBA DE TELÉFONO ===")
    
    # Teléfono con validación estricta de prefijo
    phone_strict = Teclado.read_phone("Ingresa tu teléfono (debe iniciar con 2, 6 o 7):", strict_prefix=True)
    print(f"Teléfono con validación estricta: {phone_strict}")
    
    # Teléfono sin validación estricta de prefijo
    phone_loose = Teclado.read_phone("Ingresa un teléfono (formato: 0000-0000):", strict_prefix=False)
    print(f"Teléfono sin validación estricta: {phone_loose}")
    print()

def test_date_validation():
    """Prueba la validación de fechas"""
    print("=== PRUEBA DE FECHAS ===")
    
    # Fecha formato dd/mm/yyyy
    fecha_dd_mm = Teclado.read_date("Ingresa una fecha", "dd/mm/yyyy")
    print(f"Fecha dd/mm/yyyy: {fecha_dd_mm}")
    
    # Fecha formato mm/dd/yyyy
    fecha_mm_dd = Teclado.read_date("Ingresa una fecha", "mm/dd/yyyy")
    print(f"Fecha mm/dd/yyyy: {fecha_mm_dd}")
    
    # Fecha formato yyyy/mm/dd
    fecha_yyyy_mm = Teclado.read_date("Ingresa una fecha", "yyyy/mm/dd")
    print(f"Fecha yyyy/mm/dd: {fecha_yyyy_mm}")
    print()

def test_validations_directly():
    """Prueba las validaciones directamente sin entrada de usuario"""
    print("=== PRUEBAS DIRECTAS DE VALIDACIONES ===")
    
    # Pruebas de DUI
    print("Validaciones de DUI:")
    print(f"12345678-9 -> {Validaciones.validate_dui('12345678-9')}")
    print(f"1234567-9 -> {Validaciones.validate_dui('1234567-9')}")
    print(f"12345678a9 -> {Validaciones.validate_dui('12345678a9')}")
    print()
    
    # Pruebas de email
    print("Validaciones de email:")
    print(f"test@example.com -> {Validaciones.validate_email('test@example.com')}")
    print(f"invalid-email -> {Validaciones.validate_email('invalid-email')}")
    print(f"test@domain -> {Validaciones.validate_email('test@domain')}")
    print()
    
    # Pruebas de teléfono
    print("Validaciones de teléfono:")
    print(f"6012-3456 (strict) -> {Validaciones.validate_phone('6012-3456', True)}")
    print(f"7012-3456 (strict) -> {Validaciones.validate_phone('7012-3456', True)}")
    print(f"2234-5678 (strict) -> {Validaciones.validate_phone('2234-5678', True)}")
    print(f"8012-3456 (strict) -> {Validaciones.validate_phone('8012-3456', True)}")
    print(f"8012-3456 (no strict) -> {Validaciones.validate_phone('8012-3456', False)}")
    print()
    
    # Pruebas de fecha
    print("Validaciones de fecha:")
    print(f"25/12/2023 -> {Validaciones.validate_date('25/12/2023', 'dd/mm/yyyy')}")
    print(f"32/12/2023 -> {Validaciones.validate_date('32/12/2023', 'dd/mm/yyyy')}")
    print(f"29/02/2024 -> {Validaciones.validate_date('29/02/2024', 'dd/mm/yyyy')}")  # Año bisiesto
    print(f"29/02/2023 -> {Validaciones.validate_date('29/02/2023', 'dd/mm/yyyy')}")  # No bisiesto
    print()

def show_menu():
    """Muestra el menú de opciones"""
    print("=" * 50)
    print("SISTEMA DE PRUEBAS DE VALIDACIONES")
    print("=" * 50)
    print("1. Probar números enteros")
    print("2. Probar números decimales")
    print("3. Probar texto")
    print("4. Probar DUI")
    print("5. Probar correo electrónico")
    print("6. Probar teléfono")
    print("7. Probar fechas")
    print("8. Ejecutar pruebas directas de validaciones")
    print("9. Ejecutar todas las pruebas")
    print("0. Salir")
    print("=" * 50)

def main():
    """Función principal del programa"""
    while True:
        show_menu()
        try:
            opcion = Teclado.read_integer("Selecciona una opción:", min_value=0, max_value=9)
            
            if opcion == 0:
                print("¡Hasta luego!")
                break
            elif opcion == 1:
                test_integer_validation()
            elif opcion == 2:
                test_double_validation()
            elif opcion == 3:
                test_text_validation()
            elif opcion == 4:
                test_dui_validation()
            elif opcion == 5:
                test_email_validation()
            elif opcion == 6:
                test_phone_validation()
            elif opcion == 7:
                test_date_validation()
            elif opcion == 8:
                test_validations_directly()
            elif opcion == 9:
                print("Ejecutando todas las pruebas...")
                print("NOTA: Para ejecutar todas las pruebas, deberás ingresar datos para cada validación.")
                respuesta = input("¿Deseas continuar? (s/n): ").strip().lower()
                if respuesta == 's':
                    test_integer_validation()
                    test_double_validation()
                    test_text_validation()
                    test_dui_validation()
                    test_email_validation()
                    test_phone_validation()
                    test_date_validation()
                    test_validations_directly()
            
            input("\nPresiona Enter para continuar...")
            
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido por el usuario!")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
