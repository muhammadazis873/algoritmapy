x = int(input("Masukkan jumlah hari: "))

tahun = x // 365
sisa_hari = x % 365

bulan = sisa_hari // 30
hari = sisa_hari % 30

print("Tahun:", tahun)
print("Bulan:", bulan)
print("Hari:", hari) 