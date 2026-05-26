"""
Módulo para la gestión del árbol binario de búsqueda (BST)
Contiene operaciones sobre el árbol de pedidos
"""

from nodo_arbol import NodoArbol


class GestorArbolBST:
    """
    Clase que gestiona las operaciones del árbol binario de búsqueda.
    """

    def __init__(self):
        """Inicializa el gestor del árbol."""
        self.raiz = None

    def insertar(self, pedido):
        """
        Inserta un pedido en el árbol.
        
        Args:
            pedido (Pedido): Pedido a insertar
        """
        self.raiz = self._insertar_recursivo(self.raiz, pedido)

    def _insertar_recursivo(self, nodo, pedido):
        """
        Inserta un pedido recursivamente en el árbol.
        
        Args:
            nodo (NodoArbol): Nodo actual
            pedido (Pedido): Pedido a insertar
        
        Returns:
            NodoArbol: Nodo actualizado
        """
        if nodo is None:
            return NodoArbol(pedido)

        if pedido.numPedido < nodo.pedido.numPedido:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, pedido)
        else:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, pedido)

        return nodo

    def buscar(self, numPedido):
        """
        Busca un pedido por su número.
        
        Args:
            numPedido (int): Número del pedido a buscar
        
        Returns:
            Pedido: Pedido encontrado o None
        """
        return self._buscar_recursivo(self.raiz, numPedido)

    def _buscar_recursivo(self, nodo, numPedido):
        """
        Busca recursivamente un pedido en el árbol.
        
        Args:
            nodo (NodoArbol): Nodo actual
            numPedido (int): Número del pedido a buscar
        
        Returns:
            Pedido: Pedido encontrado o None
        """
        if nodo is None:
            return None

        if nodo.pedido.numPedido == numPedido:
            return nodo.pedido

        if numPedido < nodo.pedido.numPedido:
            return self._buscar_recursivo(nodo.izquierda, numPedido)
        else:
            return self._buscar_recursivo(nodo.derecha, numPedido)

    def imprimir_inorden(self):
        """Imprime los pedidos en orden (inorden)."""
        if self.raiz is None:
            print("No hay nada guardado.")
            return

        self._inorden(self.raiz)

    def _inorden(self, nodo):
        """
        Recorrido inorden del árbol.
        
        Args:
            nodo (NodoArbol): Nodo actual
        """
        if nodo is not None:
            self._inorden(nodo.izquierda)
            print(nodo.pedido)
            self._inorden(nodo.derecha)

    def obtener_pendientes(self):
        """
        Obtiene todos los pedidos pendientes.
        
        Returns:
            list: Lista de pedidos pendientes
        """
        pendientes = []
        self._recorrer_pendientes(self.raiz, pendientes)
        return pendientes

    def _recorrer_pendientes(self, nodo, pendientes):
        """
        Recorre el árbol buscando pedidos pendientes.
        
        Args:
            nodo (NodoArbol): Nodo actual
            pendientes (list): Lista donde almacenar pedidos pendientes
        """
        if nodo is not None:
            self._recorrer_pendientes(nodo.izquierda, pendientes)
            if nodo.pedido.estado == "Pendiente":
                pendientes.append(nodo.pedido)
            self._recorrer_pendientes(nodo.derecha, pendientes)

    def contar_pendientes(self):
        """
        Cuenta los pedidos pendientes.
        
        Returns:
            int: Número de pedidos pendientes
        """
        return self._contar_pendientes_recursivo(self.raiz)

    def _contar_pendientes_recursivo(self, nodo):
        """
        Cuenta recursivamente los pedidos pendientes.
        
        Args:
            nodo (NodoArbol): Nodo actual
        
        Returns:
            int: Contador de pendientes
        """
        if nodo is None:
            return 0

        contador = 1 if nodo.pedido.estado == "Pendiente" else 0

        return (
            contador
            + self._contar_pendientes_recursivo(nodo.izquierda)
            + self._contar_pendientes_recursivo(nodo.derecha)
        )

    def buscar_por_tienda(self, id_tienda):
        """
        Busca pedidos de una tienda específica.
        
        Args:
            id_tienda (int): ID de la tienda
        
        Returns:
            bool: True si encuentra pedidos, False si no
        """
        return self._buscar_tienda_recursivo(self.raiz, id_tienda)

    def _buscar_tienda_recursivo(self, nodo, id_tienda):
        """
        Busca recursivamente pedidos de una tienda.
        
        Args:
            nodo (NodoArbol): Nodo actual
            id_tienda (int): ID de la tienda
        
        Returns:
            bool: True si encuentra pedidos
        """
        if nodo is None:
            return False

        encontrado = False

        if nodo.pedido.id_tienda == id_tienda:
            print(nodo.pedido)
            encontrado = True

        izq = self._buscar_tienda_recursivo(nodo.izquierda, id_tienda)
        der = self._buscar_tienda_recursivo(nodo.derecha, id_tienda)

        return encontrado or izq or der

    def obtener_altura(self):
        """
        Obtiene la altura del árbol.
        
        Returns:
            int: Altura del árbol
        """
        return self._altura(self.raiz)

    def _altura(self, nodo):
        """
        Calcula recursivamente la altura del árbol.
        
        Args:
            nodo (NodoArbol): Nodo actual
        
        Returns:
            int: Altura desde este nodo
        """
        if nodo is None:
            return 0

        return 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))

    def pedidos_en_rango(self, num_min, num_max):
        """
        Obtiene pedidos en un rango de números.
        
        Args:
            num_min (int): Número mínimo
            num_max (int): Número máximo
        
        Returns:
            bool: True si encuentra pedidos en rango
        """
        print(f"Pedidos del {num_min} al {num_max}")
        return self._rango_recursivo(self.raiz, num_min, num_max)

    def _rango_recursivo(self, nodo, num_min, num_max):
        """
        Busca recursivamente pedidos en rango.
        
        Args:
            nodo (NodoArbol): Nodo actual
            num_min (int): Número mínimo
            num_max (int): Número máximo
        
        Returns:
            bool: True si encuentra pedidos
        """
        if nodo is None:
            return False

        encontrado = False

        if nodo.pedido.numPedido > num_min:
            encontrado = self._rango_recursivo(nodo.izquierda, num_min, num_max) or encontrado

        if num_min <= nodo.pedido.numPedido <= num_max:
            print(nodo.pedido)
            encontrado = True

        if nodo.pedido.numPedido < num_max:
            encontrado = self._rango_recursivo(nodo.derecha, num_min, num_max) or encontrado

        return encontrado

    def limpiar(self):
        """Limpia el árbol."""
        self.raiz = None
