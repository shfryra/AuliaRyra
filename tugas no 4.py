print("================GAJI SALESMAN================")
gaji_pokok=int(input("Masukkan Gaji Pokok : Rp."))
banyak_produk=int(input("Masukkan Banyak Produk Terjual:"))
harga_satuan=int(input("Masukkan Harga Satuan : Rp."))
omset=banyak_produk*harga_satuan
print("Omset : Rp.", omset)

if banyak_produk >=100 :
    Bonus=0.2*(omset)
    print("Bonus :",Bonus)

else :
    banyak_produk <=100
    Bonus=0.1*(omset)
    print("Bonus :", Bonus)
    
Total_gaji=gaji_pokok+Bonus
print("Total Gaji :", Total_gaji)