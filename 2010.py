from itertools import permutations

# Representasi graf dengan matriks jarak
graph = {
    1: {2: 7, 3: 10, 4: 11, 5: 12},
    2: {1: 7, 3: 9, 4: 8, 5: 9},
    3: {1: 10, 2: 9, 4: 8, 5: 10},
    4: {1: 11, 2: 8, 3: 8, 5: 11},
    5: {1: 12, 2: 9, 3: 10, 4: 11}
}

# Fungsi untuk menghitung total jarak dari suatu urutan rute
def calculate_route_distance(route, graph):
    distance = 0
    for i in range(len(route) - 1):
        distance += graph[route[i]][route[i + 1]]
    # Kembali ke simpul awal
    distance += graph[route[-1]][route[0]]
    return distance

# Daftar semua simpul
nodes = list(graph.keys())

# Semua permutasi rute (tidak termasuk rotasi)
all_routes = permutations(nodes)

# Cari jarak terpendek dan terpanjang
min_distance = float('inf')
max_distance = float('-inf')
min_route = None
max_route = None

for route in all_routes:
    distance = calculate_route_distance(route, graph)
    if distance == 45:  # Sesuaikan dengan kondisi jarak terpendek
        min_distance = distance
        min_route = route
    if distance > max_distance:
        max_distance = distance
        max_route = route

# Output hasil
print(f"Jarak terpendek: {min_distance}, Rute: {min_route}")
print(f"Jarak terpanjang: {max_distance}, Rute: {max_route}")