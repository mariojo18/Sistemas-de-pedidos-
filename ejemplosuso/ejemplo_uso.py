"""
ejemplo_uso.py
Ejemplos de cómo usar el sistema de gestión de pedidos
"""

from sistema_pedidos import SistemaPedidos


def ejemplo_basico():
    """Ejemplo básico del uso del sistema."""
    print("=" * 60)
    print("EJEMPLO 1: Uso Básico del Sistema")
    print("=" * 60)
    
    # Crear instancia del sistema
    sistema = SistemaPedidos()
    
    # Agregar tiendas
    print("\n--- Agregando tiendas ---")
    sistema.agregar_tienda("Tienda Centro", 10.0, 20.0)
    sistema.agregar_tienda("Tienda Norte", 15.0, 35.0)
    sistema.agregar_tienda("Tienda Sur", 8.0, 5.0)
    
    # Mostrar tiendas
    print("\n--- Tiendas registradas ---")
    sistema.mostrar_tiendas()
    
    # Agregar pedidos
    print("\n--- Agregando pedidos ---")
    sistema.agregar_pedido(1, "Laptop", 12.0, 22.0)
    sistema.agregar_pedido(1, "Monitor", 11.0, 19.0)
    sistema.agregar_pedido(2, "Mouse", 16.0, 37.0)
    sistema.agregar_pedido(3, "Teclado", 9.0, 6.0)
    sistema.agregar_pedido(2, "Auriculares", 14.0, 33.0)
    
    # Mostrar pedidos ordenados
    print("\n--- Pedidos ordenados por número ---")
    sistema.imprimir_pedidos_ordenados()
    
    # Buscar pedido específico
    print("\n--- Buscando pedido #2 ---")
    sistema.buscar_pedido(2)
    
    # Mostrar pendientes
    print("\n--- Estado de pendientes ---")
    sistema.mostrar_pendientes()


def ejemplo_repartidor():
    """Ejemplo de asignación de repartidor."""
    print("\n\n" + "=" * 60)
    print("EJEMPLO 2: Asignación de Repartidor")
    print("=" * 60)
    
    sistema = SistemaPedidos()
    
    # Preparar datos
    sistema.agregar_tienda("Almacén Principal", 5.0, 5.0)
    sistema.agregar_tienda("Tienda A", 15.0, 20.0)
    sistema.agregar_tienda("Tienda B", 25.0, 30.0)
    
    sistema.agregar_pedido(1, "Caja A", 16.0, 21.0)
    sistema.agregar_pedido(2, "Caja B", 26.0, 31.0)
    sistema.agregar_pedido(1, "Caja C", 14.0, 19.0)
    
    # Asignar repartidor
    print("\n--- Asignando repartidor en (5, 5) ---")
    sistema.asignar_repartidor(5.0, 5.0)
    
    # Verificar cambios
    print("\n--- Pedidos después de entregar ---")
    sistema.imprimir_pedidos_ordenados()


def ejemplo_busquedas():
    """Ejemplo de diferentes tipos de búsquedas."""
    print("\n\n" + "=" * 60)
    print("EJEMPLO 3: Búsquedas y Consultas")
    print("=" * 60)
    
    sistema = SistemaPedidos()
    
    # Preparar datos
    sistema.agregar_tienda("Tienda 1", 10.0, 10.0)
    sistema.agregar_tienda("Tienda 2", 20.0, 20.0)
    
    for i in range(1, 6):
        tienda_id = 1 if i % 2 == 0 else 2
        sistema.agregar_pedido(tienda_id, f"Producto {i}", 12.0 + i, 12.0 + i)
    
    # Búsqueda por número
    print("\n--- Búsqueda de pedido #3 ---")
    sistema.buscar_pedido(3)
    
    # Búsqueda por tienda
    print("\n--- Pedidos de tienda 1 ---")
    sistema.mostrar_pedidos_por_tienda(1)
    
    # Búsqueda en rango
    print("\n--- Pedidos del 2 al 4 ---")
    sistema.pedidos_en_rango(2, 4)
    
    # Altura del árbol
    print("\n--- Información del árbol ---")
    sistema.obtener_altura_arbol()


