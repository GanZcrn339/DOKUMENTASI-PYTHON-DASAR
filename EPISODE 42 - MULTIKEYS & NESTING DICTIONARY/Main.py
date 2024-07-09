import datetime

mahasiswa1 = {
	'nama':'Ucup Surucup',
	'nim':'19022001',
	'sks_lulus':130,
	'beasiswa':False,
	'lahir':datetime.datetime(2001,4,10)
}

mahasiswa2 = {
	'nama':'Otong Surotong',
	'nim':'19022002',
	'sks_lulus':140,
	'beasiswa':True,
	'lahir':datetime.datetime(2002,10,10)
}

mahasiswa3 = {
	'nama':'Asep Si Kasyep',
	'nim':'19022003',
	'sks_lulus':100,
	'beasiswa':False,
	'lahir':datetime.datetime(2000,2,29)
}
# kita buat tiga buah dictionary mahasiswa dengan key dan value nya

data_mahasiswa = {
	'MAH001':mahasiswa1,
	#'nama':'Ucup Surucup',
	#'nim':'19022001',
	#'sks_lulus':130,
	#'beasiswa':False,
	#'lahir':datetime.datetime(2001,4,10)
	'MAH002':mahasiswa2,
	'MAH003':mahasiswa3
}
# kita masukan dictionary mahasiswa sebagai value. dimana key nya kita buat baru seperti di atas

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*50)
#kita print teks dulu supaya seperti tabel

for mahasiswa in data_mahasiswa:
	#kita buat perulangan for


	KEY = mahasiswa 
	#nah di atas kita masukan perulangan mahasiswa yang isi nya ketiga dict tadi
	#ketika di print si Const KEY ini akan menampilkan hanya KEY nya saja tidak dengan values nya

	NAMA = data_mahasiswa[KEY]['nama']
	#nah untuk menampilkan value nya kita bisa menuliskan nya seperti di atas
	NIM = data_mahasiswa[KEY]['nim']
	SKS = data_mahasiswa[KEY]['sks_lulus']
	BEASISWA = data_mahasiswa[KEY]['beasiswa']
	LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x") #strftime supaya tanggal nya jadi pake format kek gini 10/03 /03 /
# disini tinggal kita masukan ke dalam const sesuai dengan key yang ada di value dari mahasiswa = data_mahasiswa
# index pertama yaitu KEY dari mahasiwa dan kedua key dari value mahasiswa yaitu dic dari mahasiswa1,2, dan 3

	print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")
	# kemudian kita print

