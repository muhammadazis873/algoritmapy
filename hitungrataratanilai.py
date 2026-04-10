nim = ["10121001", "10121002", "10121003"]
nama = ["asep", "budi", "cecep"]

nilai = [
    [50, 70, 40, 80],   # asep
    [78, 78, 80, 65],   # budi
    [57, 88, 67, 69]    # cecep
]

mk = ["MK1", "MK2", "MK3", "MK4"]

# cari rata-rata tiap mahasiswa
rata_mhs = []

for i in range(len(nama)):
    total = 0
    for j in range(len(nilai[i])):
        total += nilai[i][j]
    avg = total / len(nilai[i])
    rata_mhs.append(avg)

# cari mahasiswa paling pintar
max_avg = rata_mhs[0]
idx_mhs = 0

for i in range(len(rata_mhs)):
    if rata_mhs[i] > max_avg:
        max_avg = rata_mhs[i]
        idx_mhs = i

# cari rata-rata tiap mata kuliah
rata_mk = []

for j in range(len(mk)):
    total = 0
    for i in range(len(nama)):
        total += nilai[i][j]
    avg = total / len(nama)
    rata_mk.append(avg)

# cari mata kuliah dengan rata-rata terkecil
min_avg = rata_mk[0]
idx_mk = 0

for i in range(len(rata_mk)):
    if rata_mk[i] < min_avg:
        min_avg = rata_mk[i]
        idx_mk = i

print("mahasiswa paling pintar:")
print(nama[idx_mhs], "-", max_avg)

print("\nmata kuliah dengan rata-rata paling kecil:")
print(mk[idx_mk], "-", min_avg)