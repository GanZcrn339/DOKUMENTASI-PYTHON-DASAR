# 1. mode write

# dia akan membuat file baru jika tidak ada,
# lalu akan menimpa atau overwrite isinya

with open("data_1.txt",'w',encoding="utf-8") as file: #encoding="utf-8"
    file.write("jon si jhonny")
    #nah di atas adalah cara membuat teks file dan menulis nya

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("ucup surucup")
    #akan di timpa jika kita membuat nya lagi

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("overwrite")

    #nah di atas akan meng overwite file nya

# 2. mode append
#ini untuk nambah teks pada file yang sama

with open("data_2.txt",'w',encoding="utf-8") as file:
    file.write("jon si jhonny\n")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("ucup surucup\n")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("tambah lagi dengan append\n")

# 3. mode r+
#akan di timpa teks nya

with open("data_3.txt",'w',encoding="utf-8") as file:
    file.write("data ke 3\n")

with open("data_3.txt",'r+',encoding="utf-8") as file:
    file.write("baris-1 \n")
    file.write("baris-2 \n")
    file.write("baris-3 \n")

with open("data_3.txt",'r+',encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_3.txt",'r+',encoding="utf-8") as file:
    file.write("otong") # menimpa isi text sesuai dengan panjang data