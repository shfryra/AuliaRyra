bil = int(input("Masukan Bilangan :"))

hasil = 1
a = bil

while a > 1:
    hasil *= a
    a -= 1

print("%d! = %d" % (bil, hasil))