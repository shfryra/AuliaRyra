print("Belanja")
harga_telur=int(input("harga telur per kg :"))
jumlah_yang_dibeli=int(input("Berat telur yang dibeli (kg):"))

total1=harga_telur*jumlah_yang_dibeli
print(total1)

print("Ongkos")
transportasi=int(input("Ongkos bolak balik :"))

total2=transportasi
print(total2)

print("Uang ibu")
Uang_ibu=int(input("Uang ibu :"))

total3=Uang_ibu
print(total3)

sisa=total3-total2-total1
print(sisa)
