#Kumpulan data integer
data_angka = [1,2,3,4,5,6,7,8,9,10]
print(data_angka)

#Kumpulan Data String

data_string = ['ghesa','otong','muaiman']
print(data_string)

#kumpulan Data Boolean
data_bolean = [True,False,True,False]
print(data_bolean)

#Kumpulan Campuran
data_campuran = [1,"uucp jualan somay", 2,'ghesa gamen' ,3,'firman masik']
print(data_campuran)

data_range = range(0,20,3) #start ,#stop, #step
data_list = list(data_range)
print(data_list)

list_fake_for = [i**3 for i in range(0,10)]
print(list_fake_for)

list_fake_for_if = [i for i in range(0,10) if i != 4]
print(list_fake_for_if)

list_fake_for_if = [i for i in range(0,10) if i%2 != 0]
print(list_fake_for_if)