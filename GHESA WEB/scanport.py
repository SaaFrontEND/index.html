def user_input():
    angka = 0

    while True:
        print("Selamat Datang Di Program ganjil/genap")
        user_input = input("mau lanjut di program ganjil/genap, (yes/no) :")
        

        if user_input.lower() != "yes":
            print('Terima kasih sudah menggunakan Program ini')
            break

        input_user = int(input('masukan angka :'))

        if input_user % 2 == 0:
            print(f"{input_user} angka genap")

        elif input_user % 2 != 0:
            print(f"{input_user} angka ganjil")
        else:
            print('masukan angka yang benar boskuh')

user_input()
    