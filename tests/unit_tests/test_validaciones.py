import sys
import os

# Agregar el directorio raíz al path para importar las clases
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Validaciones import Validaciones

def test_all_validations():
    """Prueba exhaustiva de todas las validaciones sin entrada de usuario"""
    
    print("=" * 60)
    print("PRUEBAS EXHAUSTIVAS DE VALIDACIONES")
    print("=" * 60)
    
    # Pruebas de DUI
    print("\n🔍 VALIDACIONES DE DUI:")
    print("-" * 30)
    duis_test = [
        ("12345678-9", True),
        ("00000000-0", True),
        ("99999999-1", True),
        ("1234567-9", False),   # Faltan dígitos
        ("123456789-1", False), # Muchos dígitos
        ("12345678a9", False),  # Caracter inválido
        ("12345678-", False),   # Sin último dígito
        ("12345678-99", False), # Muchos dígitos finales
        ("abcdefgh-1", False),  # Letras
        ("", False),            # Vacío
    ]
    
    for dui, expected in duis_test:
        result = Validaciones.validate_dui(dui)
        status = "✅" if result == expected else "❌"
        print(f"{status} '{dui}' -> {result} (esperado: {expected})")
    
    # Pruebas de Email
    print("\n📧 VALIDACIONES DE EMAIL:")
    print("-" * 30)
    emails_test = [
        ("usuario@dominio.com", True),
        ("test.email@gmail.com", True),
        ("admin@empresa.org", True),
        ("user123@site.edu.sv", True),
        ("invalid-email", False),         # Sin @
        ("user@", False),                 # Sin dominio
        ("@dominio.com", False),          # Sin usuario
        ("user@@dominio.com", False),     # Doble @
        ("user@dominio", False),          # Sin extensión
        ("user@.com", False),             # Dominio inválido
        ("", False),                      # Vacío
    ]
    
    for email, expected in emails_test:
        result = Validaciones.validate_email(email)
        status = "✅" if result == expected else "❌"
        print(f"{status} '{email}' -> {result} (esperado: {expected})")
    
    # Pruebas de Teléfono (strict)
    print("\n📞 VALIDACIONES DE TELÉFONO (STRICT):")
    print("-" * 40)
    phones_strict_test = [
        ("6012-3456", True),   # Celular
        ("7012-3456", True),   # Celular
        ("2234-5678", True),   # Fijo
        ("8012-3456", False),  # Prefijo inválido
        ("9012-3456", False),  # Prefijo inválido
        ("601-3456", False),   # Pocos dígitos
        ("60123-456", False),  # Formato incorrecto
        ("6012a3456", False),  # Letra en lugar de guión
        ("", False),           # Vacío
    ]
    
    for phone, expected in phones_strict_test:
        result = Validaciones.validate_phone(phone, strict_prefix=True)
        status = "✅" if result == expected else "❌"
        print(f"{status} '{phone}' -> {result} (esperado: {expected})")
    
    # Pruebas de Teléfono (no strict)
    print("\n📞 VALIDACIONES DE TELÉFONO (NO STRICT):")
    print("-" * 45)
    phones_no_strict_test = [
        ("8012-3456", True),   # Ahora válido
        ("9012-3456", True),   # Ahora válido
        ("1234-5678", True),   # Cualquier dígito
        ("0000-0000", True),   # Incluso ceros
        ("601-3456", False),   # Aún faltan dígitos
        ("", False),           # Vacío
    ]
    
    for phone, expected in phones_no_strict_test:
        result = Validaciones.validate_phone(phone, strict_prefix=False)
        status = "✅" if result == expected else "❌"
        print(f"{status} '{phone}' -> {result} (esperado: {expected})")
    
    # Pruebas de Fecha
    print("\n📅 VALIDACIONES DE FECHA (dd/mm/yyyy):")
    print("-" * 40)
    dates_test = [
        ("25/12/2023", True),   # Fecha normal
        ("01/01/2000", True),   # Inicio de milenio
        ("29/02/2024", True),   # Año bisiesto
        ("28/02/2023", True),   # Febrero no bisiesto
        ("31/01/2023", True),   # Enero con 31 días
        ("30/04/2023", True),   # Abril con 30 días
        ("32/01/2023", False),  # Día inválido
        ("29/02/2023", False),  # No es año bisiesto
        ("31/04/2023", False),  # Abril no tiene 31 días
        ("00/01/2023", False),  # Día cero
        ("15/13/2023", False),  # Mes inválido
        ("15/00/2023", False),  # Mes cero
        ("15/12/1899", False),  # Año muy antiguo
        ("15/12/2101", False),  # Año muy futuro
        ("1/1/2023", False),    # Formato incorrecto
        ("", False),            # Vacío
    ]
    
    for date, expected in dates_test:
        result = Validaciones.validate_date(date, "dd/mm/yyyy")
        status = "✅" if result == expected else "❌"
        print(f"{status} '{date}' -> {result} (esperado: {expected})")
    
    # Pruebas de años bisiestos
    print("\n🗓️  PRUEBAS DE AÑOS BISIESTOS:")
    print("-" * 35)
    leap_years_test = [
        (2024, True),   # Divisible por 4
        (2000, True),   # Divisible por 400
        (1900, False),  # Divisible por 100 pero no por 400
        (2023, False),  # No divisible por 4
        (2100, False),  # Divisible por 100 pero no por 400
        (2400, True),   # Divisible por 400
    ]
    
    for year, expected in leap_years_test:
        result = Validaciones._is_leap_year(year)
        status = "✅" if result == expected else "❌"
        print(f"{status} {year} -> {result} (esperado: {expected})")
    
    # Pruebas de rangos y longitudes
    print("\n📏 VALIDACIONES DE LONGITUD Y RANGO:")
    print("-" * 40)
    
    # Longitud
    print("Longitud de texto:")
    print(f"✅ 'Hola' (4 chars, min=3, max=5) -> {Validaciones.validate_length('Hola', 3, 5)}")
    print(f"❌ 'Hi' (2 chars, min=3, max=5) -> {Validaciones.validate_length('Hi', 3, 5)}")
    print(f"❌ 'Muy largo texto' (16 chars, min=3, max=5) -> {Validaciones.validate_length('Muy largo texto', 3, 5)}")
    
    # Rango
    print("\nRango numérico:")
    print(f"✅ 25 (min=10, max=50) -> {Validaciones.validate_range(25, 10, 50)}")
    print(f"❌ 5 (min=10, max=50) -> {Validaciones.validate_range(5, 10, 50)}")
    print(f"❌ 100 (min=10, max=50) -> {Validaciones.validate_range(100, 10, 50)}")
    
    print("\n" + "=" * 60)
    print("TODAS LAS PRUEBAS COMPLETADAS")
    print("=" * 60)

if __name__ == "__main__":
    test_all_validations()
