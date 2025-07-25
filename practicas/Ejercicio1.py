"""
Ejercicio básico que realiza la suma de dos números. 
Utiliza clases de validaciones para asegurar que las entradas sean correctas 
y la clase Teclado para capturar los valores ingresados por el usuario.
"""
import sys
import os

# Agregar el directorio padre al path para importar las clases
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Teclado import Teclado
from Validaciones import Validaciones

def ejercicio_basico():
    """Ejercicio básico de suma de dos números con validaciones"""
    
    print("🔢 EJERCICIO BÁSICO: SUMA DE DOS NÚMEROS")
    print("=" * 40)
    
    try:
        # Captura del primer número
        num1 = Teclado.read_integer("Ingresa el primer número entero:")
        print(f"Primer número ingresado: {num1}")
        
        # Captura del segundo número
        num2 = Teclado.read_integer("Ingresa el segundo número entero:")
        print(f"Segundo número ingresado: {num2}")
        
        # Suma de los números
        resultado = num1 + num2
        print(f"\n✅ Resultado de la suma: {resultado}")
        
    except KeyboardInterrupt:
        print("\n❌ Proceso cancelado por el usuario.")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
if __name__ == "__main__":
    ejercicio_basico()