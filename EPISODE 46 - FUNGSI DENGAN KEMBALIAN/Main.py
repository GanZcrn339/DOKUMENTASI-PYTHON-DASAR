''' Fungsi dengan kembalian'''

# template fungsi dengan kembalian
# def nama_fungsi(argument):
#       badan fungsi
#       return output

# fungsi kuadrat    

def kuadrat(input_angka):
    # kita buat function kuadrat untuk membuat fungsi meng kuadratkan 
    # sebuah angka dengan nama argumen nya input_angka
    '''Fungsi kuadrat'''
    output_kuadrat = input_angka**2
    # input_angka yang menjadi argumen kita tambahkan operasi pangkat dua **2
    # lalu kita masukan ke var output_kuadrat
    return output_kuadrat
    # kemudian kita kembalikan nilai nya atau return
    # yang mana hasil dari angka yang dimasukan user pada argument di atas 
    # akan di pangkat kan 2 dan hasilnya akan diperlihatkan kepada user

y = kuadrat(5)
# nah si fungsi kuadrat di atas kita isi argumen nya dengan angka 5
# yang mana pada function di atas dijelaskan bahwa angka yang di masukan pada argumen
# di pangkat kan 2 jadi angka 5 pangkat 2 sama dengan 25
print(y)
# kita print hasilnya

print(kuadrat(6))
# bisa juga kita print langsung function nya tanpa kita masukan dulu ke variabel

z = 10 + kuadrat(7)
# disini fungsi kuadrat tadi juga bisa dipake dengan operasi lain nya seperti di atas
# dimana fungsi kuadrat yang argument nya angka 7 di tambah 10 dan dimasukan ke dalam var z
print(z)
# kita print z nya maka hasilnya adalah 59


# fungsi tambah

def fungsi_tambah(angka_1,angka_2):
    # nah disini juga sama seperti di atas tapi ini argumen nya 2 dan nanti kita isi kedua 
    # argument tersebut
    '''fungsi return dengan multi input'''
    return angka_1 + angka_2
# lalu kita kembalikan hasilnya dengan operasi +

a = fungsi_tambah(10,8)
# kita masukan kedua argument nya yang mana berarti 10 + 8 = 18
# dan kita masukan ke dalam var a
print(a)
# lalu kita print variable nya

# jadi kesimpulan nya di bagian return juga bisa di tambahkan operasi

# fungsi dengan return banyak

def operasi_matematika(angka_1,angka_2):
    # nah ini sama function dengan 2 argument
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    # di atas adalah operasi aritmatika yang mana input nya nanti dari argument yang kita isi
# dan hasil dari operasi aritmatika di atas di masukan ke dalam var
    return tambah,kurang,kali,bagi
# lalu kita return masing masing variabel dengan operasi aritmatika di atas tadi

k,l,m,n = operasi_matematika(9,5)
# kita masukan fungsi nya ke 4 variabel yang mana mewakili badan fungsi di atas
# dari atas ke bawah k = tambah, l = kurang, m = kali, n = bagi

print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")
# Kita print dengan memanggil variable nya
