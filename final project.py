import pandas as pd
from datetime import datetime
from prettytable import PrettyTable
import getpass
import os

# Membuat fungsi login
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
else:
    print("\033[31m\033[1mLogin Gagal! Username atau Password salah.\033[0m")
    exit()

# Fungsi untuk input slip gaji
def input_slip_gaji():
    current_datetime = datetime.now()
    current_datetime = current_datetime.date()

    # Membaca histori karyawan dari file CSV
    histori_file = "histori_karyawan.csv"
    if os.path.exists(histori_file):
        data_karyawan = pd.read_csv(histori_file).to_dict(orient='records')
        karyawan_data = {karyawan["NIK"]: karyawan["Nama"] for karyawan in data_karyawan}
    else:
        karyawan_data = {
            19240989 : "Reihan Pasha Ramadhan",
            19240290 : "Kamila Putri Navisu",
            19241739 : "Riri Syariah",
            19240737 : "Alni Nofiani",
            19240268 : "Aulia Shafira Yahya", 
        }

    # Memproses data slip gaji seperti biasa
    while True:
        print("=================================================================================================================================================================")
        print("\033[1m                                                                      PT JAYA ABADI SEJAHTERA         \033[0m")
        print("=================================================================================================================================================================")
        print(" ")
        print("                                                                        \033[4mSLIP GAJI KARYAWAN                    \033[0m")

        nik = int(input("NIK                         : "))

        if nik in karyawan_data:
            nama_karyawan = karyawan_data[nik]  
            print(f"Nama karyawan               : {nama_karyawan}")
        else:
            print("NIK tidak ditemukan.")
            tambah_karyawan = input("Apakah Anda ingin menambahkan karyawan baru? (y/n): ").lower()
            if tambah_karyawan == 'y':
                print("\n~ Menambahkan Karyawan Baru ~")
                tambahan_nama = input("Nama Karyawan Baru : ")
                tambahan_nik = int(input("NIK Karyawan Baru : "))
                karyawan_data[tambahan_nik] = tambahan_nama
                print(f"\nKaryawan baru dengan NIK {tambahan_nik} dan nama {tambahan_nama} berhasil ditambahkan.")
                
                # Menambahkan karyawan baru ke file CSV
                data_karyawan.append({
                    "Nama": tambahan_nama,
                    "NIK": tambahan_nik
                })
                df_karyawan = pd.DataFrame(data_karyawan)
                df_karyawan.to_csv(histori_file, index=False)

                nama_karyawan = tambahan_nama
            else:
                print("Tidak ada data yang ditambahkan, melanjutkan dengan program.")

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
        
        # Kondisi untuk menentukan honor lembur berdasarkan jabatan
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
        gaji_tahunan = gaji_pokok * 12  # Gaji tahunan
        if gaji_tahunan <= 60000000:
            potongan_pajak_pph = 5/100 * gaji_tahunan / 12  # Tarif 5% untuk gaji tahunan <= 60 juta
        elif gaji_tahunan <= 250000000:
            potongan_pajak_pph = 15/100 * gaji_tahunan / 12
        elif gaji_tahunan <= 500000000:
            potongan_pajak_pph = 25/100 * gaji_tahunan / 12
        else:
            potongan_pajak_pph = 30/100 * gaji_tahunan / 12
        
        # Rumus total potongan dan total gaji
        total_potongan = koperasi + potongan_bpjs_kesehatan + potongan_bpjs_tk + potongan_pajak_pph
        total_gaji = total_pendapatan - total_potongan

        # Menampilkan hasil perhitungan gaji
        print("_________________________________________________________________________________________________________________________________________________________________")
        print(" ")
        print("\033[1mPENDAPATAN\033[0m") 
        print("_________________________________________________________________________________________________________________________________________________________________")   
        print(f"  Gaji Pokok                : Rp.{gaji_pokok}")        
        print(f"  Tunjangan Jabatan         : Rp.{persentasi_jabatan}") 
        print(f"  Tunjangan Transportasi    : Rp.{tunjangan_transportasi}")
        print(f"  Tunjangan Pendidikan Anak : Rp.{persentasi_anak}")
        print(f"  Lembur                    : Rp.{honor_lembur}")
        print(f"  Uang Makan                : Rp.{uang_makan}")
        print(f"                             -------------- +")
        print(f"  Total Pendapatan          : \033[1m\033[4mRp.{total_pendapatan}")

        print("\033[0m_________________________________________________________________________________________________________________________________________________________________")
        print(" ")
        print("\033[1mPOTONGAN\033[0m")
        print("_________________________________________________________________________________________________________________________________________________________________")  
        print(f"  Koperasi                  : Rp.{koperasi}")
        print(f"  Potongan BPJS Kesehatan   : Rp.{potongan_bpjs_kesehatan}")
        print(f"  Potongan BPJS TK          : Rp.{potongan_bpjs_tk}")
        print(f"  Potongan Pajak PPh21      : Rp.{potongan_pajak_pph}")
        print("                             -------------- +")
        print(f"  Total Potongan            : \033[1m\033[4mRp.{total_potongan}\033[0m")
        print(" ")
        print(f"\033[1mTOTAL GAJI\033[0m                  : \033[1m\033[4mRp.{total_gaji}")
        print("\033[0m_________________________________________________________________________________________________________________________________________________________________")
        print(" ")
        print(f"                                                                                                                                             Cikarang, {current_datetime}")
        print(" ")
        print(" ")
        print("                                                                                                                                               Manager Operasional")
        print("                                                                                                                                           PT JAYA ABADI SEJAHTERA")

        # Menambahkan data karyawan ke dalam list
        karyawan = {
            "Nama": nama_karyawan,
            "NIK": nik,
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

        # Menyimpan data ke file CSV setelah input
        df_karyawan = pd.DataFrame(data_karyawan)
        df_karyawan.to_csv(histori_file, index=False)

        # Menampilkan tabel hasil slip gaji menggunakan PrettyTable
        tabel = PrettyTable()

        # Menentukan field names atau kolom tabel
        tabel.field_names = ["Nama", "NIK", "Jabatan", "Jumlah Jam Kerja", "Pendidikan Anak", "Gaji Pokok", "Total Pendapatan", "Total Potongan", "Total Gaji"]

        # Menambahkan data dari karyawan yang baru saja diinput ke tabel
        tabel.add_row([nama_karyawan, nik, jabatan, jam_kerja, pendidikan_anak, gaji_pokok, total_pendapatan, total_potongan, total_gaji])

        # Menampilkan tabel
        print("\n~ Tabel Hasil Slip Gaji ~")
        print(tabel)

        # Menanyakan apakah ingin melanjutkan atau tidak
        lanjut = input("\nApakah Anda ingin input data karyawan lain? (y/n): ").lower()
        if lanjut != 'y':
            break

# Fungsi untuk menambahkan karyawan baru
def tambah_karyawan_baru():
    histori_file = "histori_karyawan.csv"
    if os.path.exists(histori_file):
        data_karyawan = pd.read_csv(histori_file).to_dict(orient='records')
    else:
        data_karyawan = []

    while True:
        tambahan_nama = input("Nama Karyawan Baru : ")
        tambahan_nik = int(input("NIK Karyawan Baru  : "))

        # Menambahkan data karyawan baru ke dalam list data_karyawan
        karyawan_baru = {
            "Nama": tambahan_nama,
            "NIK": tambahan_nik
        }
        data_karyawan.append(karyawan_baru)
        print(f"Karyawan baru dengan NIK {tambahan_nik} dan nama {tambahan_nama} berhasil ditambahkan.")
        
        # Menyimpan data terbaru ke file CSV
        df_karyawan = pd.DataFrame(data_karyawan)
        df_karyawan.to_csv(histori_file, index=False)

        lanjut = input("Apakah Anda ingin menambahkan karyawan lain? (y/n): ").lower()
        if lanjut != 'y':
            break

# Menu utama setelah login
while True:
    print("\nMenu Utama:")
    print("1. Input Slip Gaji Karyawan")
    print("2. Tambah Karyawan Baru")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == '1':
        input_slip_gaji()  # Input slip gaji
    elif pilihan == '2':
        tambah_karyawan_baru()  # Menambahkan karyawan baru
    elif pilihan == '3':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
