#  Sistema de Gestión de Pedidos



### **MÓDULOS PRINCIPALES** (8 archivos .py)

| Archivo | Descripción |
|---------|-------------|
| `pedido.py` | Clase Pedido - Modelo de datos básico |
| `tienda.py` | Clase Tienda - Ubicaciones de distribución |
| `nodo_arbol.py` | Clase NodoArbol - Nodos del árbol BST |
| `calculador_rutas.py` | Clase CalculadorRutas - Cálculos matemáticos |
| `gestor_tiendas.py` | Clase GestorTiendas - Control de tiendas |
| `gestor_arbol_bst.py` | Clase GestorArbolBST - Control del árbol |
| `sistema_pedidos.py` | Clase SistemaPedidos - Orquestador principal |
| `interfaz_usuario.py` | Clase InterfazUsuario - Menú interactivo |

### **EJEMPLOS Y DOCUMENTACIÓN** (4 archivos)

| Archivo | Descripción |
|---------|-------------|
| `ejemplo_uso.py` | 5 ejemplos funcionales completos |
| `DOCUMENTACION.md` | Documentación técnica completa |

---

##  Cómo Usar

### **Opción 1: Interfaz Interactiva**
```bash
python interfaz_usuario.py
```
Abre un menú donde puede interactuar con el sistema completo.

### **Opción 2: Ejemplos Automáticos**
```bash
python ejemplo_uso.py
```
Ejecuta 5 ejemplos que demuestran todas las funcionalidades.

### **Opción 3: Uso Programático**
```python
from sistema_pedidos import SistemaPedidos

sistema = SistemaPedidos()
sistema.agregar_tienda("Mi Tienda", 10.0, 20.0)
sistema.agregar_pedido(1, "Producto", 15.0, 25.0)
sistema.asignar_repartidor(0.0, 0.0)
stats = sistema.obtener_estadisticas()
print(stats)
```

---

##  Estructura de Módulos

```
CAPA DE PRESENTACIÓN
       ↓
  InterfazUsuario (interfaz_usuario.py)
       ↓
CAPA DE ORQUESTACIÓN  
       ↓
  SistemaPedidos (sistema_pedidos.py)
       ↓
CAPA DE GESTIÓN
       ├─ GestorTiendas (gestor_tiendas.py)
       ├─ GestorArbolBST (gestor_arbol_bst.py)
       └─ CalculadorRutas (calculador_rutas.py)
       ↓
CAPA DE MODELOS
       ├─ Pedido (pedido.py)
       ├─ Tienda (tienda.py)
       └─ NodoArbol (nodo_arbol.py)
```

---

##  Ventajas Principales

### 1️⃣ **Separación de Responsabilidades**
- Cada clase tiene UNA razón para cambiar
- Código más limpio y organizado

### 2️⃣ **Reutilización**
```python
# Importar solo lo que necesitas
from gestor_tiendas import GestorTiendas
from calculador_rutas import CalculadorRutas

# Usar en otro proyecto
mi_gestor = GestorTiendas()
```

### 3️⃣ **Testing Facilitado**
```python
# Tests para GestorTiendas sin tocar otros módulos
import unittest
from gestor_tiendas import GestorTiendas

class TestGestorTiendas(unittest.TestCase):
    def test_agregar_tienda(self):
        gestor = GestorTiendas()
        gestor.agregar_tienda("Test", 0, 0)
        assert gestor.contar_tiendas() == 1
```

---

## Documentación Incluida
### DOCUMENTACION.md
- Descripción de cada módulo
- Métodos principales de cada clase
- Ejemplos de uso
- Extensiones futuras
- Complejidad algorítmica


### ejemplo_uso.py
- **Ejemplo 1**: Uso básico
- **Ejemplo 2**: Asignación de repartidor
- **Ejemplo 3**: Búsquedas y consultas
- **Ejemplo 4**: Estadísticas
- **Ejemplo 5**: Flujo completo

---

## 🎓 Conceptos Implementados

 **Programación Orientada a Objetos**
- Encapsulación
- Abstracción
- Reutilización

 **Estructuras de Datos**
- Listas enlazadas (Tiendas)
- Árboles Binarios de Búsqueda
- Grafos (en conceptos)

 **Patrones de Diseño**
- MVC (Model-View-Controller)
- Facade
- Singleton (implícito)

 **Algoritmos**
- Búsqueda binaria
- Recorrido inorden
- Optimización de rutas (permutaciones)
- Cálculo de distancias

---

## Funcionalidades Disponibles

### Gestión de Tiendas
- Agregar tienda
- Mostrar tiendas
-  Buscar tienda por ID
-  Contar tiendas

### Gestión de Pedidos
-  Agregar pedido
-  Buscar pedido por número
-  Mostrar pedidos ordenados
-  Contar pedidos
-  Marcar como entregado
-  Mostrar pedidos por tienda
-  Buscar pedidos en rango

### Operaciones de Entrega
-  Asignar repartidor
-  Calcular ruta óptima
-  Calcular distancias
-  Actualizar estado de pedidos

### Análisis y Reportes
-  Contar pedidos pendientes
-  Obtener altura del árbol
-  Obtener estadísticas del sistema
-  Imprimir en diferentes formatos

---

##  Complejidad Algorítmica

| Operación | Complejidad | Ubicación |
|-----------|------------|-----------|
| Agregar tienda | O(1) | GestorTiendas |
| Buscar tienda | O(n) | GestorTiendas |
| Insertar pedido | O(log n) | GestorArbolBST |
| Buscar pedido | O(log n) | GestorArbolBST |
| Imprimir ordenado | O(n) | GestorArbolBST |
| Contar pendientes | O(n) | GestorArbolBST |
| Calcular ruta | O(n!) | CalculadorRutas |

---


##  Ejemplos Rápidos

### Crear una instancia
```python
from sistema_pedidos import SistemaPedidos
sistema = SistemaPedidos()
```

### Agregar tienda
```python
sistema.agregar_tienda("Tienda Centro", 10.0, 20.0)
```

### Agregar pedido
```python
sistema.agregar_pedido(id_tienda=1, producto="Laptop", 
                      x_entrega=15.0, y_entrega=25.0)
```

### Mostrar todo
```python
sistema.mostrar_tiendas()
sistema.imprimir_pedidos_ordenados()
```

### Buscar
```python
sistema.buscar_pedido(1)
sistema.mostrar_pedidos_por_tienda(1)
sistema.pedidos_en_rango(1, 5)
```

### Entregar
```python
sistema.asignar_repartidor(x_repartidor=0, y_repartidor=0)
```

### Estadísticas
```python
stats = sistema.obtener_estadisticas()
print(stats)
```

---

---


---


##  Resumen de Archivos

```
Entregables:
├── Módulos Python (8)
│   ├── pedido.py
│   ├── tienda.py
│   ├── nodo_arbol.py
│   ├── calculador_rutas.py
│   ├── gestor_tiendas.py
│   ├── gestor_arbol_bst.py
│   ├── sistema_pedidos.py
│   └── interfaz_usuario.py
│
├── Ejemplos (1)
│   └── ejemplo_uso.py
│
└── Documentación (4)
    ├── README_PROYECTO_MODULARIZADO.md (este archivo)
    ├── DOCUMENTACION.md
    ├── ESTRUCTURA_MODULAR.txt
    └── DIAGRAMA_UML.txt
```

