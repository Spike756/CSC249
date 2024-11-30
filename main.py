from graph import Graph
from optimizer import dijkstra

# Initialize the delivery graph
delivery_graph = Graph()

# Add nodes and edges
delivery_graph.add_node("Warehouse")
delivery_graph.add_node("Customer1")
delivery_graph.add_node("Customer2")
delivery_graph.add_node("Customer3")
delivery_graph.add_node("Customer4")

delivery_graph.add_edge("Warehouse", "Customer1", weight=5)
delivery_graph.add_edge("Warehouse", "Customer2", weight=8)
delivery_graph.add_edge("Customer1", "Customer3", weight=4)
delivery_graph.add_edge("Customer2", "Customer3", weight=3)
delivery_graph.add_edge("Customer3", "Customer4", weight=2)
delivery_graph.add_edge("Customer4", "Warehouse", weight=10)

# Find the optimal route
route, cost = dijkstra(delivery_graph, "Warehouse", "Customer4")
print(f"Optimal route: {route}, Cost: {cost}")
