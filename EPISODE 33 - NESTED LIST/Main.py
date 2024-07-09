data_0 = [1,2]
data_1 = [3,4,5]

data_list_biasa = [1,2,3,4]

print(f"list biasa = {data_list_biasa}")

list_2D = [data_0,data_1,6,7]

print(f"list 2D = {list_2D}")
# Kita bisa memasukan list ke dalam list seperti diatas

# contoh penggunaan

peserta_0 = ["ucup",25,"Laki-laki"]
peserta_1 = ["otong",10,"Laki-laki"]
peserta_2 = ["dedeh",50,"Wanita"]

list_peserta = [peserta_0,peserta_1,peserta_2]

print(f"peserta = {list_peserta}")
# sama seperti nested list di atas tapi tipe data nya string dan number

for peserta in list_peserta:
	print(f"nama\t: {peserta[0]}")
	print(f"umur\t: {peserta[1]}")
	print(f"gender\t: {peserta[2]}\n")
	#nah di atas kita bisa menampilkanya dalam bentuk for
	#dimana var list_peserta yang berisi 3 list juga yaitu [peserta_0,peserta_1,peserta_2]
	# nah ketika di print kita bisa panggil list yg ada di var list_peserta dengan index nya untuk di tampilkan


# dengan reference

list_copy = list_peserta.copy();
print(f"peserta = {list_copy}")
peserta_0[0] = "michael"
print(f"peserta = {list_copy}")
print(f"peserta = {list_peserta}")
# di list copy dan list peserta akan berubah list peserta_0[0] nya menjadi
# michael yang seharusnya tidak berubah jika di copy full duplicat
# karena menghasilkan data dengan address baru..
# jadi ternyata yang di copy nya itu hanya si list paling luar nya saja 
# di atas adalah list peserta yang paling luar nya, jadi jika kita mengganti
# isi dari nested list atau list yantg berada di dalam nya akan tetap berubah 
# walaupun kita copy...
