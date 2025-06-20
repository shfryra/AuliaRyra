def SelectionSort(val):
    # Mengurutkan elemen dengan Selection Sort
    for i in range(len(val) - 1, 0, -1):
        Max = 0
        for l in range(1, i + 1):
            if val[l] > val[Max]:
                Max = l
        val[i], val[Max] = val[Max], val[i]

    # Menampilkan array yang telah diurutkan
    print(val)

    # Menampilkan sublist sesuai permintaan
    sublist1 = [val[1], val[2], val[4], val[5]]  # [3, 8, 15]
    sublist2 = [val[2]]  # [8]
    print(sublist1)
    print(sublist2)

Angka = [22, 10, 15, 3, 8, 2]
SelectionSort(Angka)
