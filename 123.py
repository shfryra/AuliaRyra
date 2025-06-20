def mergeSort(X):
    print("Bilangan diurutkan: ", X)
    if len(X) > 1:
        mid = len(X) // 2
        lefthalf = X[:mid]
        righthalf = X[mid:]

        # Rekursi pada bagian kiri dan kanan
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0

        # Gabungkan dua bagian yang terurut
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                X[k] = lefthalf[i]
                i += 1
            else:
                X[k] = righthalf[j]
                j += 1
            k += 1

        # Jika masih ada elemen yang tersisa di lefthalf
        while i < len(lefthalf):
            X[k] = lefthalf[i]
            i += 1
            k += 1

        # Jika masih ada elemen yang tersisa di righthalf
        while j < len(righthalf):
            X[k] = righthalf[j]
            j += 1
            k += 1

        print("Merging: ", X)

# Data input sesuai soal pertama
X = [25, 20, 15, 3, 7, 2, 1]
print("Data sebelum diurutkan: ", X)
mergeSort(X)
print("Hasil akhir: ", X)