# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Membagi array menjadi dua
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Menggabungkan dua bagian yang sudah diurutkan
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # Menggabungkan elemen secara terurut
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Menambahkan elemen yang tersisa
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Memilih pivot
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Rekursif pada bagian kiri dan kanan
    return quick_sort(left) + middle + quick_sort(right)


# Data awal
data = [25,20,15,3, 7,2, 1]

# Mengurutkan dengan Merge Sort
sorted_merge = merge_sort(data)
print(f"Hasil pengurutan dengan Merge Sort: {sorted_merge}")

# Mengurutkan dengan Quick Sort
sorted_quick = quick_sort(data)
print(f"Hasil pengurutan dengan Quick Sort: {sorted_quick}")