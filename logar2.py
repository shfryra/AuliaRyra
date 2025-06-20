def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid  # Mengembalikan indeks elemen yang ditemukan
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1  # Jika target tidak ditemukan

# Deretan angka yang sudah diurutkan
numbers = [3, 6, 9, 13, 16, 26, 38, 58]

# Target yang ingin dicari
targets = [13, 16, 10]

# Melakukan pencarian untuk setiap target
for target in targets:
    result = binary_search(numbers, target)
    if result != -1:
        print(f"Angka {target} ditemukan di indeks {result}.")
    else:
        print(f"Angka {target} tidak ditemukan.")