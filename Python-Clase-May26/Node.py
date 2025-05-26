"""
Este m dulo define la clase `Node` que representa un nodo dentro de una estructura de datos lineal din mica.

La clase `Node` tiene los siguientes atributos:
- `siguiente`: referencia al pr ximo nodo en la lista.
- `dato`: valor almacena en el nodo.

La clase `Node` tiene el siguiente m todo:
- `__init__`: inicializa una nueva instancia de `Node` con el valor `dato` y sin pr ximo nodo.
"""

class Node:
    def __init__(self, dato):
        self.siguiente = None
        self.dato = dato