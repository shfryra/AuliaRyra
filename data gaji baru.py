#input
print("=================================================")
print("         Program Hitung Gaji Karyawan            ")
print("              PT.DINGIN DAMAI                    ")
print("=================================================")

nama=input("Masukkan Nama Karyawan :")
gaji_pokok=int(input("Masukkan Gaji Pokok :"))
golongan=input("Masukkan Golongan Jabatan [1/2/3] :")
pendidikan=input("Masukkan Pendidikan [SMA/D1/D3/S1] :") 
jam_kerja=int(input("Masukkan Jumlah Jam Kerja :"))

#Tunjangan Jabatan
if golongan=="1" :
    tunjangan_jabatan=5/100*gaji_pokok
elif golongan=="2" :
    tunjangan_jabatan=10/100*gaji_pokok
else:
    tunjangan_jabatan=15/100*gaji_pokok

#Tunjangan Pendidikan
if pendidikan=="SMA" :
    tunjangan_pendidikan=2.5/100*gaji_pokok
elif pendidikan=="D1" :
    tunjangan_pendidikan=5/100*gaji_pokok
elif pendidikan=="D3" :
    tunjangan_pendidikan=20/100*gaji_pokok
elif pendidikan=="S1" :
    tunjangan_pendidikan=30/100*gaji_pokok
else :
    tunjangan_pendidikan=0

#Honor Lembur
if jam_kerja > 8 :
    jam_lembur=jam_kerja-8
    Honor_lembur=jam_lembur*3500
else :
    Honor_lembur=0

tunjangan_total=tunjangan_jabatan+tunjangan_pendidikan
total_honor=tunjangan_jabatan+tunjangan_pendidikan+Honor_lembur+gaji_pokok
print(f"Total Gaji Karyawan Adalah :{total_honor}")




