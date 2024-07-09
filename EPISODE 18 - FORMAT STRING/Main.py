# format string

# contoh generic
# string
nama = "ucup"
format_str = f"hello {nama}"
#di atas cara membaut string tanpa ada + + han jika ada var
#penulisan nya cukup pake f yg artinya format dan untuk mengisi var menggunalan {}
print(format_str)

# boolean
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
#nah contoh lain adalah angka yg mana kita tidak perlu mengkonversikan nya lagi 
#ke str seperti ini ( str(angka)) karena sudah otomatis di konversi, berlaku jg untuk boolean
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}" #nah untuk angka :d ini untuk menandakan bahwa var angka adalah bil bulat
print(format_str) #jadi harus pake data int kalo pake :d jika tidak akan error

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f"jutaan = {angka:,}"
#nah :, untuk biasanya menambahkan titik (.) atau koma (.) pada bilangan seperti ratusan, ribuan, dan jutaan
#yg mana akan otomatis terisi seperti di atas hasilnya adalah 2,000,000
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.3f}"
#:.3f untuk mengaambil angka di belakang koma, contoh nya di atas 3 angka di belakang koma
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:010.3f}"
#:010 untuk menambahkan ruang di awal angka. kalo 10 berarti ada 2 ruang/index
# karena di atas total setelah di ambil 3 angka di belakang koma ada 8 angka, nah 2 index tersebut jadi 00 karena 010.3f
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10.1234
format_minus = f"minus = {angka_minus:+d}" #+d untuk memunculkan tanda -/+
format_plus = f"plus = {angka_plus:+.2f}" # ini juga sama + nya untuk menampilkan +/- , tapi ini di tambahkan 2 angka di belakang koma

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}" #.% berfungsi menambahkan persen

print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5

format_string = f"harga total = Rp. {harga*jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)
# nah di atas untuk mengkonversi kan ke biner, octal, hexadecimal