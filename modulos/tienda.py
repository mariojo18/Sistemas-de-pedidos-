"""
Módulo que contiene la clase Tienda
Representa una tienda en la red de distribución
"""


class Tienda:
    """
    Clase que representa una tienda en el sistema.
    
    Atributos:
        id_tienda (int): Identificador único de la tienda
        nombre (str): Nombre de la tienda
        x (float): Coordenada X de ubicación
        y (float): Coordenada Y de ubicación
        siguiente (Tienda): Referencia a la siguiente tienda en la lista
    """
    
    def __init__(self, id_tienda, nombre, x, y):
        """
        Inicializa una nueva tienda.
        
        Args:
            id_tienda (int): Identificador único de la tienda
            nombre (str): Nombre de la tienda
            x (float): Coordenada X de ubicación
            y (float): Coordenada Y de ubicación
        """
        self.id_tienda = id_tienda
        self.nombre = nombre
        self.x = x
        self.y = y
        self.siguiente = None

    def __str__(self):
        """Representación en string de la tienda"""
        return f"ID: {self.id_tienda} | {self.nombre} | Ubicación: ({self.x}, {self.y})"

    def obtener_ubicacion(self):
        """
        Retorna las coordenadas de la tienda.
        
        Returns:
            tuple: (x, y) coordenadas de la tienda
        """
        return (self.x, self.y)

    def obtener_info(self):
        """
        Retorna un diccionario con la información de la tienda.
        
        Returns:
            dict: Información completa de la tienda
        """
        return {
            'id_tienda': self.id_tienda,
            'nombre': self.nombre,
            'x': self.x,
            'y': self.y
        }
