# Sistema de Gestión de Pedidos y Rutas - VERSIÓN MODULARIZADA

## 📋 Descripción General

Este proyecto es una versión **modularizada y refactorizada** del sistema original de gestión de pedidos y optimización de rutas de entrega. El código ha sido dividido en módulos independientes que facilitan el mantenimiento, la extensión y el testing.

---

## 📁 Estructura de Módulos

```
proyecto/
│
├── pedido.py                    # Clase Pedido
├── tienda.py                    # Clase Tienda
├── nodo_arbol.py                # Clase NodoArbol (para BST)
├── calculador_rutas.py          # Clase CalculadorRutas (utilidades matemáticas)
├── gestor_tiendas.py            # Clase GestorTiendas (gestión de lista de tiendas)
├── gestor_arbol_bst.py          # Clase GestorArbolBST (gestión del árbol binario)
├── sistema_pedidos.py           # Clase SistemaPedidos (orquestador principal)
├── interfaz_usuario.py          # Clase InterfazUsuario (menú interactivo)
│
└── README.md                    # Este archivo
```

---

## 🏗️ Arquitectura del Sistema

### Diagrama de Dependencias

```
┌─────────────────────────────────────────────────────────┐
│                  InterfazUsuario                        │
│              (interfaz_usuario.py)                      │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                  SistemaPedidos                         │
│              (sistema_pedidos.py)                       │
└────────────────────┬────────────────────────────────────┘
                     │
         ┌───────────┼───────────┐
         ▼           ▼           ▼
    ┌─────────┐ ┌──────────────┐ ┌────────────────┐
    │GestorTi │ │GestorArbolBST│ │CalculadorRutas│
    │endas    │ │              │ │                │
    └─────────┘ └──────────────┘ └────────────────┘
        │              │
        ▼              ▼
    ┌────────┐   ┌──────────┐
    │ Tienda  │   │NodoArbol │
    │         │   │          │
    └────────┘   └──────────┘
                      │
                      ▼
                  ┌────────┐
                  │ Pedido │
                  └────────┘
```

---

## 📚 Descripción de Módulos

### 1. **pedido.py**
Define la clase `Pedido` que representa un pedido individual.

**Responsabilidades:**
- Almacenar información del pedido
- Gestionar el estado del pedido
- Proporcionar métodos de acceso a datos

**Métodos principales:**
```python
__init__(numPedido, id_tienda, producto, x_entrega, y_entrega)
cambiar_estado(nuevo_estado)
obtener_info()
```

---

### 2. **tienda.py**
Define la clase `Tienda` que representa una tienda en la red.

**Responsabilidades:**
- Almacenar información de la tienda
- Mantener ubicación geográfica

**Métodos principales:**
```python
__init__(id_tienda, nombre, x, y)
obtener_ubicacion()
obtener_info()
```

---

### 3. **nodo_arbol.py**
Define la clase `NodoArbol` para el árbol binario de búsqueda.

**Responsabilidades:**
- Representar un nodo en el árbol BST
- Mantener referencias a pedidos y nodos hijo

**Estructura:**
```
NodoArbol
├── pedido (Pedido)
├── izquierda (NodoArbol)
└── derecha (NodoArbol)
```

---

### 4. **calculador_rutas.py**
Define la clase `CalculadorRutas` con métodos estáticos para cálculos.

**Responsabilidades:**
- Calcular distancias entre puntos
- Optimizar rutas usando permutaciones

**Métodos principales:**
```python
@staticmethod
calcular_distancia(x1, y1, x2, y2)

@staticmethod
calcular_ruta_optima(pedidos, tiendas_dict, x_inicio, y_inicio)
```

---

### 5. **gestor_tiendas.py**
Define la clase `GestorTiendas` para gestionar la lista de tiendas.

**Responsabilidades:**
- Mantener lista enlazada de tiendas
- Operaciones CRUD sobre tiendas
- Búsqueda de tiendas

**Métodos principales:**
```python
agregar_tienda(nombre, x, y)
mostrar_tiendas()
buscar_tienda(id_tienda)
obtener_tiendas_como_dict()
contar_tiendas()
limpiar_tiendas()
```

---

### 6. **gestor_arbol_bst.py**
Define la clase `GestorArbolBST` para gestionar el árbol de pedidos.

**Responsabilidades:**
- Mantener el árbol binario de búsqueda
- Operaciones de inserción y búsqueda
- Recorridos y análisis del árbol

**Métodos principales:**
```python
insertar(pedido)
buscar(numPedido)
imprimir_inorden()
obtener_pendientes()
contar_pendientes()
buscar_por_tienda(id_tienda)
obtener_altura()
pedidos_en_rango(num_min, num_max)
limpiar()
```

---

### 7. **sistema_pedidos.py** (ORQUESTADOR)
Define la clase `SistemaPedidos` que integra todos los componentes.

**Responsabilidades:**
- Orquestar operaciones de tiendas y pedidos
- Proporcionar interfaz unificada al usuario
- Gestionar flujos de negocio complejos

**Métodos principales:**

