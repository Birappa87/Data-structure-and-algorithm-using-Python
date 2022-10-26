class Graph:
    def __init__(self):
        self.adj_list = {}
    
    #adding vertex to adjcency list
    def add_vertex(self, v):
        if v not in self.adj_list.keys():
            self.adj_list[v] = set()
            return True
        return False
    
    #adding edges
    def add_edges(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].add(v2)
            self.adj_list[v2].add(v1)
            return True
        return False
    
    #display adjcency list
    def display(self):
        for v in self.adj_list.keys():
            vertex = v
            con_edges = self.adj_list[v]
            print(f"{vertex} : {con_edges}")

G = Graph()
G.add_vertex('A')
G.add_vertex('B')
G.add_vertex('C')
G.add_vertex('D')

#adding edges
G.add_edges('A','B')
G.add_edges('A','C')
G.add_edges('A','D')
G.add_edges('B','D')
G.add_edges('C','A')

G.display()
