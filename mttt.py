print("=========================STUDI KASUS 2=========================")
n = 4  # Ukuran matriks
A =([0,0,0,0],[0,0,0,0],[0,0,
0,0],[0,0,0,0]) # Matriks nol

# Mengisi elemen matriks
for i in range(n):
    for j in range(i + 1):  # Iterasi hanya sampai diagonal utama
        A[i][j] = i + 1  # Mengisi elemen sesuai aturan

# Menampilkan matriks
for row in A:
    print(row)

print("\n")
print("=========================STUDI KASUS 3=========================")
#matriks
matriks=([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])

#isi matriks
for i in range(4):
    for j in range(4):
        if i==j:
            matriks[i][j]=1
        if i>j:
            matriks[i][j]=0
        if i<j:
            matriks[i][j]=0
            
for i in range(4):
    print(matriks[i])

print("\n")
print("=========================STUDI KASUS 4=========================")
    # Deklarasi list dengan nilai awal
nilai = [1, 2, 3, 4, 5, 6]  # Memastikan cukup elemen untuk hasil yang diinginkan

# Mengisi list dengan nilai 2, 4, 6, 8, 10, 12
for i in range(len(nilai)):
    nilai[i] = 2 * (i + 1)  # Menghitung nilai berdasarkan indeks (1, 2, 3,...)

# Mencetak elemen-elemen dari list
for i in range(len(nilai)):
    print(nilai[i])

