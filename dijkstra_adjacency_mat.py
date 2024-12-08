import heapq


def dijkstra_adj_matrix(graph, start):
    # Graph is represented as an adjacency matrix
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n
    priority_queue = [(0, start)]  # (distance, node)


    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)
        if visited[current_node]:
            continue
        visited[current_node] = True


        for neighbor in range(n):
            weight = graph[current_node][neighbor]
            if weight != 0 and not visited[neighbor] and current_dist + weight < dist[neighbor]:
                dist[neighbor] = current_dist + weight
                heapq.heappush(priority_queue, (dist[neighbor], neighbor))
    
    return dist

# Adjacency matrix representation
graph_adj_matrix = [
    [0, 1, 4, 0],  # Edges from vertex 0
    [0, 0, 2, 6],  # Edges from vertex 1
    [0, 0, 0, 3],  # Edges from vertex 2
    [0, 0, 0, 0]   # Edges from vertex 3
]

# Run Dijkstra's algorithm
start_node = 0
print("Adjacency Matrix Result:", dijkstra_adj_matrix(graph_adj_matrix, start_node))