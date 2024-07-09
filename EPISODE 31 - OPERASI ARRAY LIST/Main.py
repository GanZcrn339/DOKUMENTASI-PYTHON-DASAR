data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]

print(f"data angka = \n{data_angka}")

# count data

jumlah_data_4 = data_angka.count(4) 
# .count untuk Menghitung jumlah angka 4 yang ada pada list di atas
jumlah_data_3 = data_angka.count(3)
# Menghitung jumlah angka 3 yang ada pada list di atas

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data (index)

data = ["Ucup","Otong","Dudung","Ujang"]

print(f"data = {data}")

index_dudung = data.index("Dudung")
# ,index untuk menampilkan index dari list nya, contoh di atas dudung yang berada di index ke-2
index_ujang = data.index("Ujang")
print(f"index si Dudung = {index_dudung}")
print(f"index si Ujang = {index_ujang}")

# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
#sort untuk mengurutkan dari yang terkecil ke yang terbesar
print(f"data angka sort = \n{data_angka}")
# di urutkan dari yang paling kecil ke yang paling besar

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")
# jika array list nya  maka akan di urutkan berdasarkan huruf awal nya A ke Z

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")
# Ini sama aja tapi di balik cara pengurutan nya jika angka dari yang paling besar ke 
# yang paling kecil dan jika string maka dari z ke a