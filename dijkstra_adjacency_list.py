import heapq
from collections import defaultdict


def dijkstra_adj_list(graph, start):
    # Graph is represented as an adjacency list {node: [(neighbor, weight), ...]}
    n = len(graph)
    dist = {node: float('inf') for node in graph}  # Initialize distances to infinity
    dist[start] = 0
    visited = set()
    priority_queue = [(0, start)]  # (distance, node)


    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)
        if current_node in visited:
            continue
        visited.add(current_node)


        for neighbor, weight in graph[current_node]:
            if neighbor not in visited and current_dist + weight < dist[neighbor]:
                dist[neighbor] = current_dist + weight
                heapq.heappush(priority_queue, (dist[neighbor], neighbor))
    
    return dist

# Adjacency list representation
graph_adj_list = {
    0: [(1, 1), (2, 4)],
    1: [(2, 2), (3, 6)],
    2: [(3, 3)],
    3: []
}

# Run Dijkstra's algorithm
start_node = 0
print("Adjacency List Result:", dijkstra_adj_list(graph_adj_list, start_node))