def tampilkan_menu():
    print(f"SELAMAT DATANG DI PROGRAM KAMI")
    print(f"PILIH 1-4 UNTUK PROGRAM MANA YANG DINJALANKAN")
    print("1.Hitung Luas ")
    print("2.Hitung Keliling ")
    print("3.Hitung Semua ")

def masukan_angka():
    panjang = int(input('masukan nilai panjang : '))
    lebar = int(input('masukan nilai lebar :'))
    return panjang,lebar

def hitung_luas(panjang, lebar):
    return panjang * lebar

def hitung_keliling(panjang,lebar):
    return 2*(panjang+lebar)  

def opsi1():
    panjang,lebar = masukan_angka()
    luas = hitung_luas(panjang,lebar)
    print(f"hasil nilai luas : {luas}")
    return luas      

def opsi2():
    panjang,lebar = masukan_angka()
    keliling = hitung_keliling(panjang,lebar)
    print(f"hasil nilai dari keliling : {keliling}")
    return keliling

def opsi3():
    panjang, lebar = masukan_angka()
    luas = hitung_luas(panjang,lebar)
    keliling = hitung_keliling(panjang,lebar)
    print(f"hasil nilai luas : {luas}")
    print(f"hasil nilai dari luas : {keliling}")

    return luas,keliling


while True:
    tampilkan_menu()
    pilihan = input('masukan pilhan 1-4 : ')

    if pilihan == '1':
        opsi1()
    elif pilihan == '2':
        opsi2()
    elif pilihan == '3':
        opsi3()
    else:
        print('salah bro')

    berhenti = input('lanjut (y/n)')
    if berhenti.lower() != 'y':
        print('terima kasih sudah menggunakan program ini')
        break