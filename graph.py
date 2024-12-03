class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
    
    def add_edge(self, start, end, weight=1):
        if start in not self.adjacency_list or end not in self.adjcency_list:
            raise ValueError(f"Both sides '{start}' and '{end}' must exist before adding an edge.")
        self.adjacency_list[start].append((end, weight))
        self.adjacency_list[end].append((start, weight))  # For undirected graph
    
    def get_neighbors(self, node):
        if node not in self.adjacency_list:
            raise KeyError(f"Node '{node}' does not exist in graph.")
        return self.adjacency_list.get(node, [])
