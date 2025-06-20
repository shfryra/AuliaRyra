harga_ayam = {
    "D": 2500,  
    "P": 2000,  
    "S": 1500   
}

banyak_jenis = int(input("Masukkan jumlah jenis potongan yang dibeli: "))

total_harga = 0
jenis_terbeli = []

for i in range(banyak_jenis):
    print(f"\nJenis Ke-{i + 1}")
    kode = input("Kode Potong (D/P/S): ")
    if kode in harga_ayam:
        jumlah = int(input("Banyak Potong: "))
        harga_satuan = harga_ayam[kode]
        subtotal = harga_satuan * jumlah
        total_harga += subtotal
        jenis_terbeli.append((kode, harga_satuan, jumlah, subtotal))
    else:
        print("Kode potong tidak valid.")

print("\nGEROBAK FRIED CHICKEN")
print("----------------------")
print("No. | Jenis | Harga Satuan | Banyak Beli | Jumlah Harga")
print("-------------------------------------------------------")
for i, (kode, harga_satuan, jumlah, subtotal) in enumerate(jenis_terbeli, start=1):
    print(f"{i}.  | {kode}    | Rp {harga_satuan}        | {jumlah}         | Rp {subtotal}")
print("-------------------------------------------------------")

if banyak_jenis > 2:
    diskon = total_harga * 0.05  
    total_harga -= diskon
else:
    diskon = 0

pajak = total_harga * 0.1
total_bayar = total_harga + pajak

print("Diskon 5%:           Rp", diskon)
print("Jumlah Bayar:        Rp", total_harga)
print("Pajak 10%:           Rp", pajak)
print("Total Bayar:         Rp", total_bayar)

uang_bayar = int(input("\nMasukkan uang pembayaran: Rp "))

if uang_bayar > total_bayar:
    kembalian = uang_bayar - total_bayar
    print("Uang kembalian Anda: Rp", kembalian)
elif uang_bayar == total_bayar:
    print("Terima kasih. Pembayaran Anda pas.")
else:
    kekurangan = total_bayar - uang_bayar
    print("Mohon maaf, uang Anda kurang sebesar: Rp", kekurangan)

print("Terimakasih sudah berbelanja di toko kami")