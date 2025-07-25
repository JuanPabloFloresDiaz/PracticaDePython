import sys
import os

# Agregar el directorio raíz al path para importar las clases
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Teclado import Teclado
from Validaciones import Validaciones

def simple_test():
    """Prueba simple de las validaciones más importantes"""
    print("=== PRUEBA SIMPLE DE VALIDACIONES ===\n")
    
    # Prueba DUI
    print("Probando DUI...")
    dui = Teclado.read_dui("Ingresa un DUI válido (formato: 12345678-9):")
    print(f"DUI válido ingresado: {dui}\n")
    
    # Prueba email
    print("Probando email...")
    email = Teclado.read_email("Ingresa un email válido:")
    print(f"Email válido ingresado: {email}\n")
    
    # Prueba teléfono
    print("Probando teléfono con validación estricta...")
    phone = Teclado.read_phone("Ingresa un teléfono (debe iniciar con 2, 6 o 7):", strict_prefix=True)
    print(f"Teléfono válido ingresado: {phone}\n")
    
    # Prueba fecha
    print("Probando fecha...")
    fecha = Teclado.read_date("Ingresa una fecha válida", "dd/mm/yyyy")
    print(f"Fecha válida ingresada: {fecha}\n")
    
    print("¡Todas las validaciones funcionan correctamente!")

if __name__ == "__main__":
    simple_test()
