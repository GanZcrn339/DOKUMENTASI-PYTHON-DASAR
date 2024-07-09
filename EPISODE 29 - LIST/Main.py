## --- LIST ---

# Kumpulan data numbers
data_angka = [1,5,2,3]
print(data_angka)

# Kumpulan data string
data_string = ["ucup","otong","odah"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan campuran
data_campuran = [1,"bala-bala",2,"cireng","ucup",True,"otong",False]
print(data_campuran)

## cara alternatif membuat list
data_range = range(0,10,2) # range(start,stop,step(increment ++)) disamping increment nya 2, jadi nanti 0-10 dari 0 nya ditambah +2 
print(data_range)
data_list = list(data_range)
#untuk range harus di konversi ke list dulu
print(data_list)

# membuat list dengan for loop, list comprehension
list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)
# nah kalo di atas kita pake perulangan yang mana angka di pangkat nya 2
#sampe nilai yg di pangkatkan nya 9^9 karena itunganya menggunakan index yaitu dari 0

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i != 5]
#ini pake for dan if, jadi tidak perulangan dari index 0 -10 kecuali index kelima akan diskip
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 ==0]
# nah di atas yang di print nya yang 0 dan genap saja, jadi yang ada sisa bagi nya yaitu angka 1 dan ganjil akan di skip
#atau yang dibagi 2 sisa bagi nya 0 hasilnya true atau di tampilkan
print(list_pake_for_if)

list_pake_for_if = [i**2 for i in range(0,10) if i%2 !=0]
#nah kalo di atas list perulangan angka ganjil yang dipangkatkan dua
# i%2 != 0 artinya angka yang dibagi 2 sisa bagi nya bukan 0, maka di tampilkan
print(list_pake_for_if)