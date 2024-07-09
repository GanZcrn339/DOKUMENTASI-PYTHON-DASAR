# Break
angka = 0

while angka < 5:
	angka += 1
	print(f"angka sekarang = {angka}")

	if angka == 3:
		print("nice!")
		break #jadi jika kita break perulangan nya hanya akan sampai di perualnagan ketiga

	print("wassup!")

print("cukuuup finish!")

data_int = int(input("hitung sampai = "))
#misal data_int di input 5

angka = 0

while True:
	angka += 1
	print(f"count = {angka}")

	if angka == data_int:
		#jika var angka yang 0 nanti nya = 5
		
		print("nice!") # maka print nice dan break (artinya program selesai)
		break

	print("wassup!") # wassup akan di print di perulangan yg tidak memenuhi syarat if

print("cukuuup finish!")