print("## Profile Mahasiswa ##")
print("=====================================================")

a=input("Nama :")
b=input("Nim :")
c=input("Kelas :")

print("## Program Python Menghitung Luas Segitiga ##")
print("=================")
alas=float(input(" Input alas :"))
tinggi=float(input(" Input tinggi :"))

luas_segitiga=0.5*alas*tinggi
print("luas_segitiga:" ,luas_segitiga)

print("## Program Python Menghitung Luas Persegi Panjang ##")
print("=====================================================")
print("Luas persegi panjang")
panjang=float(input("Panjang :"))
lebar=float(input("Lebar :"))

luas_persegi_panjang=panjang*lebar
print("luas_persegi_panjang:" ,luas_persegi_panjang)

print("## Program Python Menghitung Luas Bujur Sangkar ##")
print("=====================================================")
print("Luas bujur sangkar")
sisi=float(input("Sisi :"))

luas_Bujur_sangkar=sisi*sisi
print("luas_Bujur_sangkar:" ,luas_Bujur_sangkar)

print("Total seluruhnya")
total_seluruhnya=luas_segitiga+luas_persegi_panjang+luas_Bujur_sangkar
print(total_seluruhnya)

print("Rata_rata")
rata_rata=total_seluruhnya/3
print(rata_rata)