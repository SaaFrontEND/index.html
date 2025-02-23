def jumlahkan (*data):
    output = 0 
    for angka in data:
        output += angka
    return output
print(jumlahkan(5,10,15))
print(jumlahkan(1,2,3,4,5))

hasil = jumlahkan(5,10,15)
hasil1 = jumlahkan(1,2,3,4,5)
print(f"hasil 5 + 10 + 15 : {hasil}")
print(f"hasil 1+2+3+4+5 : {hasil1}")

def maksimum(*data):
    output = 0  
    for angka in data:
        if angka > output:
            output = angka
        return output
hasil = maksimum(max(5,10,3,8))
hasil1= maksimum(max(1,99,50,75))


print(f"nilai paling terbesar adalah : {hasil}")
print(f"nilai paling terbesar adalah : {hasil1}")