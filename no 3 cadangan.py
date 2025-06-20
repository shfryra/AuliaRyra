print("==================WARNET==================")

biayaawal=int(input("Masukkan tarif 3 jam pertama :"))
biayaselanjutnya=int(input("Masukkan tarif selanjutnya :"))
nama_pelanggan=input("Masukkan Nama Pelanggan :")
Lama_sewa=int(input("Lama waktu sewa (Jam):"))

if Lama_sewa <=3 :
    tarif=biayaawal*Lama_sewa
    print("Tarif :",tarif)

else :
    tarif=(biayaawal*3)+((Lama_sewa-3)*biayaselanjutnya)
    print("Tarif :",tarif)