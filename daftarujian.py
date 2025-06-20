import pandas as pd

# Variable yang berulang menggunakan List/matriks
list_nim = []
list_uts = []
list_uas = []
list_total = []

ulang = 2
for i in range(ulang):
    print("Data Ke - " + str(i + 1))
    list_nim.append(input("Masukkan Nim anda: "))
    list_uts.append(int(input("Masukkan Nilai UTS anda: ")))
    list_uas.append(int(input("Masukkan Nilai UAS anda: ")))

# Proses menghitung total nilai per mahasiswa (rata-rata UTS dan UAS)
for i in range(ulang):
    rata_rata_per_siswa = (list_uas[i] + list_uts[i]) / 2
    list_total.append(rata_rata_per_siswa)

# Cetak data
print("=============================================================")
print("NIM            Nilai UTS        Nilai UAS      Rata-rata")
print("=============================================================")
for i in range(ulang):
    print("%s \t\t %i \t\t %i \t\t %.2f" % (list_nim[i], list_uts[i], list_uas[i], list_total[i]))
    print("=============================================================")
