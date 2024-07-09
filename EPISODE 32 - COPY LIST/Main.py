## Teknik menduplikat list

a = ["Ucup","Otong","Dudung"]
print(f"a = {a}")

b = a # pass by reference
print(f"b = {b}")
# jadi ada dua list yaitu list a dan list b yang isi nya sama dengan list a
#nah di list a dimasukan ke dalam var b jadi seperti ini 
# b = a = ["Ucup","Otong","Dudung"]


# kita akan merubah member dari a
# ini akan merubah kedua list
a[1] = "Michael"
# list dengan index 1 yaitu otong di ganti dengan Michael
b.sort()
# nah bahkan ketika kita merubah yang b dengan di sort maka yang a juga ikut berubah
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikat list dengan copy

print("membuat list c dengan a.copy()")
c = a.copy() # full duplikat / data baru
# Mengcopy data baru walaupun isi nya sama tapi address nya berbeda
# jadi jika kita ubah isi dari list nya, list yang lain tidak ikut berubah karena
# merupakan data baru dengan address yang berbeda

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("Kita ubah data 0")
c[0] = "Dadang"
# index ke 0 yaitu dudung di ubah menjadi dadang di variabel C

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("Kita ubah data 1")
a[1] = "Otong"
# index ke 1 dari data a di ubah menjadi Otong yang sebelumnya Michael
# yang mana otomatis variabel b juga berubah karena b = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")