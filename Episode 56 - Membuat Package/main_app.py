import sains.matematika
#Di atas adalah cara pemanggilan module yang terdapat dalam pacakge
from sains import fisika

from sains.fisika import gaya as force

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
#jika cara pemanggilan nya import sains.matematika
#maka cara menggunakan nya seperti di atas, package, module, dan fungsi nya di panggil juga
print(f"hasil tambah dari package adalah = {hasil_tambah}")

gaya = fisika.gaya(90,10)
#jika cara pemanggilan nya from sains import fisika
#maka cara menggunakan nya seperti di atas
#lgsg ke module dan fungsi nya
print(f"gaya adalah = {gaya}")

gaya = force(90,10)
#jika cara pemanggilan nya 
# from sains.fisika import gaya as force
#maka cara menggunakan nya seperti di atas, langsung ke nama fungsi yang
#sudah di ganti dengan alias
print(f"gaya adalah = {gaya}")