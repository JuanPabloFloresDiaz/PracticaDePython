"""
Ejercicio 3: Implementación de operaciones con matrices usando NumPy
aplicando las validaciones de entrada de datos y los métodos de lectura del teclado.

Este ejercicio demuestra el uso de NumPy para operaciones con arrays y matrices.
"""
import sys
import os
import numpy as np

# Agregar el directorio padre al path para importar las clases
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Teclado import Teclado

def mostrar_menu():
    """Muestra el menú de operaciones disponibles"""
    print("\n🔢 EJERCICIO 3: OPERACIONES CON MATRICES (NumPy)")
    print("=" * 50)
    print("Selecciona la operación que deseas realizar:")
    print("1. Suma de matrices")
    print("2. Resta de matrices")
    print("3. Multiplicación elemento por elemento")
    print("4. Producto punto (dot product)")
    print("5. Multiplicación de matrices (matmul)")
    print("6. Operaciones estadísticas")
    print("7. Operaciones matemáticas avanzadas")
    print("8. Información detallada de las matrices")
    print("0. Salir")
    print("=" * 50)

def leer_matriz(nombre_matriz, filas, columnas):
    """Lee una matriz de números del usuario"""
    print(f"\n📝 Ingresando datos para {nombre_matriz} ({filas}x{columnas}):")
    
    matriz = []
    for i in range(filas):
        fila = []
        print(f"Fila {i+1}:")
        for j in range(columnas):
            numero = Teclado.read_double(f"  Elemento [{i+1},{j+1}]:")
            fila.append(numero)
        matriz.append(fila)
    
    np_matriz = np.array(matriz)
    print(f"✅ {nombre_matriz} creada:")
    print(np_matriz)
    return np_matriz

def leer_vector(nombre_vector, longitud):
    """Lee un vector de números del usuario"""
    print(f"\n📝 Ingresando datos para {nombre_vector} (vector de {longitud} elementos):")
    
    vector = []
    for i in range(longitud):
        numero = Teclado.read_double(f"Elemento {i+1}/{longitud}:")
        vector.append(numero)
    
    np_vector = np.array(vector)
    print(f"✅ {nombre_vector} creado: {np_vector}")
    return np_vector

def mostrar_resultado(operacion, resultado):
    """Muestra el resultado de una operación de manera formateada"""
    print(f"\n✨ RESULTADO DE {operacion.upper()}:")
    print("=" * (len(operacion) + 15))
    if isinstance(resultado, np.ndarray):
        if resultado.ndim == 0:  # Escalar
            print(f"Resultado: {resultado}")
        else:  # Array o matriz
            print("Resultado:")
            print(resultado)
    else:
        print(f"Resultado: {resultado}")
    print("=" * (len(operacion) + 15))

def operaciones_estadisticas(matriz_a, matriz_b):
    """Realiza operaciones estadísticas con las matrices"""
    print("\n📊 OPERACIONES ESTADÍSTICAS")
    print("-" * 35)
    
    print("\nMatriz A:")
    print(f"  Media: {np.mean(matriz_a):.4f}")
    print(f"  Mediana: {np.median(matriz_a):.4f}")
    print(f"  Desviación estándar: {np.std(matriz_a):.4f}")
    print(f"  Varianza: {np.var(matriz_a):.4f}")
    print(f"  Suma total: {np.sum(matriz_a):.4f}")
    print(f"  Mínimo: {np.min(matriz_a):.4f}")
    print(f"  Máximo: {np.max(matriz_a):.4f}")
    
    print("\nMatriz B:")
    print(f"  Media: {np.mean(matriz_b):.4f}")
    print(f"  Mediana: {np.median(matriz_b):.4f}")
    print(f"  Desviación estándar: {np.std(matriz_b):.4f}")
    print(f"  Varianza: {np.var(matriz_b):.4f}")
    print(f"  Suma total: {np.sum(matriz_b):.4f}")
    print(f"  Mínimo: {np.min(matriz_b):.4f}")
    print(f"  Máximo: {np.max(matriz_b):.4f}")

def operaciones_matematicas_avanzadas(matriz_a, matriz_b):
    """Realiza operaciones matemáticas avanzadas"""
    print("\n🧮 OPERACIONES MATEMÁTICAS AVANZADAS")
    print("-" * 45)
    
    # Funciones trigonométricas en la primera matriz
    print("\nFunciones aplicadas a Matriz A:")
    print(f"Seno: {np.sin(matriz_a)}")
    print(f"Coseno: {np.cos(matriz_a)}")
    print(f"Raíz cuadrada: {np.sqrt(np.abs(matriz_a))}")
    print(f"Exponencial: {np.exp(matriz_a)}")
    
    # Operaciones de comparación
    print(f"\nComparaciones:")
    print(f"A > B:\n{matriz_a > matriz_b}")
    print(f"A == B:\n{matriz_a == matriz_b}")

