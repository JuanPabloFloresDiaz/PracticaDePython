# Ejemplo Básico de Uso del Sistema de Validaciones

from Teclado import Teclado
from Validaciones import Validaciones

def ejemplo_basico():
    """
    Ejemplo básico de cómo usar las clases Teclado y Validaciones
    en tus propias prácticas y ejercicios.
    """
    
    print("🚀 EJEMPLO BÁSICO DEL SISTEMA DE VALIDACIONES")
    print("=" * 50)
    print("Este es un ejemplo de cómo usar las clases en tus ejercicios:")
    print()
    
    # Ejemplo 1: Leer datos básicos
    print("1️⃣ Leyendo datos básicos:")
    nombre = Teclado.read_text("Nombre:", min_length=2, max_length=30)
    edad = Teclado.read_integer("Edad:", min_value=0, max_value=120)
    print(f"   ✅ Datos: {nombre}, {edad} años")
    print()
    
    # Ejemplo 2: Validar directamente sin entrada de usuario
    print("2️⃣ Validando datos directamente:")
    email_test = "usuario@ejemplo.com"
    es_valido = Validaciones.validate_email(email_test)
    print(f"   📧 Email '{email_test}' es válido: {es_valido}")
    
    dui_test = "12345678-9"
    es_valido_dui = Validaciones.validate_dui(dui_test)
    print(f"   🆔 DUI '{dui_test}' es válido: {es_valido_dui}")
    print()
    
    # Ejemplo 3: Usar en estructuras más complejas
    print("3️⃣ Ejemplo con estructura de datos:")
    
    estudiante = {}
    estudiante['nombre'] = Teclado.read_text("Nombre del estudiante:", min_length=2)
    estudiante['carnet'] = Teclado.read_text("Carnet:", min_length=5, max_length=10)
    estudiante['nota'] = Teclado.read_double("Nota final:", min_value=0.0, max_value=10.0)
    
    print(f"   ✅ Estudiante registrado:")
    print(f"      Nombre: {estudiante['nombre']}")
    print(f"      Carnet: {estudiante['carnet']}")
    print(f"      Nota: {estudiante['nota']}")
    print()
    
    print("🎉 ¡Ejemplo completado! Ahora puedes usar estas clases en tus ejercicios.")

if __name__ == "__main__":
    ejemplo_basico()
