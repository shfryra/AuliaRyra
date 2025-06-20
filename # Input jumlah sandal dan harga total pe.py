# Data Barang
barang = [
    {"nama": "Beras", "berat": 14, "profit": 28},
    {"nama": "Gula", "berat": 10, "profit": 40},
    {"nama": "Kentang", "berat": 20, "profit": 70},
    {"nama": "Bawang", "berat": 12, "profit": 36},
    {"nama": "Empon-empon", "berat": 16, "profit": 24},
]

# Kapasitas truk
kapasitas_truk = 40

# Fungsi untuk menghitung rasio profit per berat
def hitung_rasio(barang):
    return barang["profit"] / barang["berat"]

# Mengurutkan barang berdasarkan rasio profit per berat secara menurun
barang.sort(key=hitung_rasio, reverse=True)

# Menentukan barang yang akan diangkut berdasarkan kapasitas truk
total_profit = 0
total_berat = 0
barang_terangkut = []

for b in barang:
    if total_berat + b["berat"] <= kapasitas_truk:
        barang_terangkut.append(b)
        total_profit += b["profit"]
        total_berat += b["berat"]
    else:
        # Jika truk tidak cukup, pilih sebagian barang yang tersisa
        sisa_berat = kapasitas_truk - total_berat
        if sisa_berat > 0:
            bagian_profit = b["profit"] * (sisa_berat / b["berat"])
            total_profit += bagian_profit
            total_berat += sisa_berat
        break

# Output hasil
print("Pola urutan data yang baru untuk Pi (Profit):")
for b in barang_terangkut:
    print(f"{b['nama']}: {b['profit']} juta Rp")

print("\nPola urutan data yang baru untuk Wi (Berat):")
for b in barang_terangkut:
    print(f"{b['nama']}: {b['berat']} ton")

print(f"\nProfit maksimal yang didapat: {total_profit} juta Rp")