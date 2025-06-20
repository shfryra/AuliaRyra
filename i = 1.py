i = 1
j = 6
subtotal = 0
count = 0 

while i < j:
    number = i * 2
    print(number, end=' ')
    
    subtotal += number
    count += 1
    i = i + 1

print("\nSubtotal:", subtotal)
print("Rata-rata:", subtotal / count)