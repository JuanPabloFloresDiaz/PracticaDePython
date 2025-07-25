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

1. **Sistema de registro de estudiantes**
2. **Calculadora con validaciones**
3. **Registro de empleados**
4. **Sistema de inventario**
5. **Agenda telefónica**
6. **Control de notas**
7. **Sistema de ventas**
8. **Registro de usuarios**

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
