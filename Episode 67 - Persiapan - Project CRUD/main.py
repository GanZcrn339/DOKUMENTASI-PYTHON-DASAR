import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name
    
    while(True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
            #kode di atas untuk membuat tampilan terminal nya bersih
        
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("=========================")
        #kita buat pembukaan nya seperti di atas

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")
        #kita buat tampilan list CRUD Yang akan di buat

        user_option = input("Masukan opsi: ")
        #kita buat input nya

        print("\n=========================\n")

        match user_option:
            case "1": print("Read Data")
            case "2": print("Create Data")
            case "3": print("Update Data")
            case "4": print("Delete Data")
            #kita buat case, case mirip dengan switch di bahasa javascripts
            #jadi ada pilhan 1-4 sesuai list dan akan di print juga teks nya sesuai list

        print("\n=========================\n")
        is_done = input("Apakah Selesai (y/n)? ")
        if is_done == "y" or is_done == "Y":
            #kode di atas untuk menanyakan kembali apakah kita sudah selesai,
            #jika belum maka kita akan menginput daftar case di atas, jika selesai
            #maka program akan berakhir
            break

    print("Program Berakhir, Terima Kasiih KAKAAAAA")