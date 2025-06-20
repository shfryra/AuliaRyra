#TUGAS LANJUTAN 1
# Meminta input dari pengguna
n = int(input("Masukkan bilangan bulat N: "))
karakter = input("Masukkan karakter untuk menggambar pola: ")

k = 2 * n - 2  # Menghitung jumlah spasi awal
for i in range(0, n):
    # Mencetak spasi
    for j in range(0, k):
        print(end=" ")
    k = k - 1  # Mengurangi jumlah spasi

    # Mencetak karakter
    for j in range(0, i + 1):
        print(karakter, end=" ")  # Menggunakan karakter yang dimasukkan
    print()  # Pindah ke baris berikutnya



#TUGAS LANJUTAN 2
n = int(input("masukan nominal anak ayam: ")) 
if 0 < n < 100 :

   print("tek kotek kotek kotek, anak ayam turun berkotek")
if n >= 1 and n <=100:
   for n in range(n, 0, -1): 
    print(f"anak ayam turunlah {n} mati satu tinggallah {n-1}")
   print(f"anak ayam turunlah {n} mati satu tinggallah induknya")

else :
  print("angka tidak valid")