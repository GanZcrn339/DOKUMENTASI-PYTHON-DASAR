# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >
print('========== lebih besar dari (>)')
hasil = a > 3
# variabel hasil ini nanti jika di print hasilnya adalah boolean true/false
#dalam kasus di atas var a yang = 4 apakah lebih besar dari 3, tentu lebih besar
#maka jawaban nya true
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

# kurang dari <
print('========== kurang dari (<)')
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# lebih dari sama dengan >=
print('========== lebih dari sama dengan(>=)')
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

# kurang dari sama dengan <=
print('======== kurang dari sama dengan(<=)')
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

# sama dengan (==)
print('======== sama dengan(==)')
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

# tidak sama dengan (!=)
print('======== sama dengan(!=)')
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

# 'is' sebagai komparasi object identity, jadi seperti yg kita tau
#bahwa sebenarnya tipe data itu adalah object, misalkan
# angka 5 adalah 
# int
# mempunyai tipe data, mempunyai id , mempunyai data data lainya yang masuk ke dalam class nya
print('======== object identity(is)')
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)
#Nah operator is ini berfungsi untuk membandingkan apakah object nya sama,
#jika sama maka nilai nya true, jika tidak maka false

#di atas contoh yang true dan di bawah contoh yang false

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)


#dibawah untuk is not sama saja membandingkan object tapi
#is not berfungsi untuk makesure bahwa suatu object tidak sama dengan object yang di bandingkan
print('======== object identity(is not)')
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)

#is untuk menanyakan apakah object ini sama dengan object yang dibandingkan
#is not menanyakan apakah object ini tidak sama dengan yang di bandingkan