def mostrar_info_detallada(matriz, nombre):
    """Muestra información detallada sobre una matriz"""
    print(f"\n� INFORMACIÓN DETALLADA DE {nombre}:")
    print("-" * (25 + len(nombre)))
    print(f"Forma (shape): {matriz.shape}")
    print(f"Dimensiones: {matriz.ndim}")
    print(f"Tamaño total: {matriz.size}")
    print(f"Tipo de datos: {matriz.dtype}")
    print(f"Bytes por elemento: {matriz.itemsize}")
    print(f"Memoria total: {matriz.nbytes} bytes")
    print(f"Matriz:\n{matriz}")

def ejercicio_numpy():
    """Función principal del ejercicio con NumPy"""
    
    print("🚀 BIENVENIDO AL EJERCICIO DE OPERACIONES CON MATRICES")
    print("🐍 Usando NumPy versión:", np.__version__)
    print("=" * 60)
    
    try:
        # Preguntar si quiere trabajar con vectores o matrices
        tipo = Teclado.read_integer(
            "¿Qué tipo de estructura quieres usar?\n1. Vectores (1D)\n2. Matrices (2D)\nOpción:",
            min_value=1, max_value=2
        )
        
        if tipo == 1:  # Vectores
            longitud = Teclado.read_integer(
                "¿Qué longitud deben tener los vectores?",
                min_value=2, max_value=10
            )
            
            print(f"\n📏 Los vectores tendrán {longitud} elementos cada uno")
            matriz_a = leer_vector("Vector A", longitud)
            matriz_b = leer_vector("Vector B", longitud)
            
        else:  # Matrices
            filas = Teclado.read_integer(
                "¿Cuántas filas deben tener las matrices?",
                min_value=2, max_value=5
            )
            columnas = Teclado.read_integer(
                "¿Cuántas columnas deben tener las matrices?",
                min_value=2, max_value=5
            )
            
            print(f"\n� Las matrices serán de {filas}x{columnas}")
            matriz_a = leer_matriz("Matriz A", filas, columnas)
            matriz_b = leer_matriz("Matriz B", filas, columnas)
        
        # Menú de operaciones
        while True:
            mostrar_menu()
            opcion = Teclado.read_integer("Selecciona una opción:", min_value=0, max_value=8)
            
            if opcion == 0:
                print("\n👋 ¡Gracias por usar el calculador de matrices con NumPy!")
                break
            
            elif opcion == 1:  # Suma
                resultado = matriz_a + matriz_b
                mostrar_resultado("suma de matrices", resultado)
                
            elif opcion == 2:  # Resta
                resultado = matriz_a - matriz_b
                mostrar_resultado("resta de matrices", resultado)
                
            elif opcion == 3:  # Multiplicación elemento por elemento
                resultado = matriz_a * matriz_b
                mostrar_resultado("multiplicación elemento por elemento", resultado)
                
            elif opcion == 4:  # Producto punto
                resultado = np.dot(matriz_a, matriz_b)
                mostrar_resultado("producto punto", resultado)
                
            elif opcion == 5:  # Multiplicación de matrices (matmul)
                try:
                    resultado = np.matmul(matriz_a, matriz_b)
                    mostrar_resultado("multiplicación de matrices", resultado)
                except ValueError as e:
                    print(f"❌ Error en multiplicación de matrices: {e}")
                    print("💡 Las dimensiones deben ser compatibles para la multiplicación")
                
            elif opcion == 6:  # Operaciones estadísticas
                operaciones_estadisticas(matriz_a, matriz_b)
                
            elif opcion == 7:  # Operaciones matemáticas avanzadas
                operaciones_matematicas_avanzadas(matriz_a, matriz_b)
                
            elif opcion == 8:  # Información detallada
                mostrar_info_detallada(matriz_a, "MATRIZ A")
                mostrar_info_detallada(matriz_b, "MATRIZ B")
            
            print("\nPresiona Enter para continuar...")
            input()
            
    except KeyboardInterrupt:
        print("\n\n❌ Proceso cancelado por el usuario.")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")

if __name__ == "__main__":
    ejercicio_numpy()