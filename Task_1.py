import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

def create_mycelium_network(num_nodes=100, connection_probability=0.05):
    """
    Створення графу мережі міцелію грибів
    
    Parameters:
    - num_nodes: кількість вузлів у мережі
    - connection_probability: ймовірність з'єднання між вузлами
    
    Returns:
    NetworkX Graph
    """
    # Створення графу
    G = nx.erdos_renyi_graph(num_nodes, connection_probability)
    
    # Додавання атрибутів вузлам (наприклад, тип клітини, вік)
    for node in G.nodes():
        G.nodes[node]['cell_type'] = random.choice(['hypha', 'spore', 'mycelial_tip'])
        G.nodes[node]['age'] = random.randint(1, 100)
    
    return G

def analyze_mycelium_network(G):
    """
    Аналіз характеристик мережі міцелію
    
    Parameters:
    - G: NetworkX Graph
    """
    print("Базові характеристики мережі:")
    print(f"Кількість вершин: {G.number_of_nodes()}")
    print(f"Кількість ребер: {G.number_of_edges()}")
    
    # Аналіз ступеня вершин
    degrees = dict(G.degree())
    print("\nАналіз ступеня вершин:")
    print(f"Середній ступінь: {np.mean(list(degrees.values())):.2f}")
    print(f"Максимальний ступінь: {max(degrees.values())}")
    print(f"Мінімальний ступінь: {min(degrees.values())}")
    
    # Розподіл типів клітин
    cell_types = nx.get_node_attributes(G, 'cell_type')
    type_distribution = {}
    for cell_type in set(cell_types.values()):
        type_distribution[cell_type] = list(cell_types.values()).count(cell_type)
    
    print("\nРозподіл типів клітин:")
    for cell_type, count in type_distribution.items():
        print(f"{cell_type}: {count}")

def visualize_mycelium_network(G):
    """
    Візуалізація графу мережі міцелію
    
    Parameters:
    - G: NetworkX Graph
    """
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, k=0.5)  # позиціонування вузлів
    
    # Колірне кодування типів клітин
    color_map = {
        'hypha': 'lightblue', 
        'spore': 'green', 
        'mycelial_tip': 'red'
    }
    
    node_colors = [color_map[G.nodes[node]['cell_type']] for node in G.nodes()]
    node_sizes = [50 + G.degree(node) * 10 for node in G.nodes()]
    
    nx.draw_networkx_nodes(G, pos, 
                            node_color=node_colors, 
                            node_size=node_sizes, 
                            alpha=0.7)
    nx.draw_networkx_edges(G, pos, alpha=0.2)
    
    plt.title("Мережа міцелію грибів")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# Основний робочий процес
np.random.seed(42)
mycelium_network = create_mycelium_network(num_nodes=200, connection_probability=0.03)
analyze_mycelium_network(mycelium_network)
visualize_mycelium_network(mycelium_network)