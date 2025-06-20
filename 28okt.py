def hitung_harga(jenis_potong, banyak_beli):
    harga_per_jenis = {
        'D': 2500,  # Dada
        'P': 2000,  # Paha
        'S': 1500   # Sayap
    }
    
    if jenis_potong in harga_per_jenis:
        return harga_per_jenis[jenis_potong] * banyak_beli
    else:
        return 0

def main():
    print("Selamat datang di GEROBAK FRIED CHICKEN")
    
    total_harga = 0
    while True:
        jenis_potong = input("Masukkan jenis potong (D untuk Dada, P untuk Paha, S untuk Sayap) atau 'X' untuk selesai: ").upper()
        
        if jenis_potong == 'X':
            break
        
        if jenis_potong not in ['D', 'P', 'S']:
            print("Jenis potong tidak valid. Silakan coba lagi.")
            continue
        
        try:
            banyak_beli = int(input(f"Masukkan banyak beli untuk jenis potong {jenis_potong}: "))
            if banyak_beli < 1:
                print("Jumlah beli harus lebih dari 0. Silakan coba lagi.")
                continue
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
            continue
        
        harga = hitung_harga(jenis_potong, banyak_beli)
        total_harga += harga
        print(f"Harga untuk {banyak_beli} potong {jenis_potong}: Rp {harga}")
    
    pajak = total_harga * 0.10
    total_bayar = total_harga + pajak
    
    print(f"\nTotal harga sebelum pajak: Rp {total_harga}")
    print(f"Pajak 10%: Rp {pajak}")
    print(f"Total yang harus dibayar: Rp {total_bayar}")

if __name__ == "__main__":
    main()