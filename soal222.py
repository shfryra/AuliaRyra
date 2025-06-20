n=int(input("Masukkan Nilai N :"))

print("tek kotek kotek kotek,anak ayam turun berkotek")
for i in range(n,0,-1):
    if i > 1:
        print(f"anak ayam turunlah {i} mati satu tinggallah {i-1}")
    elif i== 1:
        print(f"anak ayam turunlah {i} mati satu tinggallah induknya")


