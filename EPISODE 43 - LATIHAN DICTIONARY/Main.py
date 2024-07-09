'''Program data mahasiswa menggunakan dictionary'''
import datetime
import os
import string
import random

# template dict mahasiswa
mahasiswa_template = {
	'nama':'nama',
	'nim':'00000000',
	'sks_lulus':0,
	'lahir':datetime.datetime(1111,1,11)
}
# kita buat sebuah dictionary

data_mahasiswa = {}
# ini juga tapi dictinary kosong

while True:
	# nah disini make perulangan while yang mana jika input nya true maka akan terus berjalan perulangan nya
	# os.system("cls") # untuk windows
	os.system("cls")
	# diatas adalah syntax untuk mengclear output yang tidak diperlukan
	print(f"{'SELAMAT DATANG':^20}")
	print(f"{'DATA MAHASISWA':^20}")
	print("-"*20)

	mahasiswa = dict.fromkeys(mahasiswa_template.keys())
	# dict.fromkeys(mahasiswa_template.keys())
    # adalah sebuah metode untuk membuat dictionary baru menggunakan key dari
    # dictinary yang sudah di buat, kasus di atas kita akan ambil key dari mahasiwa_template
	mahasiswa['nama'] = input("Nama Mahasiswa: ")
	# nah kita sudah bikin dic mahasiswa yang mana sebuah dic kosong yang hanya
    # menggunakan key yang sama dengan dic mahasiswa_template
	mahasiswa['nim'] = input("NIM Mahasiswa: ")
	mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
	TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
	BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
	TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
	mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
# di atas merupakan beberapa input yang nanti nya user isi dan akan di masukan ke key 
# dari dic mahasiswa yang masih kosong
# ada bebrapa juga cont di atas untuk key lahir..
	KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
	# kode di atas untuk merandom key nya supaya unik, dengan string yang di uppercase dengan perulangan 6 char
	data_mahasiswa.update({KEY:mahasiswa})
	# kita update untuk menambah data mahasiswa ke var data_mahasiswa yang bener bener kosong dic nya
	# dari tutorial sebelumnya, hilangkan beasiswa
	print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS Lulus':<10} {'Tanggal Lahir':<10}")
	print('-'*60)

	for mahasiswa in data_mahasiswa:
		KEY = mahasiswa
		
		NAMA = data_mahasiswa[KEY]['nama']
		NIM = data_mahasiswa[KEY]['nim']
		SKS = data_mahasiswa[KEY]['sks_lulus']
		LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
		
		print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")
		# kode di atas penjelasan nya sama dengan kode yang ada di episode 42

	print("\n")
	is_done = input("Mau tambah lagi bro (y/n)? ")
	if is_done == "n":
		break
	# kode di atas untuk menghentikan proses perulangan nya dengan break..

print("\nAkhir dari program, terima kasih")