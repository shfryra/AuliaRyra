import pandas as pd
from datetime import datetime
from prettytable import PrettyTable
import getpass
import os

# Membuat fungsi login
def login():
    print("\033[90m \033[1m~ HARAP MASUKAN USERNAME DAN PASSWORD! ~                    \033[0m")
    
    # Membuat variabel username dan password
    username = "admin"
    password = "123"

    # Mengambil input login
    input_username = input("Username: ")
    input_password = getpass.getpass("Password: ")  # Menggunakan getpass untuk menyembunyikan password input

    # Cek kredensial
    if username == input_username and password == input_password:
        print("\033[32m\033[1mLogin Berhasil!\033[0m\n")
        return True
    else:
        print("\033[31m\033[1mLogin Gagal! Username atau Password salah.\033[0m")
        return False

# Memeriksa login sebelum melanjutkan
if not login():
    print("Akses ditolak.")
    exit()

# Jika login berhasil, lanjutkan dengan program utama
current_datetime = datetime.now()
current_datetime = current_datetime.date()

# Membuat dictionary untuk menyimpan data NIK berdasarkan nama karyawan
karyawan_data = {
    "reihan pasha ramadhan": 19240989,
    "kamila putri navisu" : 19240290,
    "riri syariah" : 19241739,
    "alni nofiani" : 19240737,
    "aulia shafira yahya" : 19240268
}

# Membuat list untuk menyimpan data karyawan
data_karyawan = []

# Cek apakah file histori ada
histori_file = "histori_karyawan.csv"
if os.path.exists(histori_file):
    # Jika file ada, membaca data dari file CSV
    data_karyawan = pd.read_csv(histori_file).to_dict(orient='records')

