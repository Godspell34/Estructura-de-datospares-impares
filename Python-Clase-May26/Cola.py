
"""
La clase `Cola` representa una estructura de datos de tipo cola. En una cola, los elementos se encolan (se añaden) al final y se desencolan (se eliminan) desde el frente, siguiendo el principio FIFO (First In, First Out).

Atributos:
- `frente`: referencia al primer elemento de la cola.
- `final`: referencia al último elemento de la cola.
- `actual`: referencia temporal al elemento actual de la cola, utilizado en ciertas operaciones.

Métodos:
- `__init__()`: Inicializa una nueva instancia de `Cola` con el frente, final y actual establecidos en `None`.
- `empujar(dato)`: Añade un nuevo elemento con el valor `dato` al final de la cola.
"""


from Node import Node
from Pila import Pila

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.actual = None
        
    def empujar(self, dato):
        
        nuevo = Node(dato)
        if self.frente is None:
            self.frente = self.final = nuevo
            self.actual = self.frente
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
            
    def desencolar(self):
        if self.frente is None:
            print("La cola esta vacia")
            return None
        
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        
        if self.frente is None:
            self.final = None
            
        return dato
    
    def recorrer_cola(self):
        pila_con_datos = Pila()
        self.actual = self.frente
        if self.frente == None:
            print("La cola esta vacia")
            return
        posicion = 0
            
        while self.actual:
            posicion +=1
            if posicion % 2 != 0:
                pila_con_datos.apilar(self.actual.dato)
            
            self.actual = self.actual.siguiente
        if pila_con_datos.peek is None:
            print("No hay datos en posiciones impares.")
        
        pila_con_datos.imprimir_pila()
        return pila_con_datos
    
    def imprimir_cola(self):
        contenido = []
        actual = self.frente
        while actual:
            contenido.append(actual.dato)
            actual = actual.siguiente
        texto_a_imprimir = "Cola: " + " -> ".join(contenido)
        print(texto_a_imprimir)