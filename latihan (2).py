''' Latihan sederhana Python.
    Note: Perhatikan syntax/penulisan, terdapat typo pada codingan latihan di bawah.
    Latihan ini menggunakan Basic Syntax, Assignment Operator, Variable, dan Condition
    * Fungsi quit() digunakan untuk mengakhiri program.
'''

print("Selamat datang di Quiz Komputer!")

playing = input("Lanjut main? ")

# Buatkan kondisi yang hanya menerima kata 'Ya' untuk memulai Quiz dari variable playing di atas.
# Jika masukan variable playing bukan 'Ya', maka hentikan program.
if _________________:
    quit()

print("Okay, Ayo kita mulai! :)")
score = 0

# Berikan kondisi dimana jika jawaban benar, maka akan mencetak teks 'Correct!'
answer = input("Apa kepanjangan dari CPU?\n")
if _____________ == "central processing unit":
    print('Correct!')
    # Isi baris di bawah untuk menambahkan nilai 1 pada variable score jika jawaban benar.
    __________
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if _____________ == "graphics processing unit"
    print('Correct!')
    __________
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if _____________ == "random access memory":
    print('Correct!')
    __________
else
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if _____________ == "power supply":
    print('Correct!')
    __________
else:
    print("Incorrect!")

# Ganti bagian yang digaris bawahi dengan variable yang mencetak jawaban benar,
# dan total nilai dari jawaban yang benar.
print("You got " + str(____) + " questions correct!")
print("You got " + str((____ / 4) * 100) + "%.")