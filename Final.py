import networkx as nx
from Funciones import *

# Función para insertar un grafo
def InsertarGrafo():
    G = nx.DiGraph()  # Se crea un grafo dirigido por defecto
    n = int(input("Ingrese el número de nodos: "))
    
    for i in range(n):
        nodo = input(f"Ingrese el nombre del nodo {i + 1}: ")
        G.add_node(nodo)
    
    m = int(input("Ingrese el número de aristas: "))
    
    for i in range(m):
        inicio = input("Ingrese el nodo de inicio de la arista: ")
        fin = input("Ingrese el nodo de fin de la arista: ")
        G.add_edge(inicio, fin)
    
    return G

# Función que determina si el grafo es dirigido
def EsDirigido(G):
    return G.is_directed()

# Función que determina si el grafo es fuertemente conexo
def EsFuertementeConexo(G):
    return nx.is_strongly_connected(G)

# Función que obtiene los grados de entrada y salida de un nodo en un grafo dirigido
def GradosEntradaSalida(G, nodo):
    if EsDirigido(G):
        grado_entrada = G.in_degree(nodo)
        grado_salida = G.out_degree(nodo)
        return grado_entrada, grado_salida
    else:
        return None, None

# Función que determina si el grafo es conexo
def EsConexo(G):
    return nx.is_connected(G)

# Función que obtiene el grado de un nodo en un grafo no dirigido
def GradoNodo(G, nodo):
    return G.degree(nodo)

# Función que obtiene el grado del grafo
def GradoGrafo(G):
    return max(dict(G.degree()).values())

# Función que determina si el grafo tiene un ciclo Hamiltoniano
def TieneCicloHamiltoniano(G):
    if not G.is_directed():
        return nx.is_hamiltonian(G)

# Función que muestra el ciclo Hamiltoniano del grafo si existe
def MostrarCicloHamiltoniano(G):
    if TieneCicloHamiltoniano(G):
        ciclo = list(nx.hamiltonian_cycle(G))
        print("Ciclo Hamiltoniano:", ciclo)
    else:
        print("El grafo no tiene un ciclo Hamiltoniano.")

# Función que muestra el menú de opciones
def MostrarMenu():
    print("1. Insertar Grafo")
    print("2. Determinar si es dirigido")
    print("3. Determinar si es fuertemente conexo y obtener grados de entrada y salida de un nodo")
    print("4. Determinar si es conexo y obtener el grado de un nodo")
    print("5. Obtener el grado del grafo")
    print("6. Determinar si el grafo tiene un ciclo de Hamilton")
    print("7. Salir")

# Función principal del programa
def main():
    grafo = None

    while True:
        MostrarMenu()
        opcion = int(input("Ingrese la opción: "))

        if opcion == 1:
            grafo = InsertarGrafo()
        elif opcion == 2:
            print("El grafo es dirigido." if EsDirigido(grafo) else "El grafo no es dirigido.")
        elif opcion == 3:
            nodo = input("Ingrese el nombre del nodo: ")
            grado_entrada, grado_salida = GradosEntradaSalida(grafo, nodo)
            print(f"Grado de entrada: {grado_entrada}, Grado de salida: {grado_salida}")
        elif opcion == 4:
            print("El grafo es conexo." if EsConexo(grafo) else "El grafo no es conexo.")
            nodo = input("Ingrese el nombre del nodo: ")
            grado_nodo = GradoNodo(grafo, nodo)
            print(f"Grado del nodo {nodo}: {grado_nodo}")
        elif opcion == 5:
            grado_grafo = GradoGrafo(grafo)
            print(f"Grado del grafo: {grado_grafo}")
        elif opcion == 6:
            MostrarCicloHamiltoniano(grafo)
        elif opcion == 7:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
