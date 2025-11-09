import matplotlib.pyplot as plt
import networkx as nx
class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = []

    def add_edge(self, from_node, to_node):
        if from_node in self.nodes and to_node in self.nodes:
            self.nodes[from_node].append(to_node)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph.nodes[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
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
def visualize_graph_matplotlib(graph):
    G = nx.DiGraph()

    # Добавляем узлы и рёбра
    for node, neighbors in graph.nodes.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Рисуем граф
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            node_size=2000, arrows=True, arrowsize=20,
            font_size=16, font_weight='bold', edge_color='gray')
    plt.title("Визуализация графа", fontsize=16)
    plt.show()

graph = Graph()
for node in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
    graph.add_node(node)
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

visualize_graph_matplotlib(graph)