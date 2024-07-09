data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1,10]
data_2D_copy = data_2D.copy()

print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# mengambil data dari nested list

data = data_2D[1][0]
# nah jadi cara mengambil data dari nested list adalah
# dengan cara memanggil [] , pada [] pertama itu adalah nested list pertama
# kemudian pada [] kedua adalah index dari nested list nya,
# seperti di atas [1] adalah nested list dari data_2D yaitu data_1 dan [0] adalah index dari
# data_1 yaitu 3, coba run
print(f"data = {data}")

# address semuanya

print(f"address asli = {hex(id(data_2D))}")
print(f"address copy = {hex(id(data_2D_copy))}")
# nah disini data 2d dan data 2d copy memiliki address yang berbeda karena 
# data 2d copy hasil dari full duplicat dari data 2d, .copy untuk menduplicat

print("address dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_copy[0]))}")
# tapi disini anggota dari list kedua list tersebut masih memiliki
# address yang sama , yg mana jika kita mengganti isi data dari list trersebut
# kedua nya masih akan berganti yang mana jika list biasa yang berganti hanya salah satu list nya saja


data_2D[1][0] = 5
data_2D[2] = 9
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
# nah disini cara untuk mengubah data dari nested list,
# yaitu dengan memasukan nya secara manual tanpa .copy
# diatas yang akan berubah hanya data 2d nya saja, yang data 2d.copy nya tidak


# kita gunakan deepcopy

from copy import deepcopy

data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address asli = {hex(id(data_2D))}")
print(f"address deep = {hex(id(data_2D_deepcopy))}")

print("address dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_deepcopy[0]))}")

data_2D[1][0] = 30
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deep = {data_2D_deepcopy}")
# Nah jika menggunakan deepcopy maka yang berubah nya hanya
# data 2d dan data 2d copy, sedangkan yang deepcopy tidak berubah karena address
# setiap list nya benar benar baru.
