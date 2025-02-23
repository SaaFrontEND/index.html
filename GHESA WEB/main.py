# Fungsi-fungsi untuk operasi matematika
def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Tidak bisa dibagi dengan nol"
    return x / y

# Fungsi utama program kalkulator
def kalkulator():
    print("Selamat datang di Kalkulator Sederhana!")
    print("Operasi yang tersedia:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    while True:
        try:
            pilihan = int(input("Masukkan pilihan (1-4): "))
            if pilihan not in (1, 2, 3, 4):
                print("Pilihan tidak valid. Silakan coba lagi.")
                continue

            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))

            if pilihan == 1:
                print("Hasil:", tambah(angka1, angka2))
            elif pilihan == 2:
                print("Hasil:", kurang(angka1, angka2))
            elif pilihan == 3:
                print("Hasil:", kali(angka1, angka2))
            elif pilihan == 4:
                print("Hasil:", bagi(angka1, angka2))

            ulangi = input("Hitung lagi? (y/t): ")
            if ulangi.lower() != 'y':
                break

        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    print("Terima kasih telah menggunakan kalkulator ini!")

# Panggil fungsi utama untuk menjalankan kalkulator
kalkulator()