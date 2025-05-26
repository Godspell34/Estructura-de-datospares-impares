# ------------------------

# Este archivo define un menú de usuario que permite interactuar con una estructura de datos de tipo Cola.
# El usuario puede encolar datos, recorrer la cola para apilar los elementos en posiciones impares, e imprimir la cola actual.

from Cola import Cola

def menu_usuario():
    cola = Cola()
    pila_con_datos = None
    while True:
        print("\n--- MENÚ ---")
        print("1. Encolar un dato")
        print("2. Recorrer cola y apilar impares")
        print("3. Imprimir cola")
        print("4. Imprimir pila con datos impares")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            while True:
                dato = input("Ingresa el dato a encolar: ")
                cola.empujar(dato)
                opt = input("¿Deseas agregar otro dato? (s/n): ")
                if opt.lower() != "s":
                    break

        elif opcion == "2":
            print("Recorriendo cola y apilando impares...")
            pila_con_datos = cola.recorrer_cola()
            
        elif opcion == "3":
            cola.imprimir_cola()
        
        elif opcion == "4":
            if pila_con_datos is not None:
                print("Imprimiendo pila con datos impares:")
                pila_con_datos.imprimir_pila()
            else:
                print("No hay datos en la pila. Primero recorre la cola.")

        elif opcion == "0":
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar
if __name__ == "__main__":
    
    menu_usuario()