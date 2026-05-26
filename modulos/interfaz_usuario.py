"""
Módulo de Interfaz de Usuario
Contiene el menú principal y la interacción con el usuario
"""

from sistema_pedidos import SistemaPedidos


class InterfazUsuario:
    """
    Clase que maneja la interfaz de usuario del sistema.
    """

    def __init__(self):
        """Inicializa la interfaz del usuario."""
        self.sistema = SistemaPedidos()

    def mostrar_menu_principal(self):
        """Muestra el menú principal."""
        print("\n" + "=" * 50)
        print("SISTEMA DE GESTIÓN DE PEDIDOS Y RUTAS")
        print("=" * 50)
        print("1.  Agregar tienda")
        print("2.  Agregar pedido")
        print("3.  Buscar pedido")
        print("4.  Asignar repartidor")
        print("5.  Marcar entregado")
        print("6.  Mostrar pedidos ordenados")
        print("7.  Pedidos pendientes")
        print("8.  Buscar por tienda")
        print("9.  Altura del árbol")
        print("10. Buscar pedidos en rango")
        print("11. Mostrar estadísticas")
        print("12. Limpiar todo")
        print("--- Red de Tiendas (Grafo) ---")
        print("13. Conectar dos tiendas")
        print("14. Eliminar ruta entre tiendas")
        print("15. Eliminar tienda del grafo")
        print("16. Buscar tienda en el grafo")
        print("17. Ver ruta directa entre tiendas")
        print("18. Ruta más corta entre tiendas")
        print("19. Ver red completa de tiendas")
        print("0.  Salir")
        print("=" * 50)

    def opcion_agregar_tienda(self):
        """Maneja la opción de agregar tienda."""
        nombre = input("Nombre tienda: ").strip()
        try:
            x = float(input("Coordenada X: "))
            y = float(input("Coordenada Y: "))
            self.sistema.agregar_tienda(nombre, x, y)
        except ValueError:
            print("Error: Las coordenadas deben ser números.")

    def opcion_agregar_pedido(self):
        """Maneja la opción de agregar pedido."""
        self.sistema.mostrar_tiendas()
        try:
            id_tienda = int(input("ID tienda: "))
            producto = input("Producto: ").strip()
            x_entrega = float(input("Coordenada X de entrega: "))
            y_entrega = float(input("Coordenada Y de entrega: "))
            self.sistema.agregar_pedido(id_tienda, producto, x_entrega, y_entrega)
        except ValueError:
            print("Error: Entrada inválida.")

    def opcion_buscar_pedido(self):
        """Maneja la opción de buscar pedido."""
        try:
            num = int(input("Numero de pedido: "))
            self.sistema.buscar_pedido(num)
        except ValueError:
            print("Error: El número debe ser entero.")

    def opcion_asignar_repartidor(self):
        """Maneja la opción de asignar repartidor."""
        try:
            x_repartidor = float(input("Coordenada X del repartidor: "))
            y_repartidor = float(input("Coordenada Y del repartidor: "))
            self.sistema.asignar_repartidor(x_repartidor, y_repartidor)
        except ValueError:
            print("Error: Las coordenadas deben ser números.")

    def opcion_marcar_entregado(self):
        """Maneja la opción de marcar pedido como entregado."""
        try:
            num = int(input("Numero de pedido: "))
            self.sistema.marcar_entregado(num)
        except ValueError:
            print("Error: El número debe ser entero.")

    def opcion_mostrar_pedidos_ordenados(self):
        """Maneja la opción de mostrar pedidos ordenados."""
        self.sistema.imprimir_pedidos_ordenados()

    def opcion_pedidos_pendientes(self):
        """Maneja la opción de mostrar pedidos pendientes."""
        self.sistema.mostrar_pendientes()

    def opcion_buscar_por_tienda(self):
        """Maneja la opción de buscar pedidos por tienda."""
        self.sistema.mostrar_tiendas()
        try:
            id_tienda = int(input("ID tienda: "))
            self.sistema.mostrar_pedidos_por_tienda(id_tienda)
        except ValueError:
            print("Error: El ID debe ser entero.")

    def opcion_altura_arbol(self):
        """Maneja la opción de mostrar altura del árbol."""
        self.sistema.obtener_altura_arbol()

    def opcion_pedidos_en_rango(self):
        """Maneja la opción de buscar pedidos en rango."""
        try:
            num_min = int(input("Desde pedido número: "))
            num_max = int(input("Hasta pedido número: "))
            self.sistema.pedidos_en_rango(num_min, num_max)
        except ValueError:
            print("Error: Los números deben ser enteros.")

    def opcion_estadisticas(self):
        """Maneja la opción de mostrar estadísticas."""
        stats = self.sistema.obtener_estadisticas()
        print("\n" + "=" * 50)
        print("ESTADÍSTICAS DEL SISTEMA")
        print("=" * 50)
        print(f"Total de tiendas: {stats['total_tiendas']}")
        print(f"Total de pedidos: {stats['total_pedidos']}")
        print(f"Pedidos pendientes: {stats['pedidos_pendientes']}")
        print(f"Altura del árbol: {stats['altura_arbol']}")
        print("=" * 50)

    def opcion_limpiar_todo(self):
        """Maneja la opción de limpiar todo."""
        confirmacion = input("¿Está seguro de que desea limpiar todo? (s/n): ").lower()
        if confirmacion == 's':
            self.sistema.limpiar_sistema()
        else:
            print("Operación cancelada.")

    # ── NUEVOS MÉTODOS — Grafo ─────────────────────────────────────────

    def opcion_conectar_tiendas(self):
        """Conecta dos tiendas con una ruta en el grafo."""
        try:
            id_a = int(input("ID tienda origen: "))
            id_b = int(input("ID tienda destino: "))
            resp = input("¿Ingresar peso manualmente? (s/n): ").strip().lower()
            peso = float(input("Peso: ")) if resp == 's' else None
            self.sistema.gestor_grafo.agregar_ruta(id_a, id_b, peso)
        except ValueError:
            print("Error: Entrada inválida.")

    def opcion_eliminar_ruta(self):
        """Elimina la ruta directa entre dos tiendas."""
        try:
            id_a = int(input("ID tienda origen: "))
            id_b = int(input("ID tienda destino: "))
            self.sistema.gestor_grafo.eliminar_ruta(id_a, id_b)
        except ValueError:
            print("Error: Entrada inválida.")

    def opcion_eliminar_tienda_grafo(self):
        """Elimina una tienda del grafo."""
        try:
            id_t = int(input("ID tienda: "))
            self.sistema.gestor_grafo.eliminar_tienda(id_t)
        except ValueError:
            print("Error: Entrada inválida.")

    def opcion_buscar_tienda_grafo(self):
        """Busca una tienda en el grafo."""
        try:
            id_t = int(input("ID tienda: "))
            self.sistema.gestor_grafo.buscar_tienda(id_t)
        except ValueError:
            print("Error: Entrada inválida.")

    def opcion_ruta_directa(self):
        """Consulta si hay ruta directa entre dos tiendas."""
        try:
            id_a = int(input("ID tienda origen: "))
            id_b = int(input("ID tienda destino: "))
            self.sistema.gestor_grafo.buscar_ruta(id_a, id_b)
        except ValueError:
            print("Error: Entrada inválida.")

    def opcion_ruta_mas_corta(self):
        """Calcula la ruta más corta (Dijkstra) entre dos tiendas."""
        try:
            id_a = int(input("ID tienda origen: "))
            id_b = int(input("ID tienda destino: "))
            self.sistema.gestor_grafo.ruta_mas_corta(id_a, id_b)
        except ValueError:
            print("Error: Entrada inválida.")

    def opcion_mostrar_grafo(self):
        """Muestra la red completa de tiendas."""
        self.sistema.gestor_grafo.mostrar_grafo()

    # ── BUCLE PRINCIPAL ───────────────────────────────────────────────

    def ejecutar(self):
        """Ejecuta el bucle principal de la interfaz."""
        while True:
            self.mostrar_menu_principal()
            opcion = input("Elige una opción: ").strip()

            if opcion == "1":
                self.opcion_agregar_tienda()
            elif opcion == "2":
                self.opcion_agregar_pedido()
            elif opcion == "3":
                self.opcion_buscar_pedido()
            elif opcion == "4":
                self.opcion_asignar_repartidor()
            elif opcion == "5":
                self.opcion_marcar_entregado()
            elif opcion == "6":
                self.opcion_mostrar_pedidos_ordenados()
            elif opcion == "7":
                self.opcion_pedidos_pendientes()
            elif opcion == "8":
                self.opcion_buscar_por_tienda()
            elif opcion == "9":
                self.opcion_altura_arbol()
            elif opcion == "10":
                self.opcion_pedidos_en_rango()
            elif opcion == "11":
                self.opcion_estadisticas()
            elif opcion == "12":
                self.opcion_limpiar_todo()
            elif opcion == "13":
                self.opcion_conectar_tiendas()
            elif opcion == "14":
                self.opcion_eliminar_ruta()
            elif opcion == "15":
                self.opcion_eliminar_tienda_grafo()
            elif opcion == "16":
                self.opcion_buscar_tienda_grafo()
            elif opcion == "17":
                self.opcion_ruta_directa()
            elif opcion == "18":
                self.opcion_ruta_mas_corta()
            elif opcion == "19":
                self.opcion_mostrar_grafo()
            elif opcion == "0":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente de nuevo.")


def main():
    """Función principal que inicia la aplicación."""
    interfaz = InterfazUsuario()
    interfaz.ejecutar()


if __name__ == "__main__":
    main()
