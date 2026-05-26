"""
Módulo que contiene la clase NodoArbol
Representa un nodo en el árbol binario de búsqueda
"""


class NodoArbol:
    """
    Clase que representa un nodo en el árbol binario de búsqueda (BST).
    
    Atributos:
        pedido (Pedido): Pedido almacenado en este nodo
        izquierda (NodoArbol): Referencia al nodo hijo izquierdo
        derecha (NodoArbol): Referencia al nodo hijo derecho
    """
    
    def __init__(self, pedido):
        """
        Inicializa un nuevo nodo del árbol.
        
        Args:
            pedido (Pedido): El pedido a almacenar en este nodo
        """
        self.pedido = pedido
        self.izquierda = None
        self.derecha = None

    def __str__(self):
        """Representación en string del nodo"""
        return str(self.pedido)
