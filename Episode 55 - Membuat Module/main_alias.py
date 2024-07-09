# module matematika dengan import

from matematika import tambah as add
#nah fungsi tambah yang di ambil dari module matematika
#kita bisa ganti namanya menjadi add, begitu pun yang lainya
from matematika import kali as k
from matematika import pangkat as terserah_kalian_mau_apa
# from matematika import *

import matematika as math # <--- bisa dilakukan juga untuk nama module nya

hasil_tambah = add(1,2,3,4,5)
#jadi ketika di gunakan kita bisa pake nama alias nya yaitu add
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = math.kali(1,2,3,4,5)
print(f"hasil tambah = {hasil_kali}")

pangkat_3 = terserah_kalian_mau_apa(3)
print(f"hasil pangkat3 = {pangkat_3(3)}")