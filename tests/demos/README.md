# Demos Interactivos

Esta carpeta contiene demostraciones interactivas del sistema de validaciones.

## Archivos

- **`main.py`**: Programa principal con menú completo de pruebas
- **`demo.py`**: Demostración específica para validaciones salvadoreñas
- **`test_simple.py`**: Pruebas simples y rápidas

## Descripción Detallada

### main.py
Programa principal con menú interactivo que permite:
- Probar cada tipo de validación individualmente
- Ejecutar todas las pruebas en secuencia
- Ver demostraciones automáticas
- Navegación fácil con menú numerado

### demo.py
Demostración específica que incluye:
- Proceso completo de registro salvadoreño
- Validaciones flexibles e internacionales
- Explicaciones contextuales de cada validación
- Dos modos: salvadoreño estricto y flexible

### test_simple.py
Pruebas rápidas para:
- Verificación básica del funcionamiento
- Testing durante desarrollo
- Pruebas de las validaciones más importantes

## Ejecución

```bash
# Desde la raíz del proyecto
python3 tests/demos/main.py        # Menú completo
python3 tests/demos/demo.py        # Demo salvadoreño
python3 tests/demos/test_simple.py # Pruebas simples

# Desde esta carpeta
cd tests/demos
python3 main.py
python3 demo.py
python3 test_simple.py
```

## Casos de Uso

- **Desarrollo**: Usar `test_simple.py` para verificaciones rápidas
- **Demostración**: Usar `demo.py` para mostrar el sistema funcionando
- **Testing completo**: Usar `main.py` para pruebas exhaustivas interactivas
- **Aprendizaje**: Cualquiera de los tres para entender el funcionamiento
