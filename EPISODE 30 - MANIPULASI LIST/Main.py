## Operasi

# index   0(-3)  1(-2)  2(-1)
data = ["Ucup","Otong","Dudung"]
print(data)

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")
#data terakhir bisa diambil menggunakan nomer index nya atau menggunakan minus -1
#perhitungan minus seperti pada penjelasan index di atas

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")
#contoh pengambilan data mnggunakan nomer minus,
#untuk minus ini tidak ada 0 yah, jadi sampe -1 untuk data terakhir nya
#berbeda dengan index

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")
#melihat panjang data/jumlah data

## Manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1,"Asep")
#nah untuk menambahkan list, kita menggunakan method insert
#yang mana di dalam kurung nya format nya seperti ini (posisi,item)
#nah jadi pertama kita bisa menentukan posisi nya kalo di atas contoh nya
# di insert pada index ke-1, lalu data nya adalah string asep
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("Jajang")
#kalo mau lgsg di akhir list, kita menggunakan method apppend
print(f"data ditambah lagi =\n{data}")

# menambah list dengan list
data_baru = ["Ujang","Usep","Dadang"]
data.extend(data_baru)
#nah extend untuk menambahkan list dengan list
print(f"data gabungan =\n{data}")

# merubah data
# kita ubah data 2 menjadi michael
data[2] = "Michael"
#kita isi posisi nya dengan [] lalu isi data nya
print(f"data rubah = \n{data}")

# meremove data

data.remove("Ujang")
print(f"data remove = \n{data}")
#untuk meremove seperti di atas
# data.remove("usep") akan error karena huruf harus sesuai yaitu "Usep"

# meremove data paling belakang
data_akhir = data.pop()
#pop untuk menghapus data yang paling belakang
print(f"data akhir = \n{data}")

print(data_akhir)