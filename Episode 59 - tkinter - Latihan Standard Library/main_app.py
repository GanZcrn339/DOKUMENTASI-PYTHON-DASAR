# GUI -> Graphical User Interface

#tkinter sebuah library yang berfungsi untuk membuat
#sebuah program dengan GUI, Jadi kita kyk bikin aplikasi 
#dari windows

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
#

# Init
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Sapa Dia!")

# Variabel dan Fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    '''fungsi ini akan dipanggil oleh tombol'''
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Ganteeeng!"
    showinfo(title="Whazzup!",message=pesan)

# frame input
input_frame = ttk.Frame(window)
# penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen-komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan:")
nama_depan_label.pack(padx=10,fill="x",expand=True)
# 2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)
# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama belakang:")
nama_belakang_label.pack(padx=10,fill="x",expand=True)
# 4. entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)
# 5. Tombol
tombol_sapa = ttk.Button(input_frame,text="Sapa!",command=tombol_click)
tombol_sapa.pack(fill='x',expand=True,padx=10,pady=10)

#nah di atas kita buat label dan input, yang mana input nya di ambil di variabel di atas,
#selain itu kita juga membuat tfunc tombol dan kita gunakan juga di tk nya, selain itu
#untuk hasilnya input nya kita tampilkan di func showinfo yang diambil dari library tkinter juga

# Main Loop window
#jadi akan terus nge loop jika kita tidak close program nya
window.mainloop()