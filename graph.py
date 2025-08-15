from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Для ненаправленного графа
    
    def bfs(self, start):
        visited = set()
        queue = []
        visited.add(start)
        queue.append(start)
        
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

# Тест
g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("A", "D")

# print("BFS начиная с A:", end=" ")
# g.bfs("A")  # Вывод: A B C D
g.print_graph()