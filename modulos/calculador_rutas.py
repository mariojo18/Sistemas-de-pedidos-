"""
Módulo de utilidades matemáticas
Contiene funciones para cálculos de distancia y rutas
"""

from itertools import permutations


class CalculadorRutas:
    """
    Clase que contiene métodos para calcular distancias y optimizar rutas.
    """

    @staticmethod
    def calcular_distancia(x1, y1, x2, y2):
        """
        Calcula la distancia euclidiana entre dos puntos.
        
        Args:
            x1 (float): Coordenada X del primer punto
            y1 (float): Coordenada Y del primer punto
            x2 (float): Coordenada X del segundo punto
            y2 (float): Coordenada Y del segundo punto
        
        Returns:
            float: Distancia euclidiana redondeada a 2 decimales
        """
        return round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 2)

    @staticmethod
    def calcular_ruta_optima(pedidos, tiendas_dict, x_inicio, y_inicio):
        """
        Calcula la ruta óptima usando fuerza bruta (permutaciones).
        
        Args:
            pedidos (list): Lista de pedidos a entregar
            tiendas_dict (dict): Diccionario de tiendas por ID
            x_inicio (float): Coordenada X inicial del repartidor
            y_inicio (float): Coordenada Y inicial del repartidor
        
        Returns:
            tuple: (ruta_optima, distancia_total)
                - ruta_optima: lista de pedidos en orden óptimo
                - distancia_total: distancia total de la ruta
        """
        if not pedidos:
            return [], 0

        mejor_ruta = None
        mejor_distancia = float('inf')

        for ruta in permutations(pedidos):
            distancia_total = 0
            x_actual, y_actual = x_inicio, y_inicio

            for pedido in ruta:
                tienda = tiendas_dict.get(pedido.id_tienda)
                if tienda:
                    distancia_total += CalculadorRutas.calcular_distancia(
                        x_actual, y_actual, tienda.x, tienda.y
                    )
                    x_actual, y_actual = tienda.x, tienda.y

                distancia_total += CalculadorRutas.calcular_distancia(
                    x_actual, y_actual, pedido.x_entrega, pedido.y_entrega
                )
                x_actual, y_actual = pedido.x_entrega, pedido.y_entrega

            if distancia_total < mejor_distancia:
                mejor_distancia = distancia_total
                mejor_ruta = ruta

        return mejor_ruta, mejor_distancia
