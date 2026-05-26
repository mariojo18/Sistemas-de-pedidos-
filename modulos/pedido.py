"""
Módulo que contiene la clase Pedido
Representa un pedido individual con su información y estado
"""


class Pedido:
    """
    Clase que representa un pedido en el sistema.
    
    Atributos:
        numPedido (int): Número único del pedido
        id_tienda (int): ID de la tienda que genera el pedido
        producto (str): Nombre del producto a entregar
        estado (str): Estado actual del pedido (Pendiente, Enviado, Entregado)
        x_entrega (float): Coordenada X del punto de entrega
        y_entrega (float): Coordenada Y del punto de entrega
        siguiente (Pedido): Referencia al siguiente pedido en la lista
    """
    
    def __init__(self, numPedido, id_tienda, producto, x_entrega, y_entrega):
        """
        Inicializa un nuevo pedido.
        
        Args:
            numPedido (int): Número único del pedido
            id_tienda (int): ID de la tienda que genera el pedido
            producto (str): Nombre del producto
            x_entrega (float): Coordenada X de entrega
            y_entrega (float): Coordenada Y de entrega
        """
        self.numPedido = numPedido
        self.id_tienda = id_tienda
        self.producto = producto
        self.estado = "Pendiente"
        self.x_entrega = x_entrega
        self.y_entrega = y_entrega
        self.siguiente = None

    def __str__(self):
        """Representación en string del pedido"""
        return f"{self.numPedido} | {self.id_tienda} | {self.producto} | {self.estado}"

    def cambiar_estado(self, nuevo_estado):
        """
        Cambia el estado del pedido.
        
        Args:
            nuevo_estado (str): Nuevo estado del pedido
        """
        self.estado = nuevo_estado

    def obtener_info(self):
        """
        Retorna un diccionario con la información del pedido.
        
        Returns:
            dict: Información completa del pedido
        """
        return {
            'numPedido': self.numPedido,
            'id_tienda': self.id_tienda,
            'producto': self.producto,
            'estado': self.estado,
            'x_entrega': self.x_entrega,
            'y_entrega': self.y_entrega
        }
