# Set a large value as infinity to represent "infinity" distance between vertices
INF = 9999999

# Number of vertices in the graph
V = 5

# Create a 2D array to represent the graph's adjacency matrix
G = [
    [0, 9, 75, 0, 0],
    [9, 0, 95, 19, 42],
    [75, 95, 0, 51, 66],
    [0, 19, 51, 0, 31],
    [0, 42, 66, 31, 0]
]

# Array to track selected vertices (0 means not selected, 1 means selected)
selected = [0, 0, 0, 0, 0]

# Counter for the number of edges in the minimum spanning tree
no_edge = 0

# Choose the 0th vertex and mark it as selected
selected[0] = True

# Print for edge and weight
print("Edge : Weight\n")

# Main loop to find the minimum spanning tree
while (no_edge < V - 1):
    # For every vertex in the set S, find all adjacent vertices and calculate the distance from the vertex selected at step 1.
    # If the vertex is already in the set S, discard it; otherwise, choose another vertex nearest to the selected vertex at step 1.
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):
                    # Not in selected and there is an edge
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    # Print the selected edge and its weight
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    # Mark the selected vertex as visited
    selected[y] = True
    # Increment the number of edges
    no_edge += 1
