data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote(Kutip satu) '...'
    2. dengan menggunakan double quote(kutip dua) "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
#jika seperti di atas, kutip dua nya akan ditampilkan jadi string
print("'Halo, apa kabar?'")
#nah kalo di atas kutip satu nya yg jadi string
print("ini adalah hari jum'at") #nah di samping jum'at ,tanda kutip nya jadi string
#intinya, kutip dua atau kutip satu yg di dalam akan ikut jadi string

# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')
#nah jika kita menggunakan tanda kutip 1 atau 2 sebagai tanda untuk string, dan kita ingin menggunakan
# tanda kutip yg sama di dalam string nya, maka harus menggunakan backslah sebekum tanda kutip nya supaya
#bisa dianggap string

# backlash
# jika kita ingin menggunakan backslash di string seperti ini print("C:\\user\\Ucup")
# maka harus menggunakan double backslash supaya di anggap string, contoh nya di bawah ini
print("C:\\user\\Ucup")


# tab
print("ucup\t\t\totong, semakin jauhan")
#nah di atas untuk tab atau spasi jauh

# backspace
print("ucup \botong, jadi deketan")
#untuk menghapus , lgsg print saja untuk meliaht contoh nya


# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR -> carriage return -> commodore, acorn, lisp 
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows
#untuk newline di windows kita menggunakan CRLF


# 3. String literal atau raw

# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')
#jika kita menggunakan r di awal penulsian string seperti di atas,
#maka hasilnya akan di anggap string semua

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD   
""")
#nah di atas untuk multine jadi gak perlu pake newline CRLF lagi untuk newline
#nah kita pake kutip 3

# multiline literal string dan RAW
print(r"""
Nama : Ucup
Kelas : 3 SD\new normal 
Website : www.ucup.com/newID
""")
#nah di atas gabungan multiline dan raw string
