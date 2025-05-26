"""
Módulo principal que implementa la lógica de separación y demuestra su uso
utilizando una Pila basada en nodos.
"""

# Importar las clases Pila (basada en nodos) y Cola desde el nuevo módulo
from estructuras_nodos import Pila, Cola

def separar_cola(cola_original: Cola) -> Pila:
    """Separa los elementos de una cola dada.

    Los elementos en posiciones pares (0, 2, 4, ...) permanecen en la cola original.
    Los elementos en posiciones impares (1, 3, 5, ...) se mueven a una nueva pila
    (implementada con nodos).
    La operación se realiza recorriendo la cola original una sola vez.

    Args:
        cola_original (Cola): La cola que contiene los elementos a separar.
                              Esta cola será modificada en el proceso.

    Returns:
        Pila: Una nueva pila (basada en nodos) que contiene los elementos que
              estaban en las posiciones impares de la cola original, en orden LIFO.
    """
    pila_impares = Pila() # Ahora es una Pila basada en nodos
    tamano_original = len(cola_original)
    indice = 0

    # Recorremos la cola basándonos en su tamaño original
    while indice < tamano_original:
        try:
            # Sacamos el elemento del frente
            elemento = cola_original.desencolar()

            # Verificamos la posición (par o impar)
            if indice % 2 == 0:
                # Posición par: el elemento vuelve al final de la cola
                cola_original.encolar(elemento)
            else:
                # Posición impar: el elemento va a la pila
                pila_impares.apilar(elemento)
        except IndexError:
            # Seguridad: Si la cola se vacía inesperadamente
            print("Advertencia: La cola se vació antes de lo esperado.")
            break

        # Incrementamos el índice para la siguiente posición
        indice += 1

    return pila_impares

# --- Bloque principal para demostración ---
if __name__ == "__main__":
    print("--- Ejemplo 1: Cola [A, B, C, D, E]  ---")
    cola_ejemplo1 = Cola()
    elementos1 = ["A", "B", "C", "D", "E"]
    for elem in elementos1:
        cola_ejemplo1.encolar(elem)

    print(f"Cola original: {cola_ejemplo1}")

    pila_resultado1 = separar_cola(cola_ejemplo1)

    print(f"Cola resultante (pares): {cola_ejemplo1}")
    # La representación __str__ de la Pila de nodos muestra [base, ..., tope]
    print(f"Pila resultante (impares): {pila_resultado1}") 
    print("-----------------------------------------------------------")

    print("--- Ejemplo 2: Cola [1, 2, 3, 4, 5, 6] ---")
    cola_ejemplo2 = Cola()
    elementos2 = [1, 2, 3, 4, 5, 6]
    for elem in elementos2:
        cola_ejemplo2.encolar(elem)

    print(f"Cola original: {cola_ejemplo2}")

    pila_resultado2 = separar_cola(cola_ejemplo2)

    print(f"Cola resultante (pares): {cola_ejemplo2}")
    print(f"Pila resultante (impares): {pila_resultado2}")
    print("-----------------------------------------------------------")

    print("--- Ejemplo 3: Cola vacía []  ---")
    cola_ejemplo3 = Cola()

    print(f"Cola original: {cola_ejemplo3}")

    pila_resultado3 = separar_cola(cola_ejemplo3)

    print(f"Cola resultante (pares): {cola_ejemplo3}")
    print(f"Pila resultante (impares): {pila_resultado3}")
    print("-----------------------------------------------------------")

    print("--- Ejemplo 4: Cola con un elemento [Z]  ---")
    cola_ejemplo4 = Cola()
    cola_ejemplo4.encolar("Z")

    print(f"Cola original: {cola_ejemplo4}")

    pila_resultado4 = separar_cola(cola_ejemplo4)

    print(f"Cola resultante (pares): {cola_ejemplo4}")
    print(f"Pila resultante (impares): {pila_resultado4}")
    print("-----------------------------------------------------------")

