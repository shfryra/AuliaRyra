print("NILAI SISWA")
nilai_ujian = int(input("nilai kamu :"))
if 55 <= nilai_ujian and nilai_ujian <= 60 :
    print("Nilai Kamu C") 
elif 61 <= nilai_ujian and nilai_ujian <= 70 :
    print("Nilai Kamu B")
elif 71 <= nilai_ujian and nilai_ujian <= 80 :
    print("Nilai Kamu A")
elif 81 <= nilai_ujian and nilai_ujian <= 90 :
    print("Nilai Kamu A+")
elif 91 <= nilai_ujian and nilai_ujian <= 101 :
    print("Nilai kamu A+ PERFECT")
elif 102 <= nilai_ujian and nilai_ujian <= 114 :
    print("Nilai Tidak Memiliki Kriteria")
else :
    print("Anda Tidak Lulus")



