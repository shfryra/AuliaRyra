import numpy as np

# Dua matriks 3x3
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

# Hasil penjumlahan
result = matrix1 + matrix2

# Menampilkan format penjumlahan dalam satu baris
print("Penjumlahan matriks:")
for row1, row2, row_result in zip(matrix1, matrix2, result):
    print(f"| {row1[0]:2} {row1[1]:2} {row1[2]:2} |  +  | {row2[0]:2} {row2[1]:2} {row2[2]:2} |  =  | {row_result[0]:2} {row_result[1]:2} {row_result[2]:2} |")