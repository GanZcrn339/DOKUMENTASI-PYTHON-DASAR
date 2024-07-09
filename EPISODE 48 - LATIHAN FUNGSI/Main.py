'''Latihan Fungsi'''

import os

# program menghitung luas dan keliling persegi panjang

# # Membuat header program
# os.system("clear")
# # os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # Mengambil input user
# LEBAR = int(input("Masukan nilai lebar: "))
# PANJANG = int(input("Masukan nilai panjang: "))

# # Program menghitung luas
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# # tampilkan hasilnya
# print(f"hasil perhitungan luas = {LUAS}")
# print(f"hasil perhitungan keliling = {KELILING}")

def header():
    '''fungsi Header'''
    os.system("cls")
    # os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")
    # kita buat header dengan fungsi

def input_user():
    '''fungsi input user'''
    # Mengambil input user
    lebar = int(input("Masukan nilai lebar: "))
    panjang = int(input("Masukan nilai panjang: "))

    return lebar,panjang
# kita buat input user dengan fungsi

def hitung_luas(lebar,panjang):
    '''fungsi luas'''
    return lebar*panjang
# kita buat lebar*panjang dengan fungsi

def hitung_keliling(lebar,panjang):
    '''fungsi keliling'''
    return 2*(lebar+panjang)
# ini juga sama lah

def display(message,value):
    '''fungsi display'''
    print(f"hasil perhitungan {message} = {value}")
    # nah ini fungsi hasil perhitungan nya, 


# Program utamanya
while True:
    # kita buat perulangan
    header()
    LEBAR,PANJANG = input_user()
    # yang mana input user nya di masukan ke dalam contan lebar dan panjang
    LUAS = hitung_luas(LEBAR,PANJANG)
    # lalu hasil fungsi hitung luas nya di masukan ke luas
    KELILING = hitung_keliling(LEBAR,PANJANG)
    #  hasil fungsi hitung keliling kita masukan ke const keliling

    display("luas", LUAS)
    # nah disini argument message kita masukan string nya , lalu argument value kita masukan
    # hasil dari fungsi hitung luas dan keliling
    display("keliling", KELILING)

    isContinue = input("apakah lanjut (y/n)? ")
    if isContinue == "n":
        # kita pake if dan break untuk menghentikan perulangan nya
        break

print("Program selesai, terima kasih")