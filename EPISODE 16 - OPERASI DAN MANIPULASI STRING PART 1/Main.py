# Operasi dan Memanipulasi String

# 1. Menyambung String (concatenate)
nama_pertama = "Ucup"
nama_tengah = "D"
nama_akhir = "Fame"
#kita buat 3 variabel berisi string

nama_lengkap = nama_pertama + nama_tengah + nama_akhir
#cara penggabunganya adalah dengan cara + setiap variabel string tadi 
#lalu di masukan ke dalam variabel lagi yaitu var nama_lengkap
print(nama_lengkap)
#kita print

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
#nah di atas kalo kita ingin menggunakan spasi
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("panjang " + nama_lengkap + " adalah " + str(panjang))
#nah dikarenakan var panjang ini isi nya int maka ketika di print harus di konversi ke
#string dulu dengan func str supaya tidak error

# 3. operator untuk string

# cek apakah ada komponen pada sebuah string
d = "d"
#kita masukan d ke dalam var d
status = d in nama_lengkap
#lalu kita cek dengan in seperti di atas yg artinya menanyakan apakah var d ada di dalam
#var nama_lengkap lalu kita masukan ke dalam var status
print("apakah " + d + " ada di " + nama_lengkap + ", " + str(status))
#lalu kita print, hasilnya akan false karena huruf d kecil tidak ada di var nama_lengkap

D = "D"
status = D in nama_lengkap
print("apakah " + D + " ada di " + nama_lengkap + ", " + str(status))
#nah kalon huruf D besar akan true

x = "x"
status = x not in nama_lengkap
#nah kalo di atas untuk menanyakan apakah tidak ada (not in) dalam sebuah var
print("apakah " + x + " tidak ada di " + nama_lengkap + ", " + str(status))

# mengulang string
print("wk"*100)
print(100*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0]) # dimulai dari 0
print("index ke-6 : " + nama_lengkap[6]) # index bebas
print("index ke-(-1) : " + nama_lengkap[-1]) # indexing dari dibelakang
print("index ke-[6,8) : " + nama_lengkap[6:8]) # dimulai dari index 6 sampai sebelum 8
print("index ke-[0,2,4,6,8] : " + nama_lengkap[0:10:2]) # diambil index 0,2,4,6,8

# item paling kecil
print("nilai terkecil : " + min(nama_lengkap))
# item paling besar
print("nilai terbesar : " + max(nama_lengkap))

ascii_code = ord(" ")
#American Standard Code for Information Interchange atau Kode 
#Standar Amerika untuk Pertukaran Informasi, adalah standar
#pengodean karakter untuk alat komunikasi. Kode ASCII mewakili teks
#dalam komputer, peralatan telekomunikasi, dan perangkat lainnya.
print("ASCII number dari spasi : " + str(ascii_code))
#di atas untuk mengecek ascii code nya
data = 117
print("Character dari ascii code 117 : " + chr(data))
#diatas untuk mengecek nomer 117 ascii code nya apa

# 4. operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o")
#.count salah satu method, beda nya dengan helper func adalah method nempel dengan var
print("jumlah o di " + data + " : " + str(jumlah))
#di atas adalah untuk menghitung jumlah o di dalam var data






























