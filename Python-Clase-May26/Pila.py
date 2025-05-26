
"""
La clase `Pila` representa una estructura de datos de tipo pila. En una pila, los elementos se apilan (se añaden) al final y se desapilan (se eliminan) desde el final, siguiendo el principio LIFO (Last In, First Out).

Atributos:
- `peek`: referencia al nodo tope de la pila.

Métodos:
- `__init__()`: Inicializa una nueva instancia de `Pila` con el tope establecido en `None`.
- `apilar(dato)`: Añade un nuevo elemento con el valor `dato` al final de la pila.
- `desapilar()`: Elimina el elemento tope de la pila y devuelve su valor.
"""

from Node import Node
class Pila:
    def __init__(self):
        self.peek: Node = None
    
    def apilar(self, dato):
        nuevo_nodo = Node(dato=dato)
        if self.peek == None:
            self.peek = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.peek
            self.peek = nuevo_nodo
    
    def imprimir_pila(self):
        contenido = ""
        actual = self.peek
        while actual:
            contenido += f"{actual.dato} "
            actual = actual.siguiente
        print(contenido)