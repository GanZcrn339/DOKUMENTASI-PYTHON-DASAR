# Lambda function

def f_kuadrat(angka):
    return angka**2

print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")
#di atas adalah function biasa

# kita coba dengan lambda
# output = lambda argument: expression
# nah jadi lambda argument sama kyk argument pada function umum nya
# cuman expression nya lgsg di tulis setelah titik dua, kalo di function biasa kan
#di tulis nya di bawah/didalam function nya
kuadrat = lambda angka : angka**2
#lambda function ini perlu di masukan ke dalam var
print(f"hasil lambda kuadrat = {kuadrat(5)}")
#cara pengisian argument nya seperti di atas

pangkat = lambda num,pow : num**pow
print(f"hasil lambda pangkat = {pangkat(4,2)}")
#bisa juga lebih dari dua argument seperti di atas

## kegunaan apa bang?

# sorting untuk list biasa
data_list = ["Otong","Ucup","Dudung"]
data_list.sort()
print(f"sorted list = {data_list}")
#data list untuk tipe data char yang di urutkan A-Z

# sorting dia pakai panjang
def panjang_nama(nama):
    return len(nama)
#di atas kita buat fungsi yang berfungsi untuk mengukur panjang nama

data_list.sort(key=panjang_nama)
#kita pakai function panjang nama dan di masukan ke dalam var key sebagai key
#dan kita gunakan sort untuk var data list yang isi nya data_list = ["Otong","Ucup","Dudung"]
#nah nanti akan di urut dari nama yang char nya paling sedikit ke yang paling panjang
print(f"sorted list by panjang = {data_list}")



# sort pakai lambda
data_list = ["Otong","Ucup","Dudung"]
data_list.sort(key=lambda nama:len(nama))
print(f"sorted list by lambda = {data_list}")
#nah kalo di atas pake lambda untuk mebgurutkan char paling sedikit ke yang paling panjang

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
# kita buat array

def kurang_dari_lima(angka):
    return angka < 5
#kita buat function untuk mencari angka kurang dari lima

data_angka_baru = list(filter(kurang_dari_lima,data_angka))
#kita gunakan filter yg didalam nya terdapat function kurang dari lima, dan array data angka
#yang artinya func kurang dari lima angka mengambil data array dari data angka yang kurang dari lima
data_angka_baru = list(filter(lambda x:x<7,data_angka))
#nah di atas jika kita menggunakan lambda dimana x sebagai argument
#dan x<7 sebagai expression atau return nya, lalu kita ambil data nya dari data angka
print(data_angka_baru)


# kasus genap
data_genap = list(filter(lambda x:(x%2==0),data_angka))
print(data_genap)

# kasus ganjil
data_ganjil = list(filter(lambda x:(x%2!=0),data_angka))
print(data_ganjil)

# kelipatan 3
data_3 = list(filter(lambda x:(x%3==0),data_angka))
print(data_3)

# anonymous function
# currying <- Haskell Curry 

def pangkat(angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(5,2)
print(f"fungsi biasa = {data_hasil}")

# dengan currying menjadi

def pangkat(n):
    return lambda angka:angka**n
#function nya pakai lambda(lambda = anonymous function)

pangkat2 = pangkat(2)
#nah jadi fungsi pangkat bisa di masukan ke da;am function lagi
#yang mana ketika kita mengisi argument nya = n
print(f"pangkat2 = {pangkat2(5)}")
#terus ketika kita print kita harus masukan arguemt nya lagi
#tapi kali ini argument nya yaitu argument dari lambda yang dijadikan return
pangkat3 = pangkat(3)
print(f"pangkat3 = {pangkat3(3)}")
print(f"pangkat bebas = {pangkat(4)(5)}")
