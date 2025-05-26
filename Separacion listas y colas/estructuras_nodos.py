"""
Módulo que contiene las implementaciones de las clases Pila (con nodos) y Cola.
"""

from collections import deque

class Nodo:
    """Representa un nodo individual en una estructura enlazada (como una Pila)."""
    def __init__(self, dato):
        """Inicializa un nodo con un dato y sin enlace al siguiente."""
        self.dato = dato
        self.siguiente = None

class Pila:
    """Representa una Pila (Stack) utilizando una estructura de nodos enlazados.

    Atributos:
        tope (Nodo | None): Referencia al nodo en la cima de la pila.
    """
    def __init__(self):
        """Inicializa una pila vacía (sin tope)."""
        self.tope = None
        self._tamano = 0 # Para mantener el tamaño eficientemente

    def esta_vacia(self):
        """Verifica si la pila está vacía.

        Retorna:
            bool: True si la pila está vacía (sin tope), False en caso contrario.
        """
        return self.tope is None

    def apilar(self, item):
        """Agrega un elemento a la cima de la pila.

        Crea un nuevo nodo con el item y lo enlaza al tope actual.

        Args:
            item: El elemento a agregar.
        """
        nuevo_nodo = Nodo(item)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self._tamano += 1

    def desapilar(self):
        """Elimina y retorna el elemento de la cima de la pila.

        Retorna:
            El dato del nodo que estaba en la cima.

        Lanza:
            IndexError: Si la pila está vacía.
        """
        if self.esta_vacia():
            raise IndexError("desapilar desde una pila vacía")
        dato_desapilado = self.tope.dato
        self.tope = self.tope.siguiente # Mueve el tope al siguiente nodo
        self._tamano -= 1
        return dato_desapilado

    def ver_tope(self):
        """Retorna el elemento de la cima de la pila sin eliminarlo.

        Retorna:
            El dato del nodo en la cima.

        Lanza:
            IndexError: Si la pila está vacía.
        """
        if self.esta_vacia():
            raise IndexError("ver tope de una pila vacía")
        return self.tope.dato

    def __len__(self):
        """Retorna el número de elementos en la pila."""
        return self._tamano
        # Alternativa (menos eficiente): recorrer y contar
        # contador = 0
        # actual = self.tope
        # while actual:
        #     contador += 1
        #     actual = actual.siguiente
        # return contador

    def __str__(self):
        """Retorna una representación en cadena de la pila (cima a la izquierda).

        Ejemplo: [DatoTope -> DatoSiguiente -> ... -> DatoBase]
        """
        elementos = []
        actual = self.tope
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        # Para que coincida con el formato LIFO de la lista anterior [..., penultimo, ultimo_en_entrar]
        # podríamos invertirlo, pero la representación natural de nodos es tope->siguiente
        # return "[" + " -> ".join(elementos) + "]"
        # Mantendremos el formato similar al de lista para consistencia con el ejemplo:
        return str(elementos[::-1]) # Invertimos para mostrar [base, ..., tope]


class Cola:
    """Representa una Cola (Queue) utilizando collections.deque para eficiencia.

    Atributos:
        items (deque): Deque interno para almacenar los elementos de la cola.
    """
    def __init__(self):
        """Inicializa una cola vacía."""
        self.items = deque()

    def esta_vacia(self):
        """Verifica si la cola está vacía.

        Retorna:
            bool: True si la cola está vacía, False en caso contrario.
        """
        return not self.items

    def encolar(self, item):
        """Agrega un elemento al final de la cola.

        Args:
            item: El elemento a agregar.
        """
        self.items.append(item)

    def desencolar(self):
        """Elimina y retorna el elemento del frente de la cola.

        Retorna:
            El elemento del frente de la cola.

        Lanza:
            IndexError: Si la cola está vacía.
        """
        if not self.esta_vacia():
            return self.items.popleft()
        else:
            raise IndexError("desencolar desde una cola vacía")

    def ver_frente(self):
        """Retorna el elemento del frente de la cola sin eliminarlo.

        Retorna:
            El elemento del frente de la cola.

        Lanza:
            IndexError: Si la cola está vacía.
        """
        if not self.esta_vacia():
            return self.items[0]
        else:
            raise IndexError("ver frente de una cola vacía")

    def tamano(self):
        """Retorna el número de elementos en la cola."""
        return len(self.items)

    def __len__(self):
        """Retorna el número de elementos en la cola."""
        return len(self.items)

    def __str__(self):
        """Retorna una representación en cadena de la cola (frente a la izquierda)."""
        return str(list(self.items)) # Convertir deque a lista para mostrar

