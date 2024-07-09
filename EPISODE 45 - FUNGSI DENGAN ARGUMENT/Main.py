''' Fungsi dengan argument (input)'''

# Template
# def nama_fungsi(argument):
#     Badan fungsi


def hello_world(nama):
    # nah di def nya kita isi dengan var setelah nama fungsi nya
    # var nama setelah nama fungsi yang di kurungi disebut argument/parameter
    '''fungsi hello world menerima input dengan variable nama'''
    print(f"Selamat datang dunia wahai {nama}")


hello_world("ucup")
hello_world("Asyep")
# kita isi argument nama di atas di pemanggilan fungsi nya


# program tambah

def tambah(angka_1,angka_2):
    '''fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,5)
tambah(100000,1)
# ini juga sama tapi proses aritmatika fungsi nya dengan 2 argumen, 

def say_hi(list_peserta):
    '''fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")

anggota_boyband = ["Ucup","Otong","Dudung"]
# disini list nya kita masukin ke dalam var yang mana akan menjadi argument nantinya
#  nah jadi anggota_boyband ini variabel list yang di luar fungsi yang mana jika kita masukan
# kedalam argument function di atas walaupun berbeda nama nya akan tetap jalan
# seperti list_peserta = anggota_boyband
say_hi(anggota_boyband)
# ini juga sama tapi argument nya berisi list
# dengan perulangan juga