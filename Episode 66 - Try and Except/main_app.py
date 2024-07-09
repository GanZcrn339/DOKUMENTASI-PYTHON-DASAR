# exception akan terjadi saat program 
# mengalami error saat runtime

# contoh sederhana untuk menangkap exception

from math import nan

## contoh sederhana
# input_user = int(input("masukan angka: "))
# hasil = nan

# try:
#     hasil = 10/input_user
# except:
#     print("input tidak boleh 0")

# print(f"hasil = {hasil}")

# contoh di aplikasi

while(True):
    #selama nilai nya true kode di bawah ini akan terus berjalan
    angka = int(input("masukan angka pembagi: "))
    #kita buat input angka dan dimasukan ke dalam variabel
    try:
        #try berfungsi untuk mencoba nilai input yang benar saja
        hasil = 10/angka
        #kita buat var yang diisi nilai 10 yg mana dibagi lagi oleh angka yang kita input
        print(f"hasil = {hasil}")
        #Kita print hasilnya
        is_done = input("lanjutkan (y/n)? ")
        #nah kita buat input untuk make sure /memberhentikan program nya
        if is_done == "n":
            break
        #jika kita berhenti atau n maka programnya akan berhenti
    except:
        #kode except seperti nama nya yaitu kecuali, jika kita masukan angka nol
        #maka akan di print teks di bawah ini
        print("pembagi nol, silahkan masukan input lagi")

print("Akhir dari program 1")

# contoh aplikasi untuk membuat file data.txt 
try:
    with open("data.txt",'r') as file:
        print(file.read())
except:
    print("file data.txt tidak ditemukan, membuat file baru")
    with open("data.txt",'w',encoding='utf-8') as file:
        file.write("file baru")

print("akhir dari program 2")