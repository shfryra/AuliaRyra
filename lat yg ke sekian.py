print("====Cek Saldo====")
jumlah_saldo=int(input("Nominal yang hendak diambil:"))
if 2000 <= jumlah_saldo and jumlah_saldo <3000 :
    print("Masukan kode pin")
elif 3000 <= jumlah_saldo and jumlah_saldo <6000 :
    print("Masukkan kode pin")
elif 6000 >= jumlah_saldo and jumlah_saldo >10000 :
    print("Saldo anda tidak mencukupi")