# Class to represent the Union-Find data structure
class UnionFind:
    # Constructor to initialize the class variables
    def __init__(self, n):
        # Every node is initially its own parent
        self.parent = [i for i in range(n)]

    # Function to find the root of the set in which element 'a' is present
    def find(self, a):
        # Path compression heuristic
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    # Function to perform the union of two sets in which elements 'a' and 'b' are present
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        # Make one root the parent of the other
        self.parent[root_a] = root_b

# Function to perform Kruskal's algorithm on a given graph
def kruskal(edges, n):
    # Sort the edges based on their weight
    edges.sort()
    # Initialize UnionFind
    uf = UnionFind(n)
    # Variable to store the minimum cost of the spanning tree
    min_cost = 0
    # Iterate through all sorted edges
    for cost, a, b in edges:
        # Check if the current edge forms a cycle
        if uf.find(a) != uf.find(b):
            # If not, include it in the spanning tree
            min_cost += cost
            # Perform the union of the two sets
            uf.union(a, b)
    # Return the total cost of the minimum spanning tree
    return min_cost

# Main function to test the Kruskal's algorithm
if __name__ == "__main__":
    # Number of nodes in the graph
    nodes = 4
    # Number of edges in the graph
    edges = 5
    # Graph represented as a list of tuples (cost, node1, node2)
    graph = [
        (10, 0, 1),
        (18, 1, 2),
        (13, 2, 3),
        (21, 0, 2),
        (22, 1, 3)
    ]
    # Call Kruskal's algorithm and get the minimum cost
    min_cost = kruskal(graph, nodes)
    # Print the minimum cost of the spanning tree
    print("Minimum cost is:", min_cost)
