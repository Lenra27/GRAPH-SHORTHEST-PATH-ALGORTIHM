"""
NAMA  : Pratama Rizky Aditya
KELAS : 2IA26
NPM   : 51422299 
"""
import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        
    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []
        
    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))

    def dijkstra(self, start):
        
        distances = {node: float('infinity') for node in self.nodes}
        
        
        distances[start] = 0
        
        
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            
            if current_distance > distances[current_node]:
                continue
            
            
            for neighbor, weight in self.edges[current_node]:
                distance = current_distance + weight
                
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances


g = Graph()


for node in ['P', 'R', 'A', 'T', 'A', 'M', 'A']:
    g.add_node(node)


g.add_edge('P', 'R', 1)
g.add_edge('R', 'A', 2)
g.add_edge('P', 'A', 4)
g.add_edge('R', 'T', 5)
g.add_edge('A', 'T', 1)
g.add_edge('T', 'M', 7)
g.add_edge('A', 'M', 3)


start_node = 'P'
shortest_distances = g.dijkstra(start_node)


print(f"Shortest distances from node {start_node}:")
for node, distance in shortest_distances.items():
    print(f"To node {node}: {distance}")
