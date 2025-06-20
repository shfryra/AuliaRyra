print("                 TOKO MAINAN ANAK                  ")
print("      ********************************************       ")
nama_pembeli=input("Masukkan Nama Pembeli :")
kode_mainan=input("Masukkan Kode Mainan :")
harga_mainan=int(input("Masukkan Harga Mainan : Rp. "))
jumlah_beli=int(input("Masukkan Jumlah Beli :"))

Total_Belanja=harga_mainan*jumlah_beli
print(f"Total Belanja : Rp.",Total_Belanja)

if jumlah_beli >= 10:
    diskon=(jumlah_beli*harga_mainan)*0.3
    print("Succes, anda mendapatkan diskon 30%")
else :
    jumlah_beli  <= 10
    diskon=(jumlah_beli*harga_mainan)*0.1
    print("Succes, anda mendapatkan diskon 10%")

Total=(harga_mainan*jumlah_beli)-diskon
print("Total : Rp.",Total)



print("==========================================================")
nama_pembeli=input("Nama Pembeli :")
kode_mainan=input("Kode Mainan :")
harga_mainan=int(input("Harga Mainan : Rp. "))
jumlah_beli=int(input("Jumlah Beli :"))

Total_Belanja=harga_mainan*jumlah_beli
print(f"Total Belanja: Rp.", Total_Belanja)  
if jumlah_beli >= 10:
    diskon=(jumlah_beli*harga_mainan)*0.3
    print("Succes, anda mendapatkan diskon 30%")
else :
    jumlah_beli  <= 10
    diskon=(jumlah_beli*harga_mainan)*0.1
    print("Succes, anda mendapatkan diskon 10% ")

Total=(harga_mainan*jumlah_beli)-diskon
print("Total : Rp.",Total)
