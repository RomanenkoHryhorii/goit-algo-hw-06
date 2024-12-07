import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

def create_weighted_mycelium_network(num_nodes=100, connection_probability=0.05):
    """
    Створення зваженого графу мережі міцелію
    """
    # Створення графу
    G = nx.erdos_renyi_graph(num_nodes, connection_probability)
    
    # Додавання ваг до ребер
    for (u, v) in G.edges():
        # Генерація реалістичних ваг для біологічної мережі
        weight = np.random.uniform(0.1, 5.0)  # Вага від 0.1 до 5.0
        G.edges[u, v]['weight'] = weight
    
    # Додавання атрибутів вузлам
    for node in G.nodes():
        G.nodes[node]['cell_type'] = random.choice(['hypha', 'spore', 'mycelial_tip'])
        G.nodes[node]['age'] = random.randint(1, 100)
    
    return G

class MyceliumNetworkPathfinder:
    def __init__(self, graph):
        self.graph = graph
    
    def dijkstra_shortest_paths(self):
        """
        Знаходження найкоротших шляхів між всіма парами вершин за алгоритмом Дейкстри
        """
        # Збереження найкоротших шляхів
        shortest_paths = {}
        
        # Знаходження найкоротшого шляху між всіма парами вузлів
        for source in self.graph.nodes():
            shortest_paths[source] = {}
            for target in self.graph.nodes():
                if source != target:
                    try:
                        path = nx.dijkstra_path(self.graph, source, target, weight='weight')
                        path_length = nx.dijkstra_path_length(self.graph, source, target, weight='weight')
                        shortest_paths[source][target] = {
                            'path': path,
                            'length': path_length
                        }
                    except nx.NetworkXNoPath:
                        shortest_paths[source][target] = None
        
        return shortest_paths
    
    def visualize_shortest_paths(self, shortest_paths):
        """
        Візуалізація найкоротших шляхів
        """
        plt.figure(figsize=(15, 10))
        pos = nx.spring_layout(self.graph, k=0.5, seed=42)
        
        # Основний граф
        nx.draw_networkx_nodes(self.graph, pos, node_color='lightblue', node_size=50)
        nx.draw_networkx_edges(self.graph, pos, alpha=0.1, width=0.5)
        
        # Знаходження 3 найкоротших шляхів для демонстрації
        all_paths = []
        for source in shortest_paths:
            for target, path_info in shortest_paths[source].items():
                if path_info and len(path_info['path']) > 1:
                    all_paths.append((path_info['path'], path_info['length']))
        
        # Сортування шляхів за довжиною
        all_paths.sort(key=lambda x: x[1])
        
        # Відображення 3 найкоротших шляхів
        colors = ['red', 'green', 'blue']
        for i, (path, length) in enumerate(all_paths[:3]):
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_nodes(self.graph, pos, nodelist=path, 
                                   node_color=colors[i], 
                                   node_size=100, 
                                   alpha=0.7)
            nx.draw_networkx_edges(self.graph, pos, 
                                   edgelist=path_edges, 
                                   edge_color=colors[i], 
                                   width=2,
                                   alpha=0.7)
            plt.title(f"Найкоротші шляхи (3 приклади)")
        
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def analyze_path_statistics(self, shortest_paths):
        """
        Аналіз статистики найкоротших шляхів
        """
        # Збір статистики
        path_lengths = []
        for source in shortest_paths:
            for target, path_info in shortest_paths[source].items():
                if path_info:
                    path_lengths.append(path_info['length'])
        
        print("\nСтатистика найкоротших шляхів:")
        print(f"Загальна кількість шляхів: {len(path_lengths)}")
        print(f"Середня довжина шляху: {np.mean(path_lengths):.2f}")
        print(f"Мінімальна довжина шляху: {np.min(path_lengths):.2f}")
        print(f"Максимальна довжина шляху: {np.max(path_lengths):.2f}")
        print(f"Стандартне відхилення довжини шляху: {np.std(path_lengths):.2f}")

# Основний робочий процес
np.random.seed(42)
weighted_mycelium_network = create_weighted_mycelium_network(num_nodes=200, connection_probability=0.03)

# Створення та аналіз графу
pathfinder = MyceliumNetworkPathfinder(weighted_mycelium_network)

# Знаходження найкоротших шляхів
shortest_paths = pathfinder.dijkstra_shortest_paths()

# Візуалізація шляхів
pathfinder.visualize_shortest_paths(shortest_paths)

# Аналіз статистики шляхів
pathfinder.analyze_path_statistics(shortest_paths)

# Приклад виведення найкоротшого шляху між двома конкретними вузлами
start_node = list(weighted_mycelium_network.nodes())[0]
end_node = list(weighted_mycelium_network.nodes())[-1]

if shortest_paths[start_node][end_node]:
    print("\nНайкоротший шлях між вузлами:")
    print(f"Шлях: {shortest_paths[start_node][end_node]['path']}")