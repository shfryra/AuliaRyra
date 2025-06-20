gaji_pokok = float(input("Masukkan gaji pokok: Rp. "))  # Gaji pokok
jam_lembur = float(input("Masukkan jumlah jam lembur per bulan: "))  # Jumlah jam lembur
jumlah_anak = int(input("Masukkan jumlah anak: "))  # Jumlah anak

# Menghitung upah per jam
upah_per_jam = (1 / 173) * gaji_pokok

# Menghitung total lembur
lembur = upah_per_jam * jam_lembur

# Tunjangan berdasarkan jumlah anak
if jumlah_anak == 0:
    tunjangan = 0
elif jumlah_anak == 1:
    tunjangan = 1000000
elif jumlah_anak == 2:
    tunjangan = 1250000
elif jumlah_anak == 3:
    tunjangan = 1500000
else:
    tunjangan = 0  # Tidak ada tunjangan lebih jika lebih dari 3 anak

# Tambahan untuk pegawai yang masuk selama 24 hari
tambahan_24_hari = 540000

# Menghitung pajak
pajak = 0.10 * gaji_pokok

# Menghitung gaji bersih
gaji_bersih = (gaji_pokok + tunjangan + lembur + tambahan_24_hari) - pajak

# Tampilkan hasil
print(f"\nGaji Bersih Pegawai: Rp. {gaji_bersih:,.2f}")