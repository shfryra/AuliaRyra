#Daftar harga per jenis potong
harga_ayam = {
    'D': 2500,  # Dada
    'P': 2000,  # Paha
    'S': 1500   # Sayap
}

#Fungsi untuk menghitung total pembayaran
def hitung_total_pembayaran(Jenis_potong,banyak_potong):
    total=0
    for jenis,banyak in zip(Jenis_potong,banyak_potong):
        