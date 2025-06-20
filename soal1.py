print("Data mahasiswa baru")
NIS=int(input("Masukkan NIS :"))
nama=str(input("Masukkan Nama :"))
jurusan=input("Masukkan Kode Jurusan (SI/SIA) :")

#harga sesuai dengan jurusan

if jurusan=="SI" :
    harga=2400000
    prodi="sistem informasi"
elif jurusan=="SIA" :
    harga=2000000
    prodi="sistem informasi akuntansi"

else:
    print("Kode Jurusan Yang Dimasukkan Tidak Ada")
    harga=0

#menampilkan output

print("\nData mahasiswa baru :")
print(f"NIS: {NIS}")
print(f"nama: {nama}")
print(f"program studi: {prodi}")
print(f"biaya kuliah : Rp.{harga}")