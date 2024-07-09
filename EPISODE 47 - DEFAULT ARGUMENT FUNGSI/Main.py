'''Default argument'''

# def fungsi(argument):
# def fungsi(argument = nilai defaultnya):
# jadi argument nya dijadiin kyk variabel yang mana nilai nya static jadi gk di input lagi

# contoh 1
def say_hello(nama = "Ganteng"):
    # nah kita bisa langsung masukan input argumetn nya di bagian def
    '''fungsi dengan default argument'''
    print(f"Hallo {nama}")
    # lalu kita langsung print nama argument nya karena emang kayak variable
    # tapi di atas harus di isi dulu



say_hello("Ucup")
say_hello()
# di print aja nggak cukup karena di atas masih bagian dari function nya
# kita harus panggil function nya kayak di atas, jika argument nya kosong
# maka yang muncul adalah default argument nya, dalam kasus di atas default arguemtn nya "Ganteng"
# maka akan muncul sesuai print nan nya, lalu jika kita isi argument  nya, maka akan di timpa
# si default argument nya, di atas ganteng jadi ucup

#contoh 2
def sapa_dia(nama, pesan = "Apa kabar?"):
    '''fungsi dengan satu input biasa, dan satu default argument'''
    print(f"hai {nama}, {pesan}")
    # di atas juga sama tapi default argument nya ada dua dengan value nya cuman 1

sapa_dia("Dudung","Hai Ganteeeng")
# jika kita isi kedua argument nya maka akan di timpa
sapa_dia("Otong")
# tapi jika salah satu saja maka default argument yang kedua akan mucul setelah yang pertama


#contoh 3

def hitung_pangkat(angka, pangkat=2):
    hasil = angka**pangkat
    return hasil
# ini sama kayak contoh dua tapi angka dan badan fungsi nya operasi aritmatika

print(hitung_pangkat(2,4))
# kita isi kedua default argument nya maka akan di timpa

hasil = hitung_pangkat(pangkat=3, angka=5)
# nah kalo ini kita isi kedua default argument nya tapi secara masing masing
# dan akan di timpa juga tapi sesuai dengan nama var argument nya jadi walaupun tertukar urutan penulisan argument nya tapi tetap akan berjalan
# jangan lupa masukan ke dalam variabel
print(hasil)
# print hasil nya

# contoh 4


def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil
# nah kalo ini sama tapi dengan banyak default argument

print(fungsi())
# jika tidak kita isi atau timpa maka akan di panggil seluruh default argument nya lalu badan fungsi akan dijalankan
print(fungsi(input3=10))
# kita juga bisa isi default argument atau di timpa default argument nya sesuai dengan
# default argument yang kita ingin kan, contoh nya di atas default argument, yang ketiga..