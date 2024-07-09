# looping dari list

# for loop
print("For Loop")
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
	print(f"angka = {angka}")
# Nah disini kita bisa melooping list ,
# menggunakan for yang mana angka adalah variabel yang disini dengan
# var kumpulan_angka yang nanti akan di print ke bawah secara berurutan 
# sesuai dengan index

peserta = ["ucup","otong","dadang","diding","dudung"]

for nama in peserta:
	print(f"nama = {nama}")
	# ini juga sama cuman tipe data list nya adalah string

# for loop dan range
print("\nFor Loop dan range")
kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)

for i in range(panjang):
	print(f"angka = {kumpulan_angka[i]}")
	# disini kita masukan terlebih dahulu, var kumpulan angka
    # ke var panjang dengan metode len untuk mengetahui keseluruhan jumlah data pada list nya
    # lalu kita loop menggunakan for dengan var i yang dimasukan var panjang dengan metode range
    # dan kita print

# while loop
print("\nWhile loop")
kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
	print(f"angka = {kumpulan_angka[i]}")
	i += 1
	#diatas sama saja tapi pake while

# list comprehension
print("\nList Comprehension")
data = ["ucup",1,2,3,"otong"]

[print(f"data={i}") for i in data]
# bisa langsung di print supaya lebih singkat

angka = [10,5,4,2,6,5]

angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)
#nah di atas listnya di kuadrat kan

# enumerate
print("\nEnumerate")
data_list = ["ucup",1,2,3,"otong"]

for index,data in enumerate(data_list):
	#enumirate var yg bisa dimasukan nya ada dua, contoh di atas
	#adalah index dan data
	print(f"index = {index}, data = {data}")
	# dengan enumirate kita bisa membuat loop dengan index sekaligus data nya
    