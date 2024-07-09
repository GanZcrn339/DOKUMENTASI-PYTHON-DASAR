# copy dictionary

teman_teman = {
	"cup":"ucup surucup",
	"tong":"otong surotong",
	"dung":"dudung surudung",
	"sep":"asep si kasyep",
	"cuy":"ucuy surucuy"
}

friends = teman_teman.copy()
# Disini kita akan mengcopy dictionary teman-teman ke dalam var friend

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")
#nah jadi var friend juga isi nya sama kyk teman_teman

teman_teman["cup"]="ucup si kweren"
# disini kita update/ubah value dari cup yang ada di dictionary teman_teman
print(f"teman-teman: {teman_teman}\n")
# nah jika kita print dictionary teman_teman maka value dari key "cup" akan berubah sesuai yang diatas
print(f"friends: {friends}\n")
# tapi jika kita print friend maka akan sama dengan dictionary teman_teman sebelum di ubah
# yaitu key "cup" nya bervalue "ucup surucup"

# pop dictionary (berdasarkan key)
dataAsep = friends.pop("sep")
# untuk mem pop kita harus masukan dictinary nya ke dalam var lagi
print(f"data asep = {dataAsep}\n")
print(f"friends = {friends}\n")
# nah ketika di pop, dan di print, print pertama yaitu data asep akan keluar values nya
#tapi di frined, sep akan menghilang, jadi kyk di transfer gitu ke print nan
#print(f"data asep = {dataAsep}\n")

# popitem dictionary (yang terakhir ajah)
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")
# nah di atas hasil nya sama tapi karena items yang keluar nya key dan values nya