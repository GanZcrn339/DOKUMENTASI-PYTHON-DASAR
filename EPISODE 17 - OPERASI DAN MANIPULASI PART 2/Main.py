# operator dalam bentuk methods

## merubah case pada string

# merubah semua ke upper case
salam = "bro!"
print("normal " + salam)
salam = salam.upper()
print("upper " + salam)

# merubah semua ke lower case
alay = "aKu KeCe AbieeZZZ"
print("normal " + alay)
alay = alay.lower()
print("lower " + alay)

## method is, untuk pengecekan

# contoh isupper()
salam = "SIST"
apakah_upper = salam.isupper()
print(salam + " is upper? " + str(apakah_upper))
salam = salam.lower()
apakah_upper = salam.isupper()
print(salam + " is upper? " + str(apakah_upper))

# islower() <- untuk pengecekan apakah lower case semua
# isalpha() <- untuk mengecek apakah huruf semua
# isalnum() <- apakah huruf dan angka
# isdecimal() <- apakah numeric
# isspace() <- apakah isinya spasi, tab dan enter (newline \n)
# istitle() <- huruf pertama setiap kata upper case

judul = "It Is Okay To Not Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title? " + str(cek_judul))

# startwith() dan endwith() <-- keren

cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start " + str(cek_start))
#start with untuk mengecek kalimat pertama
cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end " + str(cek_end))
#endwith untuk mengecek kalimat terakhir

# join() dan split() <-- buat orang males
pisah = ['aku','sayang','kamu',]
gabungan = ' ehm '.join(pisah)
#join berfungsi untuk menambahkan var di antara string yg ada
print(pisah)
print(gabungan)

gabungan = "naik vespa keliling kota"
pisah = gabungan.split()
print(gabungan)
print(pisah)
#split berfungsi mengembalikan ke bentuk asalnya, kebalikan dari join
gabungan = "naikehmvespaehmkelilingehmkota"
pisah = gabungan.split("ehm")
print(gabungan)
print(pisah)
#conoth split seperti di atas untuk menghapus ehm nya di setiap antara string yg ada pada sebuah var

# alokasi karakter
print("'kiri      '")

kanan = "kanan".rjust(20) # rata kanan dengan 20 karakter
print("'" + kanan + "'")

kiri = "kiri".ljust(20) # rata kiri dengan 20 karakter
print("'" + kiri + "'")

tengah ="tengah".center(20) # rata tengah dengan 20 karakter
print("'" + tengah + "'")

tengah ="tengah".center(20,'-') # rata tengah dengan 20 karakter, yg ini sisa 20 char yg tidak terpakai diganti -
print("'" + tengah + "'")
#nah mksd nya di atas untuk memindahkan sebuah karakter, contoh nya di atas ada karakter kanan,
#yang di pindahkan ke paling kanan yg mana kaan ini terdapat di 20 char

# kebalikan dari alokasi karakter
kanan = kanan.strip()
print("'" + kanan + "'")
tengah = tengah.strip('-') #menghilangkan tanda -
print("'" + tengah + "'")