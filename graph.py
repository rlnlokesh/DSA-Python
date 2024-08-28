class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict={}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dict: ",self.graph_dict)

    def get_paths(self,start,end,path=[]):
        path = path + [start]
        if start ==  end:
            return [path]
        if start not in self.graph_dict:
            return []
        path = []



if __name__ == "__main__":
    routes = [
        ("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Paris","Dubai"),
        ("Paris","New York"),
        ("Dubai","New York"),
        ("New York","Tornoto"),
    ]

    route_graph = Graph(routes)

    start = "Tornoto"
    end = "Mumbai"

    print(f"paths between {start} and {end}: ",route_graph.get_paths(start,end))