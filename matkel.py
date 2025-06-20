# Penjumlahan Matriks 3x3
import numpy as np

# Nama, NIM, dan Kelas
nama=input("Masukkan Nama :")
NIM=int(input("Masukkan NIM :"))
Kelas=input("Kelas :")

def input_matrix(name):
    """Fungsi untuk menginput matriks 3x3"""
    print(f"\nMasukkan elemen Matriks {name} (3x3):")
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            value = int(input(f"Input nilai matriks {name} kolom ({j+1}) baris ({i+1}) = "))
            row.append(value)
        matrix.append(row)
    return matrix

def add_matrices(matrix_A, matrix_B):
    """Fungsi untuk menjumlahkan dua matriks 3x3 dengan output per elemen"""
    result = []
    print("\nPenjumlahan Matriks A + B:")
    for i in range(3):
        row = []
        for j in range(3):
            sum_value = matrix_A[i][j] + matrix_B[i][j]
            row.append(sum_value)
            print(f"A[{i+1},{j+1}] + B[{i+1},{j+1}] = {matrix_A[i][j]} + {matrix_B[i][j]} = {sum_value}")
        result.append(row)
    return result

def subtract_matrices(matrix_A, matrix_B):
    """Fungsi untuk mengurangi dua matriks 3x3 dengan output per elemen"""
    result = []
    print("\nPengurangan Matriks A - B:")
    for i in range(3):
        row = []
        for j in range(3):
            diff_value = matrix_A[i][j] - matrix_B[i][j]
            row.append(diff_value)
            print(f"A[{i+1},{j+1}] - B[{i+1},{j+1}] = {matrix_A[i][j]} - {matrix_B[i][j]} = {diff_value}")
        result.append(row)
    return result

def print_matrix(matrix, name):
    """Fungsi untuk mencetak matriks"""
    print(f"\nMatriks {name}:")
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    print("Program Penjumlahan dan Pengurangan Matriks Ordo 3x3")

    # Input Matriks A
    matrix_A = input_matrix("A")
    
    # Input Matriks B
    matrix_B = input_matrix("B")
    
    # Cetak Matriks A dan B
    print_matrix(matrix_A, "A")
    print_matrix(matrix_B, "B")

    # Penjumlahan Matriks dengan hasil ditampilkan
    matrix_sum = add_matrices(matrix_A, matrix_B)
    print_matrix(matrix_sum, "A + B (Penjumlahan)")

    # Pengurangan Matriks dengan hasil ditampilkan
    matrix_diff = subtract_matrices(matrix_A, matrix_B)
    print_matrix(matrix_diff, "A - B (Pengurangan)")

# Jalankan program utama
main()