def BubbleSort(X):
    # Bubble Sort untuk urutan ascending
    for i in range(len(X) - 1, 0, -1):
        for j in range(i):
            if X[j] > X[j + 1]:
                X[j], X[j + 1] = X[j + 1], X[j]

# Daftar awal
Hasil = [22, 10, 15, 3, 8, 2]

# Mengurutkan secara ascending
BubbleSort(Hasil)
print("Ascending:", Hasil)

# Mengurutkan secara descending dengan membalik hasil ascending
Descending = Hasil[::-1]
print("Descending:", Descending)

# Menampilkan kembali hasil descending (sama seperti Descending)
print("Ascending:", Descending)

# Memfilter elemen tertentu: [22, 10, 3] dalam urutan yang benar
Filtered = [x for x in [22, 10, 3] if x in Hasil]
print("Filtered Result:", Filtered)
