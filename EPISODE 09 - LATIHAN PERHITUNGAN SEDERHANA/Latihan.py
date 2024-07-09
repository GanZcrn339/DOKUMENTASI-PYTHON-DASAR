print("\nPROGRAM KONVERSI TEMPERATUR\n")

# TUGAS
# 1.MENGKONVERSI FAHREINHEIT KE KELVIN
# 2. MENGKONVERSI KELVIN KE FAHREINHEIT

Fahreinheit = float(input('Masukan suhu dalam Fahreinheit : '))
print("suhu adalah",Fahreinheit, "Fahreinheit")

kelvin = (Fahreinheit+459.67)*5/4 
print("suhu dalam kelvin adalah",kelvin, "Kelvin")

kelvin_ke_fahreinheit = 9/5 * (kelvin - 273) +32
print("suhu dalam fahrenheit dari Kelvin adalah ",kelvin_ke_fahreinheit, "Fahrenheit")



