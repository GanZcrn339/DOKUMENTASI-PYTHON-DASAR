# operasi logika atau boolean

# not, or, and, xor

# NOT
print('====NOT====')
#NOT sama dengan Negasi jadi kebalikan hasil variabel
# karena disini variabel isi nya a = false
# terus si var a di not a kan dan dimasukan ke var c, 
# maka var c hasilnya akan True jika di print
a = False
c = not a
print('data a =',a)
print('-------------- NOT')
print('data c =',c)

# OR (jika salah satu true, maka hasilnya adalah true)
print('====OR====')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
#Contoh Pertama di atas karena dua variabel a dan b isi nya false, maka hasilnya false
a = False
b = True
c = a or b
print(a,'OR',b,' =',c)
#Nah jika salah satu nya true seperti di atas maka hasilnya true
a = True
b = False
c = a or b
print(a,' OR',b,'=',c)
a = True
b = True
c = a or b
print(a,' OR',b,' =',c)
#begitu pun 2 contoh di atas

# AND (jika dua buah nilai true, maka hasil true)
print('====AND====')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = True
b = False
c = a and b
print(a,' AND',b,'=',c)
a = True
b = True
c = a and b
print(a,' AND',b,' =',c)
#Nah and ini keduanya harus bernilai true, jika salah satu false maka hasilnya akan false

# XOR (akan true jika salah satu true, sisanya false)
print('====XOR====')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = False
c = a ^ b
print(a,' XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,' XOR',b,' =',c)
#Nah jadi jika hasilnya akan true jika kedua variabel pembanding nya berbeda,
#mksd nya adalah harus false dan true untuk mendapatkan hasil true,
#jika dua dua nya true atau false maka hasilnya akan false