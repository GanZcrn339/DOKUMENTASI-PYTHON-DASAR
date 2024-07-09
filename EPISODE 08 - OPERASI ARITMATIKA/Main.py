# operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)

# operasi pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)

# operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

# operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
#perpangkatan lambang nya bintang 2 seperti di atas
print(a,'**',b,'=',hasil)

# operasi modulus %
#modulus adalah sisa bagi
hasil = a % b
print(a,'%',b,'=',hasil)

# operasi floor division // pembagian yang hasilnya di bulatkan ke bawah
hasil = a // b
print(a,'//',b,'=',hasil)
#mksd nya adalah jika ada angka di belakang koma maka hasilnya akan di bulatkan ke bawah

# prioritas operasi, operational precedence
'''
    1. ()
    2. exponen **
    3. perkalian dan teman-teman * / ** % //
    4. pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)
# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z 
print('(',x,'+',y,') *',z,'=',hasil)