from . import Operasi
#kita import module Operasi

DB_NAME = "data.txt"
#di atas kita buat Const Untuk database nya yang di ambil dari file data.txt
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"
}

#kode di bawah untuk mengecek database apakah sudah tersedia atau tidak,
#jika tidak maka akan dipersilahkan untuk membuat nya
def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("Database tersedia, init done!")
    except:
        print("Database tidak ditemukan, silahkan membuat database baru")
        Operasi.create_first_data()
        #kita gunakan Func create_first_data() yang ada di module Operasi