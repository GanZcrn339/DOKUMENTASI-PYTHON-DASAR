# __main__ adalah top level code environment

# __name__ == "__main__" akan terjadi 
# jika ada di file program utama

## __name__ pada file program utama
print(f"nilai __name__ pada main.py = '{__name__}'")
#nah jadi __name ini menjadi program utama ketika dipanggil

## __name__ pada file program eksternal
import fungsi
#didalam module fungsi ada main jg yaitu __fungsi__ 
#ketika kita panggil disini yang keluar = __fungsi__
#bukan __main__

#tapi jika di panggil module nya lgsg maka hasilnya
#akan menjadi __main__ bukan __fungsi__

## contoh penggunaan __main__

# deklarasi
def fungsi_tambah(a:int,b:int)->int:
    return a+b

# fungsi utama
if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1,angka2)
    print(f"hasil tambah = {hasil}")


## import package
import package
