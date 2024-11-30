class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
    
    def add_edge(self, start, end, weight=1):
        self.adjacency_list[start].append((end, weight))
        self.adjacency_list[end].append((start, weight))  # For undirected graph
    
    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])
