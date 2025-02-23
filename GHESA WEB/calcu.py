def check_password(password):

        
        

        if len(password) < 8 :
            print('Password Lemah')
            return password

        ada_huruf_besar = any(char.isupper() for char in password)
        ada_angka = any(char.isdigit() for char in password)
        
        

        if ada_huruf_besar and ada_angka:
                return "password kuat"
        else:
                return "password sedang,tambahkan huruf besar atau kecil"


input_password = input('masukan password :')
print(check_password(input_password))

