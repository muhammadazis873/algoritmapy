while True:
    print("\nMENU")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("0. Exit")

    while True:
        try:
            pilih = int(input("Pilih: "))
            break
        except:
            print("harus angka!")

    if pilih == 0:
        print("Keluar...")
        break

    while True:
        try:
            baris = int(input("Masukkan jumlah baris: "))
            break
        except:
            print("harus angka!")

    while True:
        try:
            kolom = int(input("Masukkan jumlah kolom: "))
            break
        except:
            print("harus angka!")

    print("\nMatriks A")
    A = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            while True:
                try:
                    x = int(input(f"A[{i}][{j}]: "))
                    row.append(x)
                    break
                except:
                    print("harus angka!")
        A.append(row)

    print("\nMatriks B")
    B = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            while True:
                try:
                    x = int(input(f"B[{i}][{j}]: "))
                    row.append(x)
                    break
                except:
                    print("harus angka!")
        B.append(row)

    hasil = []

    if pilih == 1:  # tambah
        for i in range(baris):
            row = []
            for j in range(kolom):
                row.append(A[i][j] + B[i][j])
            hasil.append(row)

    elif pilih == 2:  # kurang
        for i in range(baris):
            row = []
            for j in range(kolom):
                row.append(A[i][j] - B[i][j])
            hasil.append(row)

    elif pilih == 3:  # kali
        for i in range(baris):
            row = []
            for j in range(kolom):
                total = 0
                for k in range(kolom):
                    total += A[i][k] * B[k][j]
                row.append(total)
            hasil.append(row)

    else:
        print("Pilihan tidak ada")
        continue

    print("\nHasil:")
    for i in hasil:
        print(i)