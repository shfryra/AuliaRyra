import numpy as np

# Input data pengguna
nama = input("Masukkan Nama : ")
NIM =int(input("Masukkan NIM : "))
Kelas = input("Kelas : ")

# Input ukuran matriks
rows = int(input("Masukkan jumlah baris matriks: "))
cols = int(input("Masukkan jumlah kolom matriks: "))

# Fungsi untuk memasukkan elemen matriks
def input_matrix(name, rows, cols):
    print(f"\nInput elemen untuk matriks {name}:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Masukkan elemen [{i+1}, {j+1}]: "))
            row.append(value)
        matrix.append(row)
    return np.array(matrix)

# Input matriks A dan B
matrix1 = input_matrix("A", rows, cols)
matrix2 = input_matrix("B", rows, cols)

# Hasil penjumlahan matriks
result = matrix1 + matrix2

# Menampilkan matriks penjumlahan dengan format "+" hanya sekali
print("Penjumlahan matriks:")
for i, (row1, row2, row_result) in enumerate(zip(matrix1, matrix2, result)):
    print(f"| {row1[0]:2} {row1[1]:2} {row1[2]:2} |", end="")
    if i == rows // 2:  # Tampilkan tanda "+" hanya di baris tengah
        print("  +  ", end="")
    else:
        print("     ", end="")
    print(f"| {row2[0]:2} {row2[1]:2} {row2[2]:2} |", end="")
    if i == rows // 2:  # Tampilkan tanda "=" hanya di baris tengah
        print("  =  ", end="")
    else:
        print("     ", end="")
    print(f"| {row_result[0]:2} {row_result[1]:2} {row_result[2]:2} |")

import numpy as np

# Input ukuran matriks
rows = int(input("Masukkan jumlah baris matriks: "))
cols = int(input("Masukkan jumlah kolom matriks: "))

# Fungsi untuk memasukkan elemen matriks
def input_matrix(name, rows, cols):
    print(f"\nInput elemen untuk matriks {name}:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Masukkan elemen [{i+1}, {j+1}]: "))
            row.append(value)
        matrix.append(row)
    return np.array(matrix)

# Input matriks A dan B
matrix1 = input_matrix("A", rows, cols)
matrix2 = input_matrix("B", rows, cols)

# Hasil penjumlahan matriks
result = matrix1 - matrix2

# Menampilkan matriks penjumlahan dengan format "+" hanya sekali
print("Penjumlahan matriks:")
for i, (row1, row2, row_result) in enumerate(zip(matrix1, matrix2, result)):
    print(f"| {row1[0]:2} {row1[1]:2} {row1[2]:2} |", end="")
    if i == rows // 2:  # Tampilkan tanda "+" hanya di baris tengah
        print("  +  ", end="")
    else:
        print("     ", end="")
    print(f"| {row2[0]:2} {row2[1]:2} {row2[2]:2} |", end="")
    if i == rows // 2:  # Tampilkan tanda "=" hanya di baris tengah
        print("  =  ", end="")
    else:
        print("     ", end="")
    print(f"| {row_result[0]:2} {row_result[1]:2} {row_result[2]:2} |")