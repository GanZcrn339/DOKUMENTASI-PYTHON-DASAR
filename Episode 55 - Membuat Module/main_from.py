# module matematika dengan import

from matematika import tambah,kali,pangkat
# from matematika import *

#nah from matematika itu namanya sekarang jadi module
#jadi mksd di atas adalah , dari module matematika
#kita import atau ambil fungsi tambah,kali dan bagi

hasil_tambah = tambah(1,2,3,4,5)
#jadi ketika kita gunakan kita tidak perlu menggunakan 
#namespace lagi 
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = kali(1,2,3,4,5)
print(f"hasil tambah = {hasil_kali}")

pangkat_3 = pangkat(3)
print(f"hasil pangkat3 = {pangkat_3(3)}")