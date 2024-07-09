# looping dictionary

teman_teman = {
	"cup":"ucup surucup",
	"tong":"otong surotong",
	"dung":"dudung surudung",
	"sep":"asep si kasyep",
	"cuy":"ucuy surucuy"
}

# looping first try (yang keluar adalah keynya)

for teman in teman_teman:
	print(teman)
#nah jadi ketika run looping dictionary di atas yang menggunakan for,
#yang keluar nya hanya key nya saja

# operator untuk mengambil item / iterables
keys = teman_teman.keys()
print(keys)
#di atas yang keluar hanya key nya saja

for key in teman_teman.keys():
	print(teman_teman.get(key))
	#jika ingin value nya juga keluar harus menggunakan get seperti di atas

values = teman_teman.values()
print(values)
#nah kalo di atas values nya aja yang keluar tapi masih dalam bentuk mentah 
#yang mana masih ikut kurung kurung nya

for value in teman_teman.values():
	print(value)
	#nah kalo mau hasil matang nya, gunakan for seperti di atas

items = teman_teman.items()
print(items)

for item in teman_teman.items():
	print(item)
	#nah kalo mau keluar key sama value nya bisa menggunakan method items

for key,value in teman_teman.items():
	print(f"key = {key}, value = {value}")
	#nah di atas untuk lebih rapih nya