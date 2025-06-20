def BinSearch(data, key):
    awal = 0  # Indeks awal (diubah menjadi 0 untuk penyesuaian indeks Python)
    akhir = len(data) - 1  # Indeks akhir (diubah menjadi len(data) - 1)
    ketemu = False
    
    while (awal <= akhir) and not ketemu:
        tengah = (awal + akhir) // 2  # Hitung indeks tengah
        
        if key == data[tengah]:
            ketemu = True
            print(f'Data {key} ditemukan di indeks {tengah + 1}')
        elif key < data[tengah]:
            akhir = tengah - 1
        else:
            awal = tengah + 1
    
    if not ketemu:
        print(f'Data {key} tidak ditemukan')


data = [3, 6, 9, 13, 16, 26, 38, 58]
key1 = 13
key2 = 16
key3 = 10

BinSearch(data, key1)
BinSearch(data, key2)
BinSearch(data, key3)
