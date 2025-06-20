x = int(input("Masukan Batas Deret Bilangan Fibonacci : "))

print("Deret Fibonacci")
a, b = 0, 1
for i in range(x):
    print(a, end=' ')
    a, b = b, a + b
