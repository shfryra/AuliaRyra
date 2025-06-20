print("=================TARIF WARNET=================")
Nama_Pelanggan=input("Masukkan Nama Pelanggan :")
Waktu_Sewa=int(input("Masukkan Waktu Sewa :"))

if Waktu_Sewa <= 3 :
    Harga=6000*Waktu_Sewa
    print("Harga : Rp.", Harga)
elif Waktu_Sewa >= 3 :
    Harga=5000*Waktu_Sewa
    print("Harga : Rp.", Harga)
else :
    print("Harga 1000 Rupiah")

print()


