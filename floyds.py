# Number of vertices in the graph
nV = 4
# A large number representing infinity
INF = 999

# The Floyd-Warshall algorithm is used to find the shortest paths
# between all pairs of vertices in a weighted graph.
def floyd(G):
    # Create a distance matrix initialized as the input graph
    dist = [list(row) for row in G]

    # Adding vertices individually
    for r in range(nV):
        # Update the distance matrix to include the vertex as an intermediate vertex
        for p in range(nV):
            for q in range(nV):
                # Update the shortest path if a shorter path is found
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
    # Call the function to print the solution
    sol(dist)

# Function to print the output
def sol(dist):
    for p in range(nV):
        for q in range(nV):
            # Print 'INF' if no path is found
            if(dist[p][q] == INF):
                print("INF", end=" ")
            else:
                # Otherwise, print the shortest path distance
                print(dist[p][q], end="  ")
        print(" ")

# Graph represented as an adjacency matrix
G = [[0, 5, INF, INF],
     [50, 0, 15, 5],
     [30, INF, 0, 15],
     [15, INF, 5, 0]]

# Call the Floyd-Warshall algorithm function with the graph
floyd(G)
