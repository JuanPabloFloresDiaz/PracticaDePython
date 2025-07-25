# Tests y Demos del Sistema de Validaciones

Esta carpeta contiene todas las pruebas y demostraciones del sistema de validaciones.

## Estructura

```
tests/
├── unit_tests/         # Pruebas unitarias automáticas
│   └── test_validaciones.py
├── demos/              # Demostraciones interactivas
│   ├── main.py         # Programa principal con menú completo
│   ├── demo.py         # Demo específico para validaciones salvadoreñas
│   └── test_simple.py  # Pruebas simples interactivas
└── README.md           # Este archivo
```

## Descripción de Archivos

### Unit Tests (`unit_tests/`)
- **`test_validaciones.py`**: Pruebas exhaustivas automáticas de todas las validaciones
  - No requiere interacción del usuario
  - Valida todos los casos edge conocidos
  - Útil para verificar que el sistema funciona correctamente

### Demos (`demos/`)
- **`main.py`**: Programa principal con menú interactivo completo
  - Permite probar todas las validaciones una por una
  - Incluye opción para ejecutar todas las pruebas
  - Menú organizado y fácil de usar

- **`demo.py`**: Demostración específica para El Salvador
  - Enfocado en validaciones salvadoreñas (DUI, teléfonos)
  - Simula un proceso de registro completo
  - Incluye validaciones flexibles e internacionales

- **`test_simple.py`**: Pruebas simples y rápidas
  - Para verificación rápida del funcionamiento
  - Prueba las validaciones más importantes
  - Ideal para desarrollo y debugging

## Cómo Ejecutar

### Desde la raíz del proyecto:

```bash
# Pruebas unitarias (automáticas)
python3 tests/unit_tests/test_validaciones.py

# Programa principal completo
python3 tests/demos/main.py

# Demo específico salvadoreño
python3 tests/demos/demo.py

# Pruebas simples
python3 tests/demos/test_simple.py
```

### Desde cada carpeta:

```bash
# Ir a la carpeta de unit tests
cd tests/unit_tests
python3 test_validaciones.py

# Ir a la carpeta de demos
cd tests/demos
python3 main.py
python3 demo.py
python3 test_simple.py
```

## Propósito de la Separación

Esta estructura permite:

1. **Mantener el proyecto principal limpio** para futuras prácticas
2. **Organizar las pruebas** por tipo y propósito
3. **Facilitar el mantenimiento** del código de tests
4. **Permitir el crecimiento** del proyecto sin desorganización
5. **Separar funcionalidad core** de ejemplos y pruebas
