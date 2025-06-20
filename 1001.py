import itertools

# Mendefinisikan waktu antar node dalam menit
weights = {
    (1, 2): 7, (1, 3): 14, (1, 4): 12, (1, 5): 8,
    (2, 3): 9, (2, 4): 8, (2, 5): 10,
    (3, 4): 10, (3, 5): 12,
    (4, 5): 11
}

# Fungsi untuk memastikan waktu simetris
def get_distance(a, b):
    return weights.get((a, b)) or weights.get((b, a))

# Daftar node yang akan dikunjungi
nodes = [2, 3, 4, 5]

# Inisialisasi variabel untuk rute terpendek dan terpanjang
shortest_route = None
shortest_distance = float('inf')
longest_route = None
longest_distance = float('-inf')

# Menghitung semua permutasi dari node yang akan dikunjungi
for route in itertools.permutations(nodes):
    # Menghitung total waktu untuk rute ini
    total_distance = get_distance(1, route[0])  # Waktu dari node 1 ke node pertama
    for i in range(len(route) - 1):
        total_distance += get_distance(route[i], route[i + 1])  # Waktu antar node
    total_distance += get_distance(route[-1], 1)  # Waktu dari node terakhir kembali ke node 1

    # Memperbarui rute terpendek jika waktu lebih kecil
    if total_distance < shortest_distance:
        shortest_distance = total_distance
        shortest_route = (1,) + route + (1,)

    # Memperbarui rute terpanjang jika waktu lebih besar
    if total_distance > longest_distance:
        longest_distance = total_distance
        longest_route = (1,) + route + (1,)

# Menampilkan hasil
print("Rute Terpendek:", shortest_route, "Waktu:", shortest_distance, "menit")
print("Rute Terpanjang:", longest_route, "Waktu:", longest_distance, "menit")
