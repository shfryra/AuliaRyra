print("Studi kasus 1")
#bilangan genap sampai 10
for i in range(2,11,2):
    print(i)



print("Studi kasus 2")
jumlah = 0
for i in range(10) :
    i = i + 1
    print(i)
    jumlah = jumlah + i
print()
print("Jumlah Bilangan 1-10 adalah :", jumlah)


print("Studi kasus 3")
# Meminta input dari pengguna
N = int(input("Masukkan bilangan bulat (1 ≤ N ≤ 100): "))

# Mengecek apakah input berada dalam range yang diijinkan
if 1 <= N <= 100:
    # Membuat segitiga siku-siku dengan menggunakan "*"
    for i in range(1, N + 1):
        print("*" * i)
else:
    print("Masukan harus antara 1 hingga 100.")