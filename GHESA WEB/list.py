def tampilkan_menu ():
    print("Tampilkan Menu")
    print("1.   Tambah Tugas")
    print("2.   Lihat Daftar Tugas")
    print("3.   hapus tugas")
    print("4.   keluar")

def tambah_tugas(daftar_tugas):
    tugas = input('masukan tugas anda : ')
    daftar_tugas.append(tugas)
    print("tugas telah di tambahkan")

def lihat_daftar_tugas(daftar_tugas):
    if not daftar_tugas:
        print("Daftar tugas kosong")
    else:
        print("\n Daftar Tugas")
        for i ,tugas in enumerate(daftar_tugas):
            print(f"{i+1}. {tugas}")

def hapus_tugas(daftar_tugas):
    if not daftar_tugas:
        print("Daftar Tugas Kosong")
    else:

        lihat_daftar_tugas(daftar_tugas)

        try:
            indeks = int(input('masukan tugas yang pengen di hapus:) '))-1
            if 0 <= indeks < len(daftar_tugas):
                del daftar_tugas[indeks]
                print("tugas berhasil di hapus")
            
            else:
                print('nomor tidak valid') 
        except ValueError:
            print("Input tidak valid ,Harap masukan angka")

def main ():
    daftar_tugas = []

    while True:
        tampilkan_menu()
        pilihan = int(input('masukan pilihan (1-4) :'))

        if pilihan == 1:
            tambah_tugas(daftar_tugas)
        elif pilihan == 2:
            lihat_daftar_tugas(daftar_tugas)
        elif pilihan == 3:
            hapus_tugas(daftar_tugas)
        elif pilihan == 4:
            print("terima kasih telah menggunakan program ini")
            break
        else:
            print('input tidak valid')

if __name__  == "__main__":
    main()