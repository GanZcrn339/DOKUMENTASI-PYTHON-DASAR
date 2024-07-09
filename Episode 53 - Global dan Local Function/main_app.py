## Global dan Local scope

nama_global = "otong" # <- ini variabel global

# akses variabel global dalam fungsi
def fungsi1():
    print(f"fungsi menampilkan {nama_global}")
#variabel di atas kita gunakan di dalam func

fungsi1()

# akses variabel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")
    #nah sekarang var nya di akses di perulangan

# percabangan
if True:
    print(f"if menampilkan {nama_global}")
    #nah kalo di atas di percabangan


## Variabel Local Scope

def fungsi2():
    nama_local = "Ucup" # <- variabel lokal scope

fungsi2()
# print(nama_local) # tidak bisa dilakukan bos karena di dalam function fungsi2
#jadi variabel yang di dalam fungsi tidak bisa digunakan di luar fungsi

## Contoh 1: penggunaan akses variabel
def say_otong():
    print(f"Hello {nama}")

nama = "Otong"
#var nama bisa juga di taro di bawah func nya sebelum pemanggilan func
#tapi setelah pemanggilan func akan error
say_otong()

## contoh 2: merubah variabel global
angka = 0
name = "Ucup"

def ubah(nilai_baru, nama_baru):
    global angka # fungsi ini mendapat akses merubah var global
    global name
    angka = nilai_baru
    name = nama_baru
    #nah var angksa dan name yang tadi nya sudah di isi di atas akan di timpa
    #karena dijadikan argument untuk fungsi di atas

print(f"Sebelum {angka,name}")
ubah(10,"Otong")
print(f"Sesudah {angka,name}")

## contoh 3:
angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 5
    angka_dummy = 10

print(angka)
print(angka_dummy)

#untuk for dan if kita bisa mengakses var local dari luar