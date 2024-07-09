# tipe data: angka satuan (integer)
data_integer = 1
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

#Koma berfungsi memisahkan data data lain supaya bisa nge print lebih dari satu data
# Nah di atas yang di print adalah comment yang mana nanti hasilnya akan
# menjadi kalimat yg berkorelasi dengan var data_integer
# data integer adalah data dalam bilangan bulat tanpa koma contoh 1 2 3 4 5 dan seterus nya
# type(data_integer) , untuk "type" berfungsi untuk mengecek tipe data pada variabel yg ada di dalam nya 



#tipe data: angka dengan koma (float)
data_float = 1.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))
#Tipe data float atau desimal, yaitu tipe data angka dengan sebuah koma

#tipe data: kumpulan karakter (string)
data_string = "ucup"
print("data : ", data_string)
print("- bertipe : ", type(data_string))
#tipe data string yaitu tipe data bertipe karakter seperti diambil dari alphabet
#jika disatukan dengan angka tipe data angka nya akan di anggap string
#contoh "ucup 10" , 10 nya akan di anggap string

#tipe data: biner true/false (boolean)
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))
#tipe data boolean adalah tipe data yg hanya memiliki dua nilai
# yaitu true / false

## tipe data khusus

#bilangan kompleks
data_complex = complex (5,6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

#tipe data dari bahasa C
#di python kita bisa menggunakan tipe data dari bahasa C


from ctypes import c_double
#di atas kita harus import dulu ctypes, ctypes ini mksd nya adalah kumpulan
# tipe data dari bahasa C, C_Double adalah tipe data yang lebih panjang dari float

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))





