# contoh membuat exception

from numbers import Number
#kita ambil Number dari library numbers

def tambah(a,b):
    #kita buat fungction dengan parameter var a dan b
    if not isinstance(a,Number) or not isinstance(b,Number):
        #kita buat if not menggunakan isinstance, isisntance berfungsi untuk
        #memastikan tipe data yang akan di isi untuk var nya
        raise "input harus angka"
    #raise ini merupakan exception, kyk try dan except tapi ini untuk if conditional
    return a+b

print(tambah(5,6))
#kalo diinput selain angka akan error dan raise nya akan tampil

angka = 0

# try:
#     hasil = 10/angka
# except Exception as error_message:
#     print(error_message)

try:
    hasil = 10/angka
except ZeroDivisionError as error_message:
    print(error_message)