# continue, pass, break

# pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi, hanya menandakan bahwa ada sebuah kode tapi di pass supaya tidak dieksekusi

# angka = 0

# while angka < 5:
# 	angka += 1

# 	if angka == 3:
# 		pass # ini tidak akan dieksekusi

# 	print(angka)

# continue

angka = 0

print(f"angka sekarang -> {angka}")

while angka < 5:
	angka += 1
	print(f"angka sekarang -> {angka}") # aksi 1

	if angka == 3:
		print("nice!")
		continue # akan membuat loop meloncat ke step selanjutnya
	#jadi jika kita tidak menggunakan continue maka nice dan whassup ini akan di print
	#di setiap perulangan, tapi jika kita menggunakan continue, maka ketika perulangan sampai di angka 3
	#hanya akan nge print nice nya saja whassup nya tidak ikut di print di angka tiga, selain angka tiga whassup nya di print

	print("whassup!") # aksi 2

print("Pinish!")