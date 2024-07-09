# episode operator bitwise, operasi biner, binary
#Operator BItwise ini harus langsung liat videon nya di kelas terbuka episode 13
a = 9
b = 5

# bitwise OR (|)
c = a | b
print('\n=========OR=========')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('----------------------------- (|)')
print('nilai :',c,' , binary :',format(c,'08b'))
#function format ini berfungsi untuk mengubah nilai nya menjadi biner 08 adalah 8 angka biner dan b nya adalah biner


# bitwise AND (&)
#khusus ini harus liat video nya juga
c = a & b
print('\n=========AND========')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('----------------------------- (&)')
print('nilai :',c,' , binary :',format(c,'08b'))

# bitwise XOR (^)
c = a ^ b
print('\n=========XOR========')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('----------------------------- (^)')
print('nilai :',c,' , binary :',format(c,'08b'))

# bitwise NOT (~)
c = ~a
print('\n=========NOT========')
print('nilai :',a,' , binary :',format(a,'08b'))
print('----------------------------- (~)')
print('nilai :',c,' , binary :',format(c,'08b'))
print('----------------------------- (^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :',e^d,' , binary :',format(e^d,'08b'))

# shifting

# shift right (>>)
c = a >> 2
print('\n=========>>=========')
print('nilai :',a,' , binary :',format(a,'08b'))
print('----------------------------- (>>)')
print('nilai :',c,' , binary :',format(c,'08b'))

# shift left (<<)
c = a << 2
print('\n=========<<=========')
print('nilai :',a,' , binary :',format(a,'08b'))
print('----------------------------- (<<)')
print('nilai :',c,' , binary :',format(c,'08b'))

#operator shift adalah untuk menggeser ke kiri atau kekanan sebuah hasil
