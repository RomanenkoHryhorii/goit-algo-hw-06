import networkx as nx
import matplotlib.pyplot as plt

class MyceliumGraphSearch:
    def __init__(self, graph):
        self.graph = graph

    def depth_first_search(self, start_node, target_node):
        """
        Пошук у глибину (DFS)
        """
        visited = set()
        path = []

        def dfs_recursive(current_node):
            visited.add(current_node)
            path.append(current_node)

            if current_node == target_node:
                return True

            for neighbor in self.graph.neighbors(current_node):
                if neighbor not in visited:
                    if dfs_recursive(neighbor):
                        return True

            path.pop()
            return False

        dfs_recursive(start_node)
        return path if path[-1] == target_node else None

    def breadth_first_search(self, start_node, target_node):
        """
        Пошук у ширину (BFS)
        """
        visited = set()
        queue = [[start_node]]

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node not in visited:
                visited.add(node)

                if node == target_node:
                    return path

                for neighbor in self.graph.neighbors(node):
                    if neighbor not in visited:
                        new_path = list(path)
                        new_path.append(neighbor)
                        queue.append(new_path)

        return None

    def visualize_paths(self, dfs_path, bfs_path):
        """
        Візуалізація знайдених шляхів
        """
        plt.figure(figsize=(15, 6))

        # DFS Path
        plt.subplot(121)
        pos = nx.spring_layout(self.graph, seed=42)
        nx.draw_networkx_nodes(self.graph, pos, node_color='lightblue')
        nx.draw_networkx_edges(self.graph, pos, alpha=0.2)
        
        path_edges_dfs = list(zip(dfs_path, dfs_path[1:]))
        nx.draw_networkx_nodes(self.graph, pos, nodelist=dfs_path, node_color='red')
        nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges_dfs, edge_color='r', width=2)
        plt.title('DFS Шлях')
        plt.axis('off')

        # BFS Path
        plt.subplot(122)
        nx.draw_networkx_nodes(self.graph, pos, node_color='lightblue')
        nx.draw_networkx_edges(self.graph, pos, alpha=0.2)
        
        path_edges_bfs = list(zip(bfs_path, bfs_path[1:]))
        nx.draw_networkx_nodes(self.graph, pos, nodelist=bfs_path, node_color='green')
        nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges_bfs, edge_color='g', width=2)
        plt.title('BFS Шлях')
        plt.axis('off')

        plt.tight_layout()
        plt.show()

# Використання класу
np.random.seed(42)
mycelium_network = create_mycelium_network(num_nodes=200, connection_probability=0.03)

# Вибираємо випадкові стартову та цільову вершини
all_nodes = list(mycelium_network.nodes())
start_node = all_nodes[0]
target_node = all_nodes[-1]

graph_search = MyceliumGraphSearch(mycelium_network)

# Пошук шляхів
dfs_path = graph_search.depth_first_search(start_node, target_node)
bfs_path = graph_search.breadth_first_search(start_node, target_node)

print("DFS шлях:", dfs_path)
print("BFS шлях:", bfs_path)

graph_search.visualize_paths(dfs_path, bfs_path)