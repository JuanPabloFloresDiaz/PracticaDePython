# Unit Tests

Esta carpeta contiene las pruebas unitarias automáticas del sistema de validaciones.

## Archivos

- **`test_validaciones.py`**: Pruebas exhaustivas de todas las validaciones

## Características

- ✅ **Automatizadas**: No requieren interacción del usuario
- ✅ **Exhaustivas**: Cubren todos los casos edge conocidos
- ✅ **Verificación completa**: Validan todas las funciones del sistema
- ✅ **Feedback visual**: Muestran resultados con emojis y colores

## Ejecución

```bash
# Desde la raíz del proyecto
python3 tests/unit_tests/test_validaciones.py

# Desde esta carpeta
cd tests/unit_tests
python3 test_validaciones.py
```

## Casos de Prueba Incluidos

- **DUI**: 10 casos diferentes (válidos e inválidos)
- **Email**: 11 casos con diferentes formatos
- **Teléfono**: 9 casos con y sin prefijos estrictos
- **Fecha**: 16 casos incluyendo años bisiestos
- **Años bisiestos**: 6 casos específicos
- **Longitud y rango**: Casos básicos de validación

## Ejemplo de Salida

```
🔍 VALIDACIONES DE DUI:
✅ '12345678-9' -> True (esperado: True)
❌ '1234567-9' -> False (esperado: False)
...
```
