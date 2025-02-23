def tampilkan_menu():
    print("\nMenu Daftar Tugas:")
    print("1. Tambah tugas")
    print("2. Lihat daftar tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

def tambah_tugas(daftar_tugas):
    tugas = input("Masukkan tugas baru: ")
    daftar_tugas.append(tugas)
    print("Tugas berhasil ditambahkan!")

def lihat_daftar_tugas(daftar_tugas):
    if not daftar_tugas:
        print("Daftar tugas kosong.")
    else:
        print("\nDaftar Tugas:")
        for i, tugas in enumerate(daftar_tugas):
            print(f"{i+1}. {tugas}")

def hapus_tugas(daftar_tugas):
    if not daftar_tugas:
        print("Daftar tugas kosong.")
    else:
        lihat_daftar_tugas(daftar_tugas)
        try:
            indeks = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
            if 0 <= indeks < len(daftar_tugas):
                del daftar_tugas[indeks]
                print("Tugas berhasil dihapus!")
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

def main():
    daftar_tugas = []

    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan (1-4): ")

        if pilihan == '1':
            tambah_tugas(daftar_tugas)
        elif pilihan == '2':
            lihat_daftar_tugas(daftar_tugas)
        elif pilihan == '3':
            hapus_tugas(daftar_tugas)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()