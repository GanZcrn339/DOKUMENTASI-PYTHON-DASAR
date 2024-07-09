# Perulangan (loop)

# for kondisi:
# 	aksi

#perulangan atau looping ini mirip dengan if else
#jadi fungsi nya untuk mengulangi pekerjaan, jadi kita tidak perlu menuliskan program nya berulang kali satu satu


# ini dengan list
angka2_list = [0,2,4,8,10] # ini adalah list
print(angka2_list)

for i in angka2_list:
	# var angka2_list di masukan ke dalam var i dan di ulang dengan for
	print(f"i sekarang -> {i}")
	#hasilnya print ini akan memprint isi nya berulang kali sampai isi list
	# var angka2_list yang di masukan ke dalam i habis, nah nilai i akan mengikuti isi list satu persatu

print("akhir dari program 1 \n")
#kseimpulan nya jika lgsg di print angka2_list akan menghasilkan list nya
# tapi jika di for akan menghasilkan nilai baru yaitu list yg dimasukan ke dalam var i yang diulang sampai habis

# ini dengan range
angka2_range = range(5)

for i in angka2_range:
	print(f"i sekarang -> {i}")

print("akhir dari program 2 \n")
# di program 2 kita menggunakan range yang mana range ini di isi dengan angka 5
#artinya akan mengambil list sampai index ke-5 yaitu angka 4, hasilnya sama seperti loop pada program satu tapi sampai angka 4

angka2_range = range(1,10)

for i in angka2_range:
	print(f"i sekarang -> {i}")
	# print("saya keren")

print("akhir dari program 3 \n")
#nah di atas range nya 1,10 artinya angka mengambil index 1 sampai 10 dari sebuah list


# menggunakan string

data_str = "saya ganteng abiees"

for huruf in data_str:
	print(huruf)
	# huruf disini terserah kita nulisnya mau apa
    # bisa di ganti sesuai yang kita inginkan tapi
    # yang pasti itu adalah variabel untuk string di atas
    

print("akhir dari program 4 \n")
#hasil akhir nya adalah si "saya ganteng abiees"
#akan di ulang satu per satu karakter nya







