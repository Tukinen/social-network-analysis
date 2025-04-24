import networkx as nx
import matplotlib.pyplot as plt

# Параметрүүд
n = 300  # Зангилааны тоо
m = 3    # Шинээр орж ирэх зангилааны холбогдох холбоосын тоо
p = 0.3  # Гурвалжин үүсгэх магадлал

# Holme-Kim граф үүсгэх
hk_graph = nx.powerlaw_cluster_graph(n, m, p)

# Граф зурах
plt.figure(figsize=(8, 6))
nx.draw(hk_graph, node_size=30, edge_color='gray', alpha=0.6, with_labels=False)
plt.title("Holme-Kim Powerlaw Cluster Graph")
plt.show()