**Tiendas:**
```python
agregar_tienda(nombre, x, y)
mostrar_tiendas()
```

**Pedidos:**
```python
agregar_pedido(id_tienda, producto, x_entrega, y_entrega)
buscar_pedido(numPedido)
imprimir_pedidos_ordenados()
contar_pedidos()
```

**Búsquedas:**
```python
mostrar_pedidos_por_tienda(id_tienda)
pedidos_en_rango(num_min, num_max)
```

**Entrega:**
```python
asignar_repartidor(x_repartidor, y_repartidor)
marcar_entregado(numPedido)
```

**Estadísticas:**
```python
mostrar_pendientes()
obtener_altura_arbol()
obtener_estadisticas()
```

**Mantenimiento:**
```python
limpiar_sistema()
```

---

### 8. **interfaz_usuario.py**
Define la clase `InterfazUsuario` que maneja la interacción con el usuario.

**Responsabilidades:**
- Mostrar menú principal
- Capturar entrada del usuario
- Manejar opciones del menú
- Validar datos ingresados

**Métodos principales:**
```python
mostrar_menu_principal()
opcion_agregar_tienda()
opcion_agregar_pedido()
opcion_buscar_pedido()
opcion_asignar_repartidor()
opcion_marcar_entregado()
opcion_mostrar_pedidos_ordenados()
opcion_pedidos_pendientes()
opcion_buscar_por_tienda()
opcion_altura_arbol()
opcion_pedidos_en_rango()
opcion_estadisticas()
opcion_limpiar_todo()
ejecutar()
```

---

## 🚀 Cómo Usar

### Instalación
No requiere dependencias externas. Solo Python 3.6+

### Ejecución
```bash
python interfaz_usuario.py
```

### Ejemplo de Uso
```python
# O iniciar manualmente en Python
from sistema_pedidos import SistemaPedidos

# Crear instancia del sistema
sistema = SistemaPedidos()

# Agregar tiendas
sistema.agregar_tienda("Tienda Centro", 10.0, 20.0)
sistema.agregar_tienda("Tienda Norte", 15.0, 35.0)

# Agregar pedidos
sistema.agregar_pedido(1, "Laptop", 12.0, 22.0)
sistema.agregar_pedido(2, "Mouse", 16.0, 37.0)

# Buscar pedido
sistema.buscar_pedido(1)

# Asignar repartidor
sistema.asignar_repartidor(5.0, 15.0)

# Ver estadísticas
print(sistema.obtener_estadisticas())
```

---

## ✅ Ventajas de la Modularización

1. **Separación de Responsabilidades**
   - Cada módulo tiene una función específica
   - Código más limpio y organizado

2. **Reutilización**
   - Módulos pueden ser usados en otros proyectos
   - Fácil de importar y utilizar

3. **Testing**
   - Cada módulo puede ser testeado independientemente
   - Facilita debugging

4. **Mantenimiento**
   - Cambios localizados en módulos específicos
   - Menos probabilidad de efectos secundarios

5. **Escalabilidad**
   - Fácil agregar nuevas funcionalidades
   - Estructura preparada para crecimiento

6. **Documentación**
   - Cada módulo está documentado
   - Código autodocumentado

---

## 🔄 Flujo de Ejecución

```
1. InterfazUsuario.ejecutar()
   ├─ Mostrar menú
   ├─ Capturar opción
   └─ Llamar método correspondiente
      │
      └─ SistemaPedidos.metodo_seleccionado()
         ├─ GestorTiendas.operacion()
         ├─ GestorArbolBST.operacion()
         └─ CalculadorRutas.operacion()
```

---

## 📊 Complejidad Algorítmica

| Operación | Complejidad | Módulo |
|-----------|------------|--------|
| Agregar tienda | O(1) | GestorTiendas |
| Buscar tienda | O(n) | GestorTiendas |
| Insertar pedido | O(log n) | GestorArbolBST |
| Buscar pedido | O(log n) | GestorArbolBST |
| Imprimir ordenado | O(n) | GestorArbolBST |
| Contar pendientes | O(n) | GestorArbolBST |
| Calcular ruta | O(n!) | CalculadorRutas |
| Calcular distancia | O(1) | CalculadorRutas |

---

##  Extensiones Futuras

### Posibles Mejoras

1. **Persistencia**
   - Guardar datos en archivo JSON
   - Conexión a base de datos

2. **Optimización de Rutas**
   - Implementar algoritmo de Dijkstra
   - Usar programación dinámica

3. **Interfaz Gráfica**
   - GUI con tkinter
   - Visualización de rutas en mapa

4. **Testing**
   - Unit tests con pytest
   - Test coverage analysis

5. **API REST**
   - Exponer funcionalidades mediante API
   - Usar Flask o FastAPI

---

## 📝 Autores Originales

- Elias David Arrieta Olivero – 2250952
- Emanuel Miranda Sinning – 2250913
- Mario Jose Moreno Ramirez – 2250941
- Miguel Angel Plata Tello – 2211245
- Gabriel Alejandro Zambrano Herazo – 2250944
- Daniel Esteban Romero Dueñes – 2250948

---


---


---
