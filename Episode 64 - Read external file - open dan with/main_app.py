## Tutorial membaca file eksternal

print(3*"=", " Membaca file txt ", 3*"=")
#cara membuka file external seperti di bawah ini
#mode untuk menentukan Read atau write
file = open("data.txt",mode="r")

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")
#di atas untuk mengetahui 

## baca seluruh file
print(file.read())


## baca per baris
# print(file.readline(),end="") # baca baris pertama
# print(file.readline(),end="") # baca baris selanjut nya (kedua)

## baca semua baris sebagai list
# print(file.readlines())

print(f"apakah file sudah diclose : {file.closed}")
file.close()
print(f"apakah file sudah diclose : {file.closed}")


## salah satu teknik membuka file di python

print("\n",3*"=", " Membaca file txt dengan with", 3*"=")

with open("data.txt",mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah diclose : {file.closed}")

print(f"apakah file sudah diclose : {file.closed}")