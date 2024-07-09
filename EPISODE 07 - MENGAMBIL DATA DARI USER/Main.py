# Episode input user

# data yang dimasukan pasti string (mksd nya secara dasar akan menjadi string apapaun nilai yang di input)
data = input("Masukan data: ")
# input adalah function yang berfungsi dimana kita dipersilahkan mengisi sesuatu
#Dalam kasus di atas kita perlu masukan data yang mana hasilnya akan di simpan di variabel
# data

print("data = ",data,",type =",type(data))
#baru kita tampilkan hasil dan tipe nya

# jika kita ingin mengambil int, maka
angka = float(input("masukan angka: "))
angka = int(input("masukan angka: "))
# jika kita menggunakan variabel yang bukan constan seperti angka di atas
# maka yang akan di print salah satu nya saja dan yang terakhir
#kasus di atas var angka yang isi nya int

print("data = ",angka,",type =",type(angka))

# bagaimana dengan boolean
biner = bool(int(input("masukan nilai boolean: ")))

print("data = ",biner,",type =",type(biner))