#password = input('masukan password anda : ')

#if len(password) < 8 :
 #   print('password terlalu lemah,minimal 8 karakter')
#else:
#    print('password cukup kuat')    



port_umum = [21,22,80,2222,8081]

while True:
    list_port = [21,22,80,2222,80081]
    print(list_port)
    port = int(input('masukan nomor port '))

    

    if port in port_umum:
        print(f"port {port} yang sering di gunakan")
    else:
        print(f'port {port} bukan port umum')

    pilihan = input('apakah kamu mau mengulang ? (y/n)')
    if pilihan.lower() != "y":
        print('terima kasih')
        break


