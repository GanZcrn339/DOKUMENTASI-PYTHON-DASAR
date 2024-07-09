# Latihan

# kalkulator sederhana
print(20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")

angka_1 = float(input("masukan angka 1 = "))
#kita buat input untuk angka nya
operator = input("operator (+,-,x,/) : ")
#kita buat input untuk operator nya 
angka_2 = float(input("masukan angka 2 = "))
#kita buat input untuk angka kedua nya

# percabangannya

if operator == "+":
	hasil = angka_1 + angka_2
	print(f"hasilnya adalah {hasil}")
	#nah di atas jika operator nya + maka tambahan angka 1 dan angka 2
	#lalu print hasilnya
elif operator == "-":
	hasil = angka_1 - angka_2
	print(f"hasilnya adalah {hasil}")
	#nah di atas jika operator nya - maka kurangkan angka 1 dan angka 2
	#lalu print hasilnya
elif operator == "x" or operator == "*":
	hasil = angka_1 * angka_2
	print(f"hasilnya adalah {hasil}")
	#nah di atas jika operator nya * maka kalikan angka 1 dan angka 2
	#lalu print hasilnya
elif operator == "/":
	hasil = angka_1 / angka_2
	print(f"hasilnya adalah {hasil}")
	#nah di atas jika operator nya / maka bagi angka 1 dan angka 2
	#lalu print hasilnya
else:
	print("masukan yang bener dong!, aku pusying")
	#nah di atas jika kita tidak benar memasukan angka dan operator nya maka akan false

print("Akhir dari program, terima gajih!")