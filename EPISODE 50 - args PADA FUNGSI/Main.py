'''*args'''

# memasukan data/argument

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup",170,40)

def fungsi(data_list):
    # kita buat fungsi dengan argument data_list
    data = data_list.copy()
    # di bagian badan fungsi ini, kita masukan copyan dari data_list ke var data
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    # yang mana  data memiliki array yang akan kita input sesuai dengan
    # data yang dimasukan ke dalam variabel nya, jadi
    # nama sebagai index 0 dari data , tinggi index ke 1 , dan berat index ke 3

    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["otong",100,120])
# kita masukan data sesuai dengan index nya

# kenalan dengan *args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("dudung",120,120)
# jadi args itu sama aja sama data di atas di bagian fungsi sebelum nya,
# yang mana akan menjadikan var yang memiliki args sebagai array dengan index
# input nya sesuai nama var yang ada args nya

# studi kasus

def tambah(*data):
    # data tipenya adalah tuple, dia bisa diiterasi
    output = 0
    for angka in data:
        output += angka
        # kita buat perulangan dengan for di bagian fungsi nya
        # untuk menambah input nya
    
    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
# input akan di tambah sesuai for di atas di mulai dari 0
#  0 + 1 = 2, 1+2=3 dan seterus nya
print(f"hasil = {hasil}")
# kita print hasil nya

hasil = tambah(10,5,15)
print(f"hasil = {hasil}")
# ini juga sama