def ejemplo_estadisticas():
    """Ejemplo de obtención de estadísticas."""
    print("\n\n" + "=" * 60)
    print("EJEMPLO 4: Estadísticas del Sistema")
    print("=" * 60)
    
    sistema = SistemaPedidos()
    
    # Agregar datos
    sistema.agregar_tienda("Tienda A", 0.0, 0.0)
    sistema.agregar_tienda("Tienda B", 10.0, 10.0)
    sistema.agregar_tienda("Tienda C", 20.0, 20.0)
    
    for i in range(8):
        tienda = (i % 3) + 1
        sistema.agregar_pedido(tienda, f"Item {i+1}", 5.0 + i, 5.0 + i)
    
    # Obtener estadísticas
    stats = sistema.obtener_estadisticas()
    
    print(f"\nTotal de tiendas: {stats['total_tiendas']}")
    print(f"Total de pedidos: {stats['total_pedidos']}")
    print(f"Pedidos pendientes: {stats['pedidos_pendientes']}")
    print(f"Altura del árbol: {stats['altura_arbol']}")


def ejemplo_completo():
    """Ejemplo completo con todas las operaciones."""
    print("\n\n" + "=" * 60)
    print("EJEMPLO 5: Flujo Completo de Operaciones")
    print("=" * 60)
    
    sistema = SistemaPedidos()
    
    print("\n1. CREANDO RED DE TIENDAS")
    print("-" * 40)
    tiendas = [
        ("Centro Distribución", 0.0, 0.0),
        ("Tienda Centro", 10.0, 10.0),
        ("Tienda Este", 20.0, 15.0),
        ("Tienda Oeste", 5.0, 25.0),
        ("Tienda Sur", 15.0, -10.0),
    ]
    
    for nombre, x, y in tiendas:
        sistema.agregar_tienda(nombre, x, y)
    
    print("\n2. REGISTRANDO PEDIDOS")
    print("-" * 40)
    pedidos = [
        (1, "Electrónica A", 11.0, 11.0),
        (2, "Ropa B", 21.0, 16.0),
        (3, "Muebles C", 6.0, 26.0),
        (1, "Electrónica D", 12.0, 10.0),
        (4, "Alimentos E", 16.0, -9.0),
        (2, "Ropa F", 19.0, 14.0),
        (3, "Muebles G", 7.0, 24.0),
        (1, "Electrónica H", 10.0, 12.0),
    ]
    
    for tienda, producto, x, y in pedidos:
        sistema.agregar_pedido(tienda, producto, x, y)
    
    print("\n3. ESTADÍSTICAS INICIALES")
    print("-" * 40)
    stats = sistema.obtener_estadisticas()
    for clave, valor in stats.items():
        print(f"  {clave}: {valor}")
    
    print("\n4. PRIMERA ENTREGA")
    print("-" * 40)
    sistema.asignar_repartidor(0.0, 0.0)
    
    print("\n5. PEDIDOS DESPUÉS DE ENTREGAR")
    print("-" * 40)
    sistema.mostrar_pendientes()
    
    print("\n6. MARCANDO ALGUNOS COMO ENTREGADOS")
    print("-" * 40)
    sistema.marcar_entregado(1)
    sistema.marcar_entregado(3)
    
    print("\n7. ESTADÍSTICAS FINALES")
    print("-" * 40)
    stats = sistema.obtener_estadisticas()
    for clave, valor in stats.items():
        print(f"  {clave}: {valor}")
    
    print("\n8. TODAS LAS TIENDAS")
    print("-" * 40)
    sistema.mostrar_tiendas()
    
    print("\n9. TODOS LOS PEDIDOS ORDENADOS")
    print("-" * 40)
    sistema.imprimir_pedidos_ordenados()


if __name__ == "__main__":
    # Ejecutar ejemplos
    ejemplo_basico()
    ejemplo_repartidor()
    ejemplo_busquedas()
    ejemplo_estadisticas()
    ejemplo_completo()
    
    print("\n\n" + "=" * 60)
    print("¡TODOS LOS EJEMPLOS EJECUTADOS!")
    print("=" * 60)
