from time import time
from . import Database
from .Util import random_string
import time

def create_first_data():
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    tahun = input("Tahun: ")

    data = Database.TEMPLATE.copy()
    #nah Const TEMPLATE yang 

    data["pk"] = random_string(6) 
    #pk harus unik makanya pake random string
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun
    #Kita isi key yang ada di dictionary TEMPLATE

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    #nah seluruh data tadi yang sudah di inpit kita masukan ke var data_str
    print(data_str)
    #baru kita tampilkan
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udah lah Gagal booooos")
        #try except di atas untuk memastikan database berhasil di buat atau tidak

def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    except:
        print("Membaca database error")
        return False
    #di atas func untuk read yang digunakan di module view
    
    