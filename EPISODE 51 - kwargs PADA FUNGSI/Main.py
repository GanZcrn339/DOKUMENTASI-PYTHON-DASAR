'''**kwargs'''

def fungsi(nama,tinggi,berat):
    '''fungsi biasa'''
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup",183,79)
# diatas adalah fungsi biasa

def fungsi(**kwargs):
    # nah ini adalah fungsi kwargs yang mana nanti bisa pake keyword sesuka kita
    '''fungsi kwargs'''
    # bagian badan fungsi nya kyk kita mengambil key dari dictinary
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    # disini kita ambil key nya ke dalam variabel
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    # kita print

fungsi(nama="ucup",tinggi=183,berat=79)
# lalu kita panggil dengan mengisi argument nya sekaligus value nya


# studi kasus

def math(*args,**kwargs):
    # nah disini kita bisa masukan args dan kwargs secara sekaligus pada argument fungsi
    output = 0
    # disini output nya kita inisiasi 0
    if kwargs["option"] == "tambah":
        # kita gunakan pengkondisian if dimana jika kwargs nya key option sama dengan string tambah
        for angka in args:
            output +=angka
            # maka lakukan perulangan for dimana value args dimasukan kedalam
            # var for yaitu angka dimana perulangan nya adalah output yang 0 tadi ditambah
            # dengan input dari args nanti yang akan kita isi
    elif kwargs["option"] == "kali":
        # nah tapi jika kwargs nya adalah key "option" equal "kali"
        output = 1
    # maka output nya adalah 1
        for angka in args:
            output *= angka
            # yang mana input args dimasukan ke dalam perulangan for
            # dan output nya dikali dengan input angka dari args
    else:
        print("tidak ada operasi")
        # lalu jika tidak memenuhi if diatas maka else nya nge print string di atas

    return output

hasil = math(1,2,3,4,option="tambah")
# kita input args nya dengan int dan kwargs nya yang kita kasih nama option value nya kita isi tambah
# maka output nya akan menambah seluruh input args nya di mulai dari 0
#  0+1+2+3+4 = 10

print(f"hasil jumlah {hasil}")
# kita print hasil nya

hasil = math(1,2,3,4,option="kali")
# ini juga sama tapi di kali
print(f"hasil kali {hasil}")