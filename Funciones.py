

def EsDirigido(G):
    # Verificar si hay aristas inversas para cada arista en el grafo
    for edge in G.edges():
        reverse_edge = (edge[1], edge[0])
        if reverse_edge not in G.edges():
            return False
    
    # Si no se encontraron aristas inversas, el grafo es dirigido
    return True

def EsFuertementeConexo(G):
    # Verificar la fuerte conectividad usando DFS desde cada nodo
    for nodo in G.nodes():
        if not EsAlcanzableDesdeTodos(G, nodo):
            return False
    
    # Si todos los nodos son alcanzables desde todos los demás, el grafo es fuertemente conexo
    return True

def EsAlcanzableDesdeTodos(G, origen):
    # Realizar una búsqueda en profundidad (DFS) desde el nodo de origen
    visitados = set()
    pila = [origen]

    while pila:
        nodo_actual = pila.pop()

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            # Agregar todos los sucesores (nodos vecinos) a la pila
            pila.extend(sucesor for sucesor in G.successors(nodo_actual) if sucesor not in visitados)

    # Verificar si todos los nodos fueron visitados
    return len(visitados) == G.number_of_nodes()

# Función que obtiene los grados de entrada y salida de un nodo en un grafo dirigido
def GradosEntradaSalida(G, nodo):
    if EsDirigido(G):  # Verifica si el grafo es dirigido
        grado_entrada = G.in_degree(nodo)  # Obtiene el grado de entrada del nodo
        grado_salida = G.out_degree(nodo)  # Obtiene el grado de salida del nodo
        return grado_entrada, grado_salida
    else:
        return None, None  # Si el grafo no es dirigido, devuelve None para ambos grados
    

def EsConexo(G):
    # Verificar la conectividad utilizando DFS desde cualquier nodo
    nodos_visitados = set()

    # Función de búsqueda en profundidad recursiva
    def DFS(nodo):
        nodos_visitados.add(nodo)
        for vecino in G[nodo]:
            if vecino not in nodos_visitados:
                DFS(vecino)

    # Seleccionar un nodo inicial
    primer_nodo = next(iter(G.nodes()), None)

    if primer_nodo is not None:
        DFS(primer_nodo)

    # Verificar si todos los nodos fueron visitados
    return len(nodos_visitados) == G.number_of_nodes()

def GradoNodo(G, nodo):
    if nodo in G:
        return len(G[nodo])  # La longitud de la lista de vecinos representa el grado
    else:
        return None  # El nodo no está presente en el grafo
    
def GradoGrafo(G):
    if G:
        grados = [len(G[nodo]) for nodo in G]
        return max(grados) if grados else 0
    else:
        return None

# Función que muestra el ciclo Hamiltoniano del grafo si existe
def MostrarCicloHamiltoniano(G):
    if TieneCicloHamiltoniano(G):
        ciclo = EncontrarCicloHamiltoniano(G)
        print("Ciclo Hamiltoniano:", ciclo)
    else:
        print("El grafo no tiene un ciclo Hamiltoniano.")

# Función para encontrar un ciclo Hamiltoniano en el grafo
def EncontrarCicloHamiltoniano(G):
    def dfs(nodo, visitados, ruta):
        visitados.add(nodo)
        ruta.append(nodo)

        if len(visitados) == len(G) and ruta[0] in G[nodo]:
            return ruta

        for vecino in G[nodo]:
            if vecino not in visitados:
                ciclo = dfs(vecino, visitados.copy(), ruta.copy())
                if ciclo:
                    return ciclo

        return None

    for nodo in G:
        ciclo = dfs(nodo, set(), [])
        if ciclo:
            return ciclo

    return None



