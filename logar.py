import numpy as np

# Input data pengguna
nama = input("Masukkan Nama : ")
NIM = input("Masukkan NIM : ")
Kelas = input("Kelas : ")

# Input ukuran matriks
rows = int(input("Masukkan jumlah baris matriks: "))
cols = int(input("Masukkan jumlah kolom matriks: "))

# Fungsi untuk memasukkan elemen matriks
def input_matrix(name, rows, cols):
    print(f"\nInput nilai untuk matriks {name}:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Masukkan nilai [{i+1}, {j+1}]: "))
            row.append(value)
        matrix.append(row)
    return np.array(matrix)

# Input matriks A dan B
matrix1 = input_matrix("A", rows, cols)
matrix2 = input_matrix("B", rows, cols)

# Hasil penjumlahan matriks
result_add = matrix1 + matrix2
result_sub = matrix1 - matrix2
result_mul = matrix1 * matrix2

# Header untuk nama, NIM, kelas
print(f"\nNama: {nama}")
print(f"NIM : {NIM}")
print(f"Kelas: {Kelas}\n")

# Fungsi untuk menampilkan matriks dengan format yang diinginkan
def print_matrices(matrix1, matrix2, result, operator):
    for i, (row1, row2, row_result) in enumerate(zip(matrix1, matrix2, result)):
        print(f"| {' '.join(map(str, row1))} |", end="")
        if i == rows // 2:  # Tampilkan tanda operator hanya di baris tengah
            print(f"  {operator}  ", end="")
        else:
            print("     ", end="")
        print(f"| {' '.join(map(str, row2))} |", end="")
        if i == rows // 2:  # Tampilkan tanda "=" hanya di baris tengah
            print("  =  ", end="")
        else:
            print("     ", end="")
        print(f"| {' '.join(map(str, row_result))} |")

# Menampilkan hasil penjumlahan matriks
print("Penjumlahan matriks:")
print_matrices(matrix1, matrix2, result_add, "+")

# Menampilkan hasil pengurangan matriks
print("Pengurangan matriks:")
print_matrices(matrix1, matrix2, result_sub, "-")

# Menampilkan hasil perkalian matriks
print("Perkalian matriks:")
print_matrices(matrix1, matrix2, result_mul, "*")