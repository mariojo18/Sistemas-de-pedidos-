"""
Módulo principal - Sistema de Gestión de Pedidos y Rutas de Entrega
Integra todos los componentes del sistema
"""

from pedido import Pedido
from gestor_tiendas import GestorTiendas
from gestor_arbol_bst import GestorArbolBST
from calculador_rutas import CalculadorRutas
from gestor_grafo import GestorGrafo          # ← NUEVO


class SistemaPedidos:
    def __init__(self):
        self.gestor_tiendas = GestorTiendas()
        self.gestor_arbol = GestorArbolBST()
        self.gestor_grafo = GestorGrafo()   
        self.contador_pedidos = 1

    def agregar_tienda(self, nombre, x, y):
        self.gestor_tiendas.agregar_tienda(nombre, x, y)
        id_nuevo = self.gestor_tiendas.contar_tiendas()   
        self.gestor_grafo.agregar_tienda(id_nuevo, nombre, x, y) 

    def mostrar_tiendas(self):
        self.gestor_tiendas.mostrar_tiendas()

    def _obtener_tienda(self, id_tienda):
        return self.gestor_tiendas.buscar_tienda(id_tienda)

    def agregar_pedido(self, id_tienda, producto, x_entrega, y_entrega):
        if not self._obtener_tienda(id_tienda):
            print("Error: La tienda no existe.")
            return

        numPedido = self.contador_pedidos
        self.contador_pedidos += 1

        nuevo_pedido = Pedido(numPedido, id_tienda, producto, x_entrega, y_entrega)
        self.gestor_arbol.insertar(nuevo_pedido)

        print("Pedido creado con exito")
        print(f"Numero de pedido: {numPedido}")

    def buscar_pedido(self, numPedido):
        pedido = self.gestor_arbol.buscar(numPedido)

        if pedido:
            print(pedido)
        else:
            print("Ese pedido no aparece.")

    def imprimir_pedidos_ordenados(self):
        self.gestor_arbol.imprimir_inorden()

    def contar_pedidos(self):
        return self.contador_pedidos - 1
    
    def mostrar_pedidos_por_tienda(self, id_tienda):
        encontrado = self.gestor_arbol.buscar_por_tienda(id_tienda)

        if not encontrado:
            print("No hay pedidos de esa tienda.")

    def pedidos_en_rango(self, num_min, num_max):
        encontrado = self.gestor_arbol.pedidos_en_rango(num_min, num_max)

        if not encontrado:
            print("No hay pedidos en ese rango.")

    def asignar_repartidor(self, x_repartidor, y_repartidor):
        pendientes = self.gestor_arbol.obtener_pendientes()

        if not pendientes:
            print("No hay pedidos pendientes.")
            return

        print(f"\nRepartidor en: ({x_repartidor}, {y_repartidor})")
        print(f"Pedidos pendientes: {len(pendientes)}")

        tiendas_dict = self.gestor_tiendas.obtener_tiendas_como_dict()
        ruta, distancia_total = CalculadorRutas.calcular_ruta_optima(
            pendientes, tiendas_dict, x_repartidor, y_repartidor
        )

        if ruta:
            print(f"Distancia total: {distancia_total} unidades")
            punto_actual = (x_repartidor, y_repartidor)

            for pedido in ruta:
                tienda = self._obtener_tienda(pedido.id_tienda)
                dist_tienda = CalculadorRutas.calcular_distancia(
                    punto_actual[0], punto_actual[1], tienda.x, tienda.y
                )
                print(f"Tienda {pedido.id_tienda} -> {dist_tienda}")
                punto_actual = (tienda.x, tienda.y)

                dist_entrega = CalculadorRutas.calcular_distancia(
                    punto_actual[0], punto_actual[1], pedido.x_entrega, pedido.y_entrega
                )
                print(f"Pedido #{pedido.numPedido} -> {dist_entrega}")
                punto_actual = (pedido.x_entrega, pedido.y_entrega)
                pedido.cambiar_estado("Enviado")

            print(f"{len(ruta)} pedidos enviados.")
        else:
            print("No se pudo calcular ruta.")

    def marcar_entregado(self, numPedido):
        pedido = self.gestor_arbol.buscar(numPedido)

        if pedido:
            pedido.cambiar_estado("Entregado")
            print(f"Pedido {numPedido} ya se entregó.")
        else:
            print("No se encontró ese pedido.")
            
    def mostrar_pendientes(self):
        contador = self.gestor_arbol.contar_pendientes()
        print(f"Quedan {contador} pendientes.")
        return contador

    def obtener_altura_arbol(self):
        altura = self.gestor_arbol.obtener_altura()
        print(f"Altura: {altura}")
        return altura

    def limpiar_sistema(self):
        self.gestor_tiendas.limpiar_tiendas()
        self.gestor_arbol.limpiar()
        self.contador_pedidos = 1
        print("Se borró todo.")

    def obtener_estadisticas(self):
        return {
            'total_tiendas': self.gestor_tiendas.contar_tiendas(),
            'total_pedidos': self.contar_pedidos(),
            'pedidos_pendientes': self.gestor_arbol.contar_pendientes(),
            'altura_arbol': self.gestor_arbol.obtener_altura()
        }
