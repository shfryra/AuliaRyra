# Harga ayam berdasarkan jenis potongan
harga_ayam = {
    'D': 2500,  # Dada
    'P': 2000,  # Paha
    'S': 1500   # Sayap
}

print("    GEROBAK FRIED CHICKEN    ")
print("------------------------------")
print("Kode | Jenis Potong | Harga")
print("------------------------------")
print("D      Dada           Rp. 2500")
print("P      Paha           Rp. 2000")
print("S      Sayap          Rp. 1500")
print("------------------------------")

# Input jumlah jenis potong yang ingin dibeli
jumlah_jenis = int(input("Masukkan jumlah jenis potong yang ingin dibeli: "))
total_harga = 0

# Loop untuk setiap jenis potong
for i in range(jumlah_jenis):
    print(f"\nJenis potong ke-{i + 1}:")
    kode_potong = input("Masukkan kode potong (D/P/S): ")
    banyak_beli = int(input("Masukkan jumlah beli: "))

    # Cek validitas kode potong
    if kode_potong in harga_ayam:
        harga_per_potong = harga_ayam[kode_potong]
        subtotal = harga_per_potong * banyak_beli

        # Terapkan diskon 5% jika banyak beli lebih dari 2
        if banyak_beli >2:
            diskon = subtotal * 0.05
            total_harga += subtotal-diskon
            print("total harga",total_harga)
            print("Selamat anda mendapatkan diskon sebesar 5%")
          

        # Tampilkan rincian pembelian
        if kode_potong == 'D':
            jenis_potong = "Dada"
        elif kode_potong == 'P':
            jenis_potong = "Paha"
        elif kode_potong == 'S':
            jenis_potong = "Sayap"
        print(f"{jenis_potong} - {banyak_beli} x Rp. {harga_per_potong} = Rp. {subtotal}")
    else:
        print("Kode potong tidak valid! Silakan coba lagi.")
        continue

# Hitung pajak dan total keseluruhan
pajak = total_harga * 0.1
total_bayar = total_harga + pajak

# Tampilkan hasil akhir
print("\nRincian Pembayaran:")
print(f"Total Harga    : Rp. {total_harga}")
print(f"Pajak (10%)    : Rp. {int(pajak)}")
print(f"Total Bayar    : Rp. {int(total_bayar)}")
print("\nTerima kasih telah berbelanja di GEROBAK FRIED CHICKEN!")
