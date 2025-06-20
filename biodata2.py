#Tampilan atas biodata
lebar=115
print("="*lebar)
print("BIODATA".center(lebar))
print("="*lebar)

def biodata(nama="Aulia",umur=18, kewarganegaraan="Indonesia", alamat="Jl.H.Omon Somantri", 
            kode_pos="17330", kota="Bekasi", provinsi="Jawa Barat", 
            no_telepon="089673648146", status="Mahasiswa", fakultas="Teknik & Informatika"):
   
    print(f"Nama           : {nama}")
    print(f"Umur           : {umur}")
    print(f"Kewarganegaraan: {kewarganegaraan}")
    print(f"Alamat         : {alamat}")
    print(f"Kode Pos       : {kode_pos}")
    print(f"Kota           : {kota}")
    print(f"Provinsi       : {provinsi}")
    print(f"No. Telepon    : {no_telepon}")
    print(f"Status         : {status}")
    print(f"Fakultas       : {fakultas}")

# Pemanggilan fungsi dengan argumen default
biodata()
#Tampilan atas biodata
lebar=115
print("="*lebar)
