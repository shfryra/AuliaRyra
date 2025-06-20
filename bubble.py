def BubbleSort(X):
    # Iterasi untuk setiap elemen
    for i in range(len(X) - 1, 0, -1):
        for j in range(i):  # Membandingkan elemen bersebelahan
            if X[j] > X[j + 1]:  # Jika elemen tidak terurut
                # Menukar elemen
                X[j], X[j + 1] = X[j + 1], X[j]

Hasil = [22, 10, 15, 3, 8, 2]
BubbleSort(Hasil)
print(Hasil)
