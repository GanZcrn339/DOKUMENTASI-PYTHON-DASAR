# kita belajar casting
#merubah dari satu tipe ke tipe lain

#integer
print("====INTEGER====")
#di atas berfungsi sebagai tampilan saja 
data_int = 0;
#Tipe data int yang diisi value 0
print("data = ", data_int, ", type =", type(data_int))
#kita print variabel data_int beserta dengan menunjukan tipe data nya

data_float = float(data_int)
# Nah, variabel data_int yang value nya adalah nilai int, dipakai dalam function
# float yang berfungsi mengubah nilai di dalam nya menjadi tipe data float
# lalu di masukan kembali ke dalam variabel dengan nama data_float
data_str    = str(data_int)
#ini juga sama hanya saja mengubah nya kedalam str
data_bool = bool(data_int)  #akan false jika nilai int = 0
#nah di atas di ubah ke dalam boolean
print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_str, ",type = ", type(data_str))
print("data = ", data_bool, ",type = ", type(data_bool))
# lalu kita print

#float
print("====FLOAT====")
data_float = 9.5;
print("data = ", data_float, ", type =", type(data_float))

data_int    = int(data_float) # akan di bulatkan ke bawah brp pun nilai di belakang koma nya kyk di atas 9.5 akan menjadi 9
data_str    = str(data_float)
data_bool = bool(data_float) #akan false jika nilai float = 0
print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_str, ",type = ", type(data_str))
print("data = ", data_bool, ",type = ", type(data_bool))

#Boolean
print("====BOOLEAN====")
data_bool = True;
print("data = ", data_bool, ", type =", type(data_bool))

data_int    = int(data_bool) # akan di bulatkan ke bawah
data_str    = str(data_bool)
data_float = float(data_bool) #akan false jika nilai float = 0
print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_str, ",type = ", type(data_str))
#kalo di convert ke string, nilai boolean nya akan menjadi string, contoh True nya menjadi string
print("data = ", data_float, ",type = ", type(data_float))

#String
print("====STRING====")
data_str = "10"; #harus angka dan tidak boleh kosong kalo tidak int dan float akan error
print("data = ", data_str, ", type =", type(data_str))

data_int    = int(data_str) 
data_float    = float(data_str)
data_bool = bool(data_str) 
print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_float, ",type = ", type(data_float))
print("data = ", data_bool, ",type = ", type(data_bool))


















