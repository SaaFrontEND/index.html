def operator (angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    return tambah,kurang,kali,bagi 


hasil_tambah,hasil_kurang,hasil_kali,hasil_bagi = operator (20,5)

print(f"hasil dari tambah = {hasil_tambah}")   
print(f"hasil dari kurang= {hasil_kurang}")   
print(f"hasil dari kali = {hasil_kali}")   
print(f"hasil dari  bagi = {hasil_bagi}")   

hasil_bagi = operator(15,5)