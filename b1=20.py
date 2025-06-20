
print("##======== Mencari Nilai Terbesar ========##")

b1=int(input("Masukkan bilangan 1 :"))
b2=int(input("Masukkan bilangan 2 :"))
b3=int(input("Masukkan bilangan 3 :"))
b4=int(input("Masukkan bilangan 4 :"))

if b1>b2 and b1>b3 and b1>b4:
    nilai_terbesar=b1
elif b2>b1 and b2>b3 and b2>b4:
    nilai_terbesar=b2
elif b3>b1 and b3>b2 and b3>b4:
    nilai_terbesar=b3
else :
    nilai_terbesar=b4

print("Nilai Terbesar adalah :", nilai_terbesar)

