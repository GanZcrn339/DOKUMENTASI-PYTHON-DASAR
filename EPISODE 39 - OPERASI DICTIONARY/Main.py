# operator dictionary

data_dict = {
	"cup":"ucup surucup",
	"tong":"otong surotong",
	"dung":"dudung surudung"
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")
#di atas adalah untuk mengecek panjang dictionary 
#Var LENDICT ditulis besar semua karena akan menjadi Const bukan VAR biasa
#yang bisa di ubah nilai nya

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")
#di atas adalah untuk mengecek apakah sebuah data ada pada dictionary

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan")) # cek key dengan message tidak ditemukan, sebelah key kis itu masage nya
#get berfungsi untuk membedakan data list dengan dictionary ketika akan mengambil data nya


# mengupdate/mengubah data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
#menambah data dictionary
data_dict["sep"] = "asep si kasyep"
print(data_dict)

#dibawah cara yang lebih tepat untuk dictionary
data_dict.update({"cup":"ucup surucup"})
print(data_dict)
data_dict.update({"faqih":"faqihza si kweren"}) # kalau gak ada diadd ajah
print(data_dict)

# mendelete data pada dictionary
del data_dict["faqih"]
print(data_dict)