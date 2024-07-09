# list -> array, mengakses dengan 
# menggunakan index

data_list = ['ucup','otong','dudung']

print(data_list[0])

# dictionary (dict) -> associative array
# identifier -> key

data_dict = {
	'key':'value',
	'cp':'ucup',
	'tg':'otong',
	'dg':'dudung',
	'nmbr':100,
	'list':data_list,
} #dictionary sama dengan objek di b pemrograman lain
#yang isi nya ada key dan value
#bisa di ibaratkan jika di list key ini index nya , value adalah data nya

print(data_dict['tg'])
print(data_dict['nmbr'])
print(data_dict['list'])