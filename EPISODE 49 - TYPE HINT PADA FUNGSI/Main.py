''' Type hints untuk fungsi '''

# bentuk standar fungsi yang udah kita pelajari

'''
studi kasus
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(1)
fungsi("Ucup")
fungsi(True)
'''

# penggunaan type hints

import string

def sepuluh_pangkat(argument:int) -> int: 
    # nah jadi type hint itu adalah seperti const tapi untuk
    # menentukan tipe data dari input dan output argument fungsi
    '''FUNGSI DENGAN HINTS'''
    output = 10**argument
    return output
# di atas input argument nya harus int dan output nya juga integer

HASIL = sepuluh_pangkat(4)
# kita masukan input argument int di atas ke cont hasil
print(HASIL)
# lalu kita print hasil nya

def display(argument:string):
    print(argument)
    # ini juga sama tapi type hint nya input string

display("Ucup")
# maka input nya harus string tidak boleh yang lain