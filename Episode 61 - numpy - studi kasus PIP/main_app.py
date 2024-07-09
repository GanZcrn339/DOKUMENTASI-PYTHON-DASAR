import numpy as np
#nah kita import si library numpy atau pip numpy

list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])
#kita akan gunakan untuk menghitung vector
#di atas kita buat list a
#lalu kita buat list juga tapi menggunakan func nya numpy yaitu array

print(f"list_a = {list_a}")
# print(list_a**2) <- ini akan gagal
print(f"vector_a = {vector_a}")
print(f"a pangkat 2 = {vector_a**2}")
print(f"a kali 5 = {vector_a*5}")
#perbedaan pertama:
#menggunakan np array kita lgsg muncul matriks list nya tanpa koma
#perbedaan kedua
#karena sudah dalam bentuk vector jadi bisa di tambahkan operasi matematika langsung
#seperti pangkat 2 di atas atau kali lima

matrix_b = np.array([(1,2),(3,4)])
#(1,2) adalah matriks untuk baris pertama
#(3,4) adalah matriks untuk baris kedua
print(f"matrix b = \n{matrix_b}")
#kita print matriks nya
print(f"matrix b^2 = \n{matrix_b**2}")
#nah di atas matriks nya di pangkatkan dua

zeros_c = np.zeros((2,2))
print(f"zeros c = \n{zeros_c}")

ones_d = np.ones((2,2))
print(f"ones c = \n{ones_d}")

jumlah = matrix_b + matrix_b**2 + ones_d
print(f"jumlah = \n{jumlah}")