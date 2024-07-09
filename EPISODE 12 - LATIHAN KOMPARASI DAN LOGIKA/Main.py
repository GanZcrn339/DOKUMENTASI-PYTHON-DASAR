# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

#+++++++3--------10+++++++

inputUser = float(input("masukan angka yang bernilai\nkurang dari 3 \natau \nlebih dari 10\n:"))
#kita buat variabel yang nanti kita input tipe data float, jika bukan tipe data float juga akan di konversi ke float
# angka nya harus lebih besar dari tiga atau lebih kecil dari 10


# ++++++3-----------------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
#kita periksa var input tadi apakah kurang dari tiga isi nya dan di masukan ke dalam variabel lagi, cek nya dengan
#operator komparasi kurang dari <
print("Kurang dari 3 =", isKurangDari)
#lalu kita print

# ---------------10++++++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)
#di atas sama saja tapi untuk angka yang lebih dari 10 menggunakan operator lebih dari >

# ++++++3--------10+++++++

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan: ", isCorrect)
#inget!!! Operator OR jika salah satu nya hasilnya true, maka hasilnya akan true
#kasus di atas salah satu nya saja yang akan true entah itu angka kurang dari 3 atau lebih dari 10




#Contoh Kasus
# -----3++++++++10--------
# kasus irisan
print("\n",10*"=","\n")
inputUser = float(input("masukan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n:"))
#contoh kali ini sama saja, tapi yang di cari nya adlaah angka lebih dari 3 dan kurang dari 10



# -----3++++++++++++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 = ",isLebihDari)


# +++++++++++++++10-------
# kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10 = ",isKurangDari)

#di atas, setelah input nya kita isi baru kita cek apakah angka yang dimasukan 
# lebih dari 3 atau kurang dari 10

# -----3++++++++10--------
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukan: ", isCorrect)
#Nah kasus ini hasil akhir nya jika kita masukan angka yang benar maka hasilnya akan true
# karena menggunakan operator and yg mana kedua var harus true dua dua nya atau false dua dua nya
# untuk mendapatkan hasil true, kasus di atas tidak akan bernilai false dua dua nya
