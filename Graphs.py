
#using a basic dictionary object
G = {'S':[]}

#Clase Grafo
class Directed_Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex):
       if vertex in self.graph_dict:
           return "Vertex already in graph"
       self.graph_dict[vertex] = [] 
        
    def add_edge(self, edge):
        v1 = edge.get_v1()
        v2 = edge.get_v2()
        if v1 not in self.graph_dict:
            raise ValueError(f"Vertex {v1.get_name()} not added")
        if v2 not in self.graph_dict:
            raise ValueError(f"Vertex {v2.get_name()} not added")
        self.graph_dict[v1].append(v2)

    def is_vertex_in(self, vertex):
        return vertex in self.graph_dict

    def get_vertex(self, vertex_name):
        for v in self.graph_dict:
            if vertex_name == v.get_name():
                return v
        else:
            print(f'Vertex {vertex_name} does not exist') 

    def get_neighbours(self, vertex):
        return self.graph_dict[vertex]      

    def __str__(self):
        all_edges = ''
        for v1 in self.graph_dict:
            for v2 in self.graph_dict[v1]:
                all_edges += v1.get_name() +' ---> ' + v2.get_name()          

        return all_edges        
    

class Undirected_Graph(Directed_Graph):
    def add_edge(self, edge):
        Directed_Graph.add_edge(self, edge)
        edge_back = Edge(edge.get_v2(), edge.get_v1())
        Directed_Graph.add_edge(self, edge_back)




#En esta clase se define el grafo como un diccionario de listas de adyacencia 
#y se definen los métodos para agregar vértices y aristas

class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def get_v1(self):
        return self.v1
    def get_v2(self):
        return self.v2    
    def __str__(self):
        return self.v1.get_name() + ' -> ' + self.v2.get_name()
    
#En esta clase se define el vértice como un objeto con un nombre
#y se define el método para obtener el nombre del vértice

class Vertex:


    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name

    def __str__(self):
        return self.name        
    
# Resto del código sin cambios...

def build_graph(graph_class):
    g = graph_class()
    for i in 'sabcdefghix':
        g.add_vertex(Vertex(i))
    g.add_edge(Edge(g.get_vertex('s'), g.get_vertex('a')))
    g.add_edge(Edge(g.get_vertex('s'), g.get_vertex('b')))
    return g

G1 = build_graph(Directed_Graph)

print(G1)
