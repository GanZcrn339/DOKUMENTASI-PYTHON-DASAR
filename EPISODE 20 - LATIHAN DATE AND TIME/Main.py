# Date and time (latihan)

import datetime as dt
#di atas kita import library datetime, mksd nya dt itu sebagai var yg isi nya datetime(class)
#yang akan digunakan, datatime ini library yang berisi berbagai class mengenai waktu

print("Silahkan masukan tanggal, bulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))
#kita buat inputan tanggal. bulan, tahun 

tanggal_lahir = dt.date(tahun,bulan,tanggal)
#kita gunakan library datetime yang jadi dt dan menggunakan method date untuk mengkonversi var
#tahun, bulan dan tanggal menjadi data dan di masukan kedalam var tanggal_lahir
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
#kita tampilkan

hari_ini = dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")
#nah di atas method untuk mengecek tanggal hari ini
umur_hari = hari_ini - tanggal_lahir # disamping perhitungan untuk melihat umur kita saat ini dalam bentuk total hari
umur_tahun = umur_hari.days // 365 # #disamping untuk membagi nya menjadi tahun dan mengubah tipe data nya menjadi int menggunakan method .days
umur_bulan_sisa = (umur_hari.days % 365) // 30 #disamping untuk mengitung bulan, jadi umur_hari di modulus 365 baru di bagi 30 atau di bulatkan ke bawah
# nah di atas adalah perhitungan untuk menghitung umur

print(f"Hari nya adalah : {tanggal_lahir:%A}")
print(f"Umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")
#hasilnya adalah umur kita dalam tahun dan bulan



