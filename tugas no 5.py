print("=============GAJI PEGAWAI=============")
gaji_pokok=int(input("Gaji Pokok Karyawan:"))
jam_kerja=int(input("Jumlah jam kerja:"))
tunjangan=0.2*gaji_pokok
print("Tunjangan :",tunjangan)


if jam_kerja >200 :
    lembur=(jam_kerja-200)*20000
    print(f"Lembur :",lembur)

else :
    lembur=0
    print(f"lembur :",lembur)

total_gaji=gaji_pokok+tunjangan+lembur
print("Total Gaji : Rp.",total_gaji)

pajak=0.1*(gaji_pokok+tunjangan+lembur)
print("Pajak :",pajak)

gaji_bersih=gaji_pokok+tunjangan+lembur-pajak
print(f"Gaji :",gaji_bersih)