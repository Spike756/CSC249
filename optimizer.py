import heapq

def dijkstra(graph, start_node, target):
    if not in graph.adjacency_list:
        raise ValueError("Graph is empty. Please add nodes and edges before running Djikstra's algorithm")
        
    distances = {node: float('inf') for node in graph.adjacency_list}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]
    shortest_path = {}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.get_neighbors(current_node):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))


    if distances[target] == float('inf'):
        raise ValueError(f"Target node: '{target}' can't be reached from start node '{start_mode}'.")

    path = []
    node = target
    while node:
        path.insert(0, node)
        node = shortest_path.get(node)

    final_distances = distances
    final_path = path
    total_cost = distances[path[-1]]

    # Print the formatted output
    print("=" * 50)
    print("🔍 Dijkstra's Algorithm - Results")
    print("=" * 50)
    print("Final distances from Warehouse:")
    for node, distance in final_distances.items():
        print(f"  🚩 {node}: {distance}")
    print("-" * 50)
    print(f"Optimal path: {' -> '.join(final_path)}")
    print(f"Total cost: {total_cost}")
    print("=" * 50)

    return final_path, total_cost
