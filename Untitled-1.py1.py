print("             PENDAFTARAN MAHASISWA BARU              ")
print("=====================================================")

biaya_kuliah={
    'SI' : {'Nama Prodi': 'Sistem Informasi','Harga' : 2400000},
    'SIA': {'Nama Prodi': 'Sistem Informasi Akuntansi','Harga' :2000000},
}
NIS=int(input("Masukkan NIS :"))
nama=str(input("Masukkan Nama :"))
jurusan=input("Masukkan Kode Jurusan (SI/SIA) :")

print("|-----------------------------------------------------------------------|")
print("| Kode Jurusan |     Nama Prodi                  |       Harga          |")
print("|-----------------------------------------------------------------------|")
print("| SI           | Sistem Informasi                | 2.400.000            |")
print("|SIA           | Sistem Informasi Akuntansi      | 2.000.000            |")
print("|-----------------------------------------------------------------------|")

print('Data Calon Mahasiswa :')
print('NIS :',NIS)
print('Nama :',nama)
print()
