# program list buku

list_buku = []
# Kita buat sebuah list
while True:
	# Kita buat perulangan menggunakan while
	print("\nMasukan data buku")
	judul = input("Judul buku\t: ")
	penulis = input("Nama penulis\t: ")
	# kita buat sebuah input yang dimasukan ke sebuah variabel judul dan penulis

	buku_baru = [judul,penulis]
	# kedua variabel di atas kita masukan sebagai list dan dimasukan ke
	# dalam var buku_baru
	list_buku.append(buku_baru)
	# Kita masukan sebagai list terakhir di list nya list_buku
	# jadi kalo kita input lagi buku_baru nya bakalan jadi gini
	# list_buku = [buku_baru[judul, penulis],buku_baru[judul,penulis]]
	# buku_baru kedua adalah appends

	print("\n\n","="*10,"Data Buku","="*10)

	for index,buku in enumerate(list_buku):
		print(f"{index+1} | {buku[0]} | {buku[1]}") 
		# untuk index nya udah bener +1 jadi 1 kalo dimulai dari 0
		# yang belom paham di bagian buku[0] dan buku[1]
		# tapi kyk nya gini
		# list_buku=[buku_baru[judul,penulis]]
		# tapi kalo for kan jadi gini 
		# buku = list_buku=[buku_baru(yg mana buku baru nya itu di appends)[judul, penulis]]
		# kesimpulan nya jadi 
		# buku = [judul,penulis], [judul,penulis]
		# belum tentu benar tapi logika nya masuk
		# tapi yg pasti buku[0] 0 merupakan index dari judul
		# dan buku [1] 1 nya merupakan penulis
	
	print("\n\n","="*20)

	isLanjut = input("Apakah dilanjutkan?(y/n) ")
	# kita buat input untuk perulangan nya, jika mau dilanjutkan ketik y
	# dan jika tidak ketik n

	if isLanjut == "n":
		break
	# jika kita ketik n maka program selesai

print("PROGRAM SELESAI")