while True:
    print("=================================================================================================================================================================")
    print("\033[1m                                                                      PT JAYA ABADI SEJAHTERA         \033[0m")
    print("=================================================================================================================================================================")
    print(" ")
    print("                                                                        \033[4mSLIP GAJI KARYAWAN                    \033[0m")

    # Menginput data
    nama = input("Nama Karyawan               : ").lower()

    # Mengecek apakah nama karyawan sudah ada dalam karyawan_data (untuk otomatisasi NIK)
    if nama in karyawan_data:
        nik_karyawan = karyawan_data[nama]  # Mengambil NIK yang sudah ada
        print(f"NIK                         : {nik_karyawan}")
    else:
        nik_karyawan = int(input("NIK                         : "))
        karyawan_data[nama] = nik_karyawan  # Menyimpan nama dan NIK di dictionary

    jabatan = input("Jabatan                     : ").lower()
    jam_kerja = int(input("Jumlah Jam Kerja/Bulan      : "))
    pendidikan_anak = input("Pendidikan Anak             : ")

    # Variabel
    gaji_pokok = 0
    uang_makan = 300000
    potongan_bpjs_kesehatan = 50000
    koperasi = 100000
    potongan_bpjs_tk = 100000
    potongan_pajak_pph = 0
    tunjangan_transportasi = 300000 
    gaji_tahunan = 0

    # Kondisi untuk menentukan gaji pokok berdasarkan jabatan
    if jabatan == "operator":
        gaji_pokok = 5000000
    elif jabatan == "staff admin":
        gaji_pokok = 6500000
    elif jabatan == "section head":
        gaji_pokok = 10000000
    elif jabatan == "manager":
        gaji_pokok = 20000000
    elif jabatan == "director":
        gaji_pokok = 40000000
    else:
        gaji_pokok = 0


    # Kondisi untuk menentukan tunjangan berdasarkan jabatan
    if jabatan == "operator" : 
        persentasi_jabatan = 30/100 * gaji_pokok
    elif jabatan == "staff admin"  :
        persentasi_jabatan = 45/100 * gaji_pokok
    elif jabatan == "section head" :
        persentasi_jabatan = 65/100 * gaji_pokok   
    elif jabatan == "manager" :
        persentasi_jabatan = 75/100 * gaji_pokok
    elif jabatan == "director"  :
        persentasi_jabatan = 85/100 * gaji_pokok
    else :
        persentasi_jabatan = 0 
        
    # kondisi untuk menentukan honor lembur berdasarkan jabatan
    if jabatan == "operator" :
        lembur_jabatan = 15000
    elif jabatan == "staff admin" :
        lembur_jabatan = 20000
    elif jabatan == "section head" :
        lembur_jabatan = 35000
    elif jabatan == "manager" :
        lembur_jabatan = 45000
    elif jabatan == "director" :
        lembur_jabatan = 70000

    # Kondisi untuk menentukan tunjangan pendidikan anak
    if pendidikan_anak == "TK" or pendidikan_anak == "tk" :
        persentasi_anak = 200000
    elif pendidikan_anak == "SD" or pendidikan_anak == "sd" :
        persentasi_anak = 400000
    elif pendidikan_anak == "SMP" or pendidikan_anak == "smp" :
        persentasi_anak = 600000
    elif pendidikan_anak == "SMA" or pendidikan_anak == "sma" :
        persentasi_anak = 800000
    elif pendidikan_anak == "-" :
        persentasi_anak = 0
    else :
        persentasi_anak = 0 

    # Kondisi untuk menentukan honor lembur
    if jam_kerja > 260 :
        jam_lembur = jam_kerja - 260
        honor_lembur = jam_lembur * lembur_jabatan
    else :
        honor_lembur = 0

    # Rumus total pendapatan, tunjangan dan honor lembur
    total_pendapatan = gaji_pokok + persentasi_jabatan + honor_lembur + uang_makan + tunjangan_transportasi + persentasi_anak
    tunjangan = persentasi_jabatan
    honor = persentasi_jabatan + honor_lembur

    # Kondisi untuk menentukan pajak pph21
    if gaji_tahunan <= 60000000 :
        potongan_pajak_pph = 5/100 * gaji_pokok 
    elif gaji_tahunan == 60000000 <= 250000000 : 
        potongan_pajak_pph = 15/100 * gaji_pokok 
    elif gaji_tahunan >= 250000000 <= 500000000 :
        potongan_pajak_pph = 25/100 * gaji_pokok
    else :
        potongan_pajak_pph = 0
    
    # Rumus  total potongan dan total gaji
    total_potongan = koperasi + potongan_bpjs_kesehatan + potongan_bpjs_tk + potongan_pajak_pph
    total_gaji = total_pendapatan - total_potongan

    # Menampilkan hasil perhitungan gaji
    print("_______________________________________________________")
    print(" ")
    print("\033[1mPENDAPATAN\033[0m") 
    print("_______________________________________________________")   
    print(f"  Gaji Pokok                : Rp.{gaji_pokok}")        
    print(f"  Tunjangan Jabatan         : Rp.{persentasi_jabatan}") 
    print(f"  Tunjangan Transportasi    : Rp.{tunjangan_transportasi}")
    print(f"  Tunjangan Pendidikan Anak : Rp.{persentasi_anak}")
    print(f"  Lembur                    : Rp.{honor_lembur}")
    print(f"  Uang Makan                : Rp.{uang_makan}")
    print(f"                             -------------- +")
    print(f"  Total Pendapatan          : \033[1m\033[4mRp.{total_pendapatan}")

    print("\033[0m_______________________________________________________")
    print(" ")
    print("\033[1mPOTONGAN\033[0m")
    print("_______________________________________________________")  
    print(f"  Koperasi                  : Rp.{koperasi}")
    print(f"  Potongan BPJS Kesehatan   : Rp.{potongan_bpjs_kesehatan}")
    print(f"  Potongan BPJS TK          : Rp.{potongan_bpjs_tk}")
    print(f"  Potongan Pajak PPh21      : Rp.{potongan_pajak_pph}")
    print("                             -------------- +")
    print(f"  Total Potongan            : \033[1m\033[4mRp.{total_potongan}\033[0m")
    print(" ")
    print(f"\033[1mTOTAL GAJI\033[0m                  : \033[1m\033[4mRp.{total_gaji}")
    print("\033[0m_______________________________________________________")
    print(" ")
    print(f"                                                                                                                                             Cikarang, {current_datetime}")
    print(" ")
    print(" ")
    print("                                                                                                                                               Manager Operasional")
    print("                                                                                                                                           PT JAYA ABADI SEJAHTERA")

    # Menambahkan data karyawan ke dalam list
    karyawan = {
        "Nama": nama,
        "NIK": nik_karyawan,
        "Jabatan": jabatan,
        "Jumlah Jam Kerja": jam_kerja,
        "Pendidikan Anak": pendidikan_anak,
        "Gaji Pokok": gaji_pokok,
        "Total Pendapatan": total_pendapatan,
        "Total Potongan": total_potongan,
        "Total Gaji": total_gaji
    }
    
    # Menyimpan karyawan ke dalam list
    data_karyawan.append(karyawan)

    # Menanyakan apakah ingin melanjutkan atau tidak
    lanjut = input("\nApakah Anda ingin input data karyawan lain? (y/n): ").lower()
    if lanjut != 'y':
        break

# Menyimpan data ke file CSV
df_karyawan = pd.DataFrame(data_karyawan)
df_karyawan.to_csv(histori_file, index=False)

# Mengonversi DataFrame pandas ke PrettyTable
def convert_to_prettytable(df):
    table = PrettyTable()
    table.field_names = ['No', 'Nama', 'NIK', 'Jabatan', 'Jumlah Jam Kerja', 'Pendidikan Anak', 'Gaji Pokok', 'Total Pendapatan', 'Total Potongan', 'Total Gaji']
    
    # Menambahkan nomor urut dan baris data
    for idx, row in df.iterrows():
        table.add_row([idx + 1] + row.tolist())
    
    # Menambahkan pengaturan alignment untuk kolom-kolom agar menjorok ke kiri
    table.align['No'] = 'l'  # Alignment kiri 'l'
    table.align['Nama'] = 'l'  
    table.align['NIK'] = 'l' 
    table.align['Jabatan'] = 'l'  
    table.align['Jumlah Jam Kerja'] = 'l'  
    table.align['Pendidikan Anak'] = 'l'  
    table.align['Gaji Pokok'] = 'l'  
    table.align['Total Pendapatan'] = 'l'  
    table.align['Total Potongan'] = 'l'  
    table.align['Total Gaji'] = 'l'  
    
    return table

# Mengonversi df_karyawan ke PrettyTable
pretty_table = convert_to_prettytable(df_karyawan)

# Menampilkan PrettyTable
print("\nData Karyawan:")
print(pretty_table)