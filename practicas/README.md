# Carpeta de Prácticas

Esta carpeta está destinada para almacenar diferentes ejercicios y prácticas que utilicen las clases `Teclado` y `Validaciones`.

## Cómo usar las clases en tus prácticas

### Importar las clases

```python
import sys
import os

# Agregar el directorio padre al path para importar las clases
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Teclado import Teclado
from Validaciones import Validaciones
```

### Ejemplos de uso común

```python
# Leer datos con validaciones automáticas
nombre = Teclado.read_text("Nombre:", min_length=2, max_length=50)
edad = Teclado.read_integer("Edad:", min_value=0, max_value=150)
email = Teclado.read_email("Email:")
dui = Teclado.read_dui("DUI:")

# Validar datos directamente
es_email_valido = Validaciones.validate_email("test@example.com")
es_dui_valido = Validaciones.validate_dui("12345678-9")
```

### Ideas para prácticas

1. **Sistema de registro de estudiantes** ✅ (Ejercicio1.py - suma básica)
2. **Lectura de archivos** ✅ (Ejercicio2.py - lector de README)
3. **Operaciones con matrices/NumPy** ✅ (Ejercicio3.py - álgebra lineal)
4. **Calculadora con validaciones**
5. **Registro de empleados**
6. **Sistema de inventario**
7. **Agenda telefónica**
8. **Control de notas**
9. **Sistema de ventas**
10. **Registro de usuarios**

### Ejercicios completados

#### Ejercicio1.py - Suma de dos números
- Uso básico de `Teclado.read_integer()`
- Manejo de errores
- Validaciones automáticas

#### Ejercicio2.py - Lector de archivos
- Menú interactivo con validaciones
- Lectura de archivos con manejo de errores
- Navegación por diferentes README del proyecto

#### Ejercicio3.py - Operaciones con matrices usando NumPy
- **Usa NumPy completamente**: Operaciones optimizadas con arrays reales
- **Vectores y matrices**: Soporte para estructuras 1D y 2D
- **8 tipos de operaciones**: Suma, resta, multiplicación, producto punto, matmul, estadísticas, matemáticas avanzadas
- **Funciones avanzadas**: Media, mediana, desviación estándar, funciones trigonométricas
- **Información detallada**: Shape, dimensiones, tipos de datos, memoria
- **Menú interactivo completo**: Navegación intuitiva con validaciones

## Estructura recomendada

```
practicas/
├── ejercicio_01/
│   ├── main.py
│   └── README.md
├── ejercicio_02/
│   ├── main.py
│   └── README.md
└── ...
```

## Ejemplo básico

Revisa el archivo `ejemplo_uso.py` en la raíz del proyecto para ver un ejemplo básico de cómo usar las clases.
