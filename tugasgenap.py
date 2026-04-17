def fibonacci(n):
    a, b = 1, 1
    print("Barisan fibonacci sebanyak", n, "suku :")
    
    for i in range(n):
        print(a, end=", " if i < n-1 else "")
        a, b = b, a + b
    print()


def perkalian():
    bilangan = int(input("Masukkan Suatu Bilangan Bulat : "))
    pengali = int(input("Masukkan Suatu Bilangan Pengali : "))
    
    hasil = bilangan * pengali
    print(f"\n{bilangan} x {pengali} = {hasil}")


while True:
    print("\nMenu Pilihan")
    print("1. Barisan Fibonacci")
    print("2. M Kali N")
    print("0. Keluar")
    
    pilih = input("Pilih Menu : ")
    
    if pilih == "1":
        n = int(input("\nMasukkan Jumlah Suku : "))
        fibonacci(n)
        
    elif pilih == "2":
        perkalian()
        
    elif pilih == "0":
        print("Program selesai.")
        break
        
    else:
        print("Pilihan tidak valid!")