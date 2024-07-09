import sains
#kita coba import package sains
from sains.matematika import scientific
#nah cara import di atas berhubungan dengan contoh yang keempat
#lihat contoh nya di bawah

hasil_tambah = sains.matematika.tambah(1,2,3,4,45)
#kita panggil fungsi tambah yang ada pada package matematika,
#yang mana package matematika ini berada dalam pacakge sains
#nah didalam package matematika ini ada sebuah
#init yang didalam nya sudah mengimport semua module
#yang ada di package matematika, termasuk module basic
#yang ada fungsi tambah
print(f"hasil tambah = {hasil_tambah}")

hasil_pisika = sains.pisika.gaya(10,9.8)
#nah kalo di natas kita panggil fungsi gaya yangada pada module pisika
#yang mana module pisika ada di dalam package sains
print(f"hasil pisika = {hasil_pisika}")

hasil_kali = sains.matematika.kali(1,3,4,5,6)
#ini sama kyk yang di atas cuman yang di panggil adalah fungsi kali
print(f"hasil kali = {hasil_kali}")

pangkat_3 = scientific.pangkat(3)
#nah di atas karena pemanggilan package dan module nya spesifik pake from
# dan yang di import nya module scientific, maka pas 
#menggunakan nya bisa kyk di atas, kita tulis fungsi dan module nya lgsg, 
#tanpa nulis lagi secara detail package dan modul modul nya
print(f"hasil pangkat 3 = {pangkat_3(5)}")
#dikarenakan fungsi pangkat menggunakan lambda
#jadi argument pertama yaitu pangkat(3) masuk ke argument fungsi nya
#nah sedangkan 5 masuk ke argument lambda nya, jadi 5 pangkat 3

# from sains import *

# hasil_tambah = matematika.basic.tambah(1,2,3,4,45)
# print(f"hasil tambah = {hasil_tambah}")

# hasil_pisika = pisika.gaya(10,9.8)
# print(f"hasil pisika = {hasil_pisika}")

# hasil_kali = matematika.basic.kali(1,3,4,5,6)
# print(f"hasil kali = {hasil_kali}")