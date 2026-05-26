"""
Módulo para la gestión de tiendas
Maneja la lista enlazada de tiendas
"""

from tienda import Tienda


class GestorTiendas:
    """
    Clase que gestiona las operaciones sobre tiendas.
    """

    def __init__(self):
        """Inicializa el gestor de tiendas."""
        self.lista_tiendas = None
        self.contador_tiendas = 0

    def agregar_tienda(self, nombre, x, y):
        """
        Añade una nueva tienda a la lista.
        
        Args:
            nombre (str): Nombre de la tienda
            x (float): Coordenada X
            y (float): Coordenada Y
        
        Returns:
            int: ID de la tienda agregada
        """
        self.contador_tiendas += 1
        nueva = Tienda(self.contador_tiendas, nombre, x, y)
        nueva.siguiente = self.lista_tiendas
        self.lista_tiendas = nueva
        print("Tienda agregada con exito")
        print(f"ID: {self.contador_tiendas}")
        return self.contador_tiendas

    def mostrar_tiendas(self):
        """Muestra todas las tiendas registradas."""
        if self.lista_tiendas is None:
            print("No hay tiendas registradas")
            return

        actual = self.lista_tiendas
        while actual:
            print(f"ID: {actual.id_tienda} | {actual.nombre}")
            actual = actual.siguiente

    def buscar_tienda(self, id_tienda):
        """
        Busca una tienda por su ID.
        
        Args:
            id_tienda (int): ID de la tienda a buscar
        
        Returns:
            Tienda: Objeto Tienda si se encuentra, None si no existe
        """
        actual = self.lista_tiendas
        while actual:
            if actual.id_tienda == id_tienda:
                return actual
            actual = actual.siguiente
        return None

    def obtener_tiendas_como_dict(self):
        """
        Retorna todas las tiendas como un diccionario.
        
        Returns:
            dict: Diccionario con ID como clave y Tienda como valor
        """
        tiendas_dict = {}
        actual = self.lista_tiendas
        while actual:
            tiendas_dict[actual.id_tienda] = actual
            actual = actual.siguiente
        return tiendas_dict

    def limpiar_tiendas(self):
        """Elimina todas las tiendas."""
        self.lista_tiendas = None
        self.contador_tiendas = 0

    def contar_tiendas(self):
        """
        Cuenta la cantidad de tiendas.
        
        Returns:
            int: Número de tiendas registradas
        """
        contador = 0
        actual = self.lista_tiendas
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador
