# Latihan perulangan membuat segitiga

sisi = 10

# 1. Menggunakan For

# dummy variable
print("awal For")
count = 1
for i in range(sisi):
	print("*"*count)
	count += 1

print("akhir dari for")
#bintang nya akan berakhir = sisi = 10
# 2. Menggunakan while

print("awal while")
count = 1
while True:
	print("*"*count)
	count += 1

	if count > sisi:
		break
	#bintang nya berakhir = 10 tapi ini menggunakan break, jadi jika count > sisi = 10, maka akan berhenti program nya

print("akhier while")

# 3. hanya ganjil saja

print("awal while")
count = 1
while True:
	if (count%2): # %2 untuk mencari angka ganjil, jadi jika modulus nya 1 akan di print
		# Print jika ganjil
		print("*"*count)
		count += 1
	else:
		# jika ketemu akan ganjil akan kembali ke atas dengan di tambahkan penambahan 1 untuk setiap perulangan nya
		count += 1
		continue
# intinya program di atas berfungsi menskip angka genap

	# akan break jika count melebihi sisi = 10 , jadi maksimal perulanganan nya 10 kali
	if count > sisi:
		break

print("akhier while")

# 4. hanya ganjil saja

print("awal while")
count = 1
spasi = int(sisi/2)

while True:
	if (count%2):
		# Print jika ganjil
		print(" "*spasi,"+"*count)
		# jika dapat angka ganjil maka ada spasi " " yang dikali * dengan var spasi
		# spasi = 5, jadi ketika di print nanti hasilnya di tengah karena kiri dan kanan nya ada spasi 5 karakter
		spasi -= 1
		#setiap angka ganjil ketemu maka spasi nya di kurang satu, contoh nya tadi 5 dikurang jadi 4
		count += 1
		#var count nya akan di iterasi +1 setiap perulangan 
	else:
		# akan kembali ke atas jika genap, mengulangi operasi di atas dengan nilai count sudah di +1
		count += 1 
		continue

	# akan break jika count melebihi sisi
	if count > sisi:
		break
# akan selesai jika melebihi sisi = 10
print("akhier while")













