class Graph:
    def __init__(self):
        self.nodes = {}
        self.node_data = {}
    def add_node(self, value, data):
        if value not in self.nodes:
            self.nodes[value] = []
            self.node_data[value] = data
    def add_edge(self, from_node, to_node):
        if from_node in self.nodes and to_node in self.nodes:
            self.nodes[from_node].append(to_node)
    def get_node_data(self, node):
        return self.node_data.get(node, "No data")
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph.nodes[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def find_dfs(graph, start, target_value, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(start)
    if graph.get_node_data(start) == target_value:
        return path + [start]
    for neighbor in graph.nodes[start]:
        if neighbor not in visited:
            result = find_dfs(graph, neighbor, target_value, visited, path + [start])
            if result:
                return result
    return None

def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in graph.nodes[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
def find_bfs(graph, start, target_value):
    queue = [(start, [start])]
    visited = set()
    while queue:
        (node, path) = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        current_data = graph.get_node_data(node)
        if current_data == target_value:
            return path
        for neighbor in graph.nodes[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None

graph = Graph()
graph.add_node("A", 5)
graph.add_node("B", 6)
graph.add_node("C", 8)
graph.add_node("D", 15)
graph.add_node("E", 19)
graph.add_node("F", 23)
graph.add_node("G", 40)
graph.add_node("H", 1)
graph.add_node("I", 11)
graph.add_node("J", 35)

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("F", "E")
graph.add_edge("C", "F")
graph.add_edge("H", "F")
graph.add_edge("J", "A")
graph.add_edge("J", "H")
graph.add_edge("J", "C")
graph.add_edge("E", "H")
graph.add_edge("H", "J")
graph.add_edge("I", "G")
graph.add_edge("I", "A")
graph.add_edge("G", "E")
graph.add_edge("J", "I")

print("DFS:")
dfs(graph, "A")
print("\nBFS:")
bfs(graph, "A")

print(find_bfs(graph, "A", 15))
print(find_dfs(graph, "A", 11))