while True:
    angka_1 = int(input('Masukkan angka 1: '))
    operator = input("Operator (+, -, *, /) atau ketik 'exit' untuk keluar: ")

    if operator == 'exit':
        print("Terima kasih, bang!")
        break

    angka_2 = int(input('Masukkan angka 2: '))

    if operator == '+':
        hasil = angka_1 + angka_2
    elif operator == '-':
        hasil = angka_1 - angka_2
    elif operator == '*':
        hasil = angka_1 * angka_2
    elif operator == '/':
        if angka_2 == 0:
            print("Error: Tidak bisa membagi dengan nol!")
            continue
        hasil = angka_1 / angka_2
    else:
        print("Operator tidak valid, coba lagi.")
        continue  # Mengulang loop jika operator tidak valid

    print('Hasil:', hasil)
