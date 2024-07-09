# import

# fungsinya adalah untuk mengambil 
# program dari file external .py

# 1. untuk menyambung program dari external
import program_print
import program_ucup

# 2. import dengan data
import variable
import kucuy
#variabel dan kucuy ini disebut nya namespace

# data ada di namespace variable
print(variable.data)
print(kucuy.data)
#cara pemanggilan data/var yang ada di file berbeda 
#seperti di atas, harus cantumkan dulu namespace nya baru nama var nya

# 3. import dengan fungsi
import matematika

hasil = matematika.tambah(4,5)
#begitu pun dengan fungsi harus namespace nya dulu
#baru fungsi nya dengan di isi var nya tapi kita juga 
#harus masukin ke dalam var lagi
print(hasil)
