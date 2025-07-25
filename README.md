# Sistema de Validaciones en Python

Este proyecto implementa un sistema completo de validaciones para entrada de datos en Python, dividido en módulos especializados.

## Estructura del Proyecto

```
PracticaDePython/
├── Teclado.py              # Clase para manejo de entrada de datos
├── Validaciones.py         # Clase con todas las validaciones
├── ejemplo_uso.py          # Ejemplo básico de uso
├── practicas/              # Carpeta para futuras prácticas y ejercicios
│   └── README.md           # Guía para crear prácticas
├── tests/                  # Carpeta de pruebas y demostraciones
│   ├── unit_tests/         # Pruebas unitarias automáticas
│   │   ├── test_validaciones.py
│   │   └── README.md
│   ├── demos/              # Demostraciones interactivas
│   │   ├── main.py         # Programa principal con menú
│   │   ├── demo.py         # Demo específico salvadoreño
│   │   ├── test_simple.py  # Pruebas simples
│   │   └── README.md
│   └── README.md           # Documentación de tests
└── README.md               # Este archivo
```

## Módulos

### 1. Validaciones.py
Contiene todas las funciones de validación:

#### Validaciones básicas:
- `validate_length()`: Valida longitud de cadenas
- `validate_range()`: Valida rangos numéricos
- `validate_integer()`: Valida números enteros
- `validate_double()`: Valida números decimales

#### Validaciones específicas:
- `validate_dui()`: Valida DUI salvadoreño (formato: 00000000-0)
- `validate_email()`: Valida formato de correo electrónico
- `validate_phone()`: Valida teléfono salvadoreño (formato: 0000-0000)
  - Con opción `strict_prefix` para validar prefijos (2, 6, 7)
- `validate_date()`: Valida fechas en múltiples formatos
  - Soporta: dd/mm/yyyy, mm/dd/yyyy, yyyy/mm/dd
  - Incluye validación de años bisiestos

### 2. Teclado.py
Maneja la entrada de datos con validaciones automáticas:

#### Métodos disponibles:
- `read_integer()`: Lee enteros con validaciones de dígitos y rangos
- `read_double()`: Lee números decimales con validaciones de rango
- `read_text()`: Lee texto con validaciones de longitud
- `read_dui()`: Lee DUI con validación de formato
- `read_email()`: Lee email con validación de formato
- `read_phone()`: Lee teléfono con validación de formato y prefijos opcionales
- `read_date()`: Lee fechas con validación de formato y fechas válidas

### 3. tests/ (Pruebas y Demostraciones)
Contiene todas las pruebas y demostraciones del sistema:

#### tests/unit_tests/
- **`test_validaciones.py`**: Pruebas exhaustivas automáticas

#### tests/demos/
- **`main.py`**: Programa principal con menú completo de pruebas
- **`demo.py`**: Demostración específica para validaciones salvadoreñas
- **`test_simple.py`**: Pruebas simples y rápidas

## Características Especiales

### Validación de DUI
- Formato: 8 dígitos + guión + 1 dígito
- Ejemplo: `12345678-9`

### Validación de Teléfono
- Formato: 4 dígitos + guión + 4 dígitos
- Ejemplo: `6012-3456`
- **Validación estricta de prefijos (configurable):**
  - `6` y `7`: Números de celular
  - `2`: Números fijos
  - Si `strict_prefix=False`, acepta cualquier primer dígito

### Validación de Email
- Validación básica de formato
- Verifica presencia de @ y dominio con extensión
- Ejemplo: `usuario@dominio.com`

### Validación de Fecha
- **Múltiples formatos soportados:**
  - `dd/mm/yyyy`
  - `mm/dd/yyyy`
  - `yyyy/mm/dd`
- **Validaciones incluidas:**
  - Días válidos por mes
  - Años bisiestos automáticos
  - Rangos de años (1900-2100)

## Uso

### Para hacer nuevas prácticas:
```python
# Ver ejemplo básico
python3 ejemplo_uso.py

# Crear tus ejercicios en la carpeta practicas/
# Ejemplo:
from Teclado import Teclado
from Validaciones import Validaciones

nombre = Teclado.read_text("Nombre:")
edad = Teclado.read_integer("Edad:", min_value=0, max_value=150)
```

### Ejecutar pruebas automáticas:
```bash
python3 tests/unit_tests/test_validaciones.py
```

### Ejecutar programa principal con menú:
```bash
python3 tests/demos/main.py
```

### Ejecutar demo específico salvadoreño:
```bash
python3 tests/demos/demo.py
```

### Ejecutar prueba simple:
```bash
python3 tests/demos/test_simple.py
```

### Usar en otro proyecto:
```python
from Teclado import Teclado
from Validaciones import Validaciones

# Leer un DUI
dui = Teclado.read_dui("Ingresa tu DUI:")

# Leer un teléfono sin validación estricta de prefijo
telefono = Teclado.read_phone("Ingresa teléfono:", strict_prefix=False)

# Validar directamente
es_valido = Validaciones.validate_email("test@example.com")
```

## Ejemplos de Validaciones

### DUI válidos:
- ✅ `12345678-9`
- ❌ `1234567-8` (faltan dígitos)
- ❌ `12345678a9` (caracter inválido)

### Teléfonos válidos:
- ✅ `6012-3456` (celular)
- ✅ `7012-3456` (celular)
- ✅ `2234-5678` (fijo)
- ❌ `8012-3456` (prefijo inválido con strict_prefix=True)

### Emails válidos:
- ✅ `usuario@dominio.com`
- ❌ `usuario-sin-arroba`
- ❌ `usuario@dominio-sin-extension`

### Fechas válidas:
- ✅ `25/12/2023`
- ✅ `29/02/2024` (año bisiesto)
- ❌ `32/12/2023` (día inválido)
- ❌ `29/02/2023` (no es año bisiesto)

## Características Técnicas

- **Sin dependencias externas**: Todo implementado con Python estándar
- **Manejo de errores robusto**: Bucles while hasta entrada válida
- **Mensajes de error informativos**: Explicaciones claras de los errores
- **Configuración flexible**: Opciones como `strict_prefix` para teléfonos
- **Validación de años bisiestos**: Implementación manual precisa

## Notas de Implementación

1. **Separación de responsabilidades**: Validaciones separadas de la entrada de datos
2. **Reutilización**: Las validaciones pueden usarse independientemente
3. **Extensibilidad**: Fácil agregar nuevas validaciones siguiendo el patrón
4. **Robustez**: Manejo de todos los casos edge conocidos
5. **Usabilidad**: Mensajes claros y reintentos automáticos

## Organización del Proyecto

### Archivos Core (Raíz)
- **`Teclado.py`** y **`Validaciones.py`**: Clases principales del sistema
- **`ejemplo_uso.py`**: Ejemplo básico para aprender a usar las clases

### Carpeta `practicas/`
- Destinada para **tus ejercicios y prácticas futuras**
- Usa las clases `Teclado` y `Validaciones` en tus proyectos
- Cada práctica puede tener su propia subcarpeta

### Carpeta `tests/`
- **`unit_tests/`**: Pruebas automáticas para verificar funcionamiento
- **`demos/`**: Demostraciones interactivas del sistema
- **No modificar**: Solo para testing y demostración del sistema

Esta organización mantiene el proyecto principal limpio y permite el crecimiento ordenado con nuevas prácticas.
