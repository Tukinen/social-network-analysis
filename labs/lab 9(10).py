import networkx as nx

# Сүлжээ үүсгэх
G = nx.DiGraph()  # Дамжуулалтын чиглэлтэй граф

# Ирмэгүүдийг нэмэх (эхлэл, зорилго, жин)
edges = [
    ('A', 'B', 5),  # Эхлэл -> Зорилго, Жин
    ('B', 'C', 3),
    ('A', 'C', 10),
    ('C', 'D', 2),
    ('B', 'D', 8)
]
G.add_weighted_edges_from(edges)

# Хамгийн богино замыг олох
shortest_paths = nx.single_source_dijkstra_path_length(G, source='A', weight='weight')
print("Хамгийн богино замууд:", shortest_paths)

# Замын хурдны хязгаарлалт, нөхцөлийг харгалзан жинг шинэчлэх
def update_edge_weights_based_on_conditions(G):
    for u, v, data in G.edges(data=True):
        # Жишээ: хурдны хязгаарлалттай тооцоо
        speed_limit = 60  # км/цаг
        distance = data['weight']  # км
        time = distance / speed_limit  # цаг
        data['weight'] = time  # Жинг хугацаагаар шинэчилнэ

update_edge_weights_based_on_conditions(G)

# Хамгийн хурдан замыг олох
fastest_paths = nx.single_source_dijkstra_path_length(G, source='A', weight='weight')
print("Хамгийн хурдан замууд:", fastest_paths)

# Хамгийн түргэн замыг олох (жишээ нь, хамгийн их жинтэй зам)
def find_fastest_paths(G):
    fastest_paths = {}
    for node in G.nodes():
        # Замын хамгийн их жинг олох
        max_weight = max((data['weight'] for _, _, data in G.edges(node, data=True)), default=0)
        fastest_paths[node] = max_weight
    return fastest_paths

fastest_paths = find_fastest_paths(G)
print("Хамгийн түргэн замууд:", fastest_paths)

# Хамгийн хурдан хамгийн богино замыг олох
# (энэ нь хамгийн хурдан замыг олоход ижилхэн, учир нь бид хугацааг хамгийн бага байлгахыг зорьж байна)
fastest_shortest_paths = fastest_paths
print("Хамгийн хурдан хамгийн богино замууд:", fastest_shortest_paths)

# Хамгийн богино хамгийн хурдан замыг олох
# (энэ нь хамгийн богино замыг олоход ижилхэн, учир нь бид жинг хамгийн бага байлгахыг зорьж байна)
shortest_fastest_paths = shortest_paths
print("Хамгийн богино хамгийн хурдан замууд:", shortest_fastest_paths)
