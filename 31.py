x = int(input("Masukan Nilai X : "))
y = int(input("Masukan Nilai Y : "))

if y == 0:
    hasil = 1
else:
    hasil = x
    for i in range(y - 1):
        hasil *= x

print("%d dipangkatkan %d = %d" % (x, y, hasil))

