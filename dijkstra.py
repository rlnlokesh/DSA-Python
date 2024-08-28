def dijkstra(graph, source):
    # Initialize distances to all vertices as infinity
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0

    # Set of vertices whose shortest distance from the source is already found
    visited = set()

    while len(visited) < len(graph):
        # Find the vertex with the minimum distance from the source among unvisited vertices
        min_distance = float('infinity')
        min_vertex = None
        for vertex in graph:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex

        # Mark the selected vertex as visited
        visited.add(min_vertex)

        # Update distances to neighbors of the selected vertex
        for neighbor, weight in graph[min_vertex].items():
            distance = min_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances

# Example usage:
graph = {
    'A': {'B': 3, 'C': 4},
    'B': {'A': 3, 'C': 1, 'D': 7},
    'C': {'A': 4, 'B': 1, 'D': 2},
    'D': {'B': 7, 'C': 2}
}
source_vertex = 'A'
shortest_distances = dijkstra(graph, source_vertex)
print("Shortest distances from source vertex", source_vertex, ":")
for vertex, distance in shortest_distances.items():
    print("Vertex:", vertex, "Distance:", distance)
