from tkinter import *
import random

master = Tk()

master.title("Güvenli Şifre Oluştur")
canvas = Canvas (master, height=150, width=300)
canvas.pack()

frame_orta = Frame(master)
frame_orta.place(relx=0.20, rely=0.20)

def sifre():
    upper = "ABCDEFGHIJKLMNOPRQTUWXVYZ"
    lower = "abcdefghijklmnoprqtuwxvyz"
    number = "1234567890"
    shape = "><!'^+%&/?*"

    _all = upper+ lower+ number + shape
    lenght = 16

    sifre_olustur = "".join(random.sample(_all, lenght))
    metin_alani = Text(frame_orta, height = 2, width= 16)
    metin_alani.tag_configure("style", foreground="black", font=("Arial", 10, "bold"))
    metin_alani.pack(anchor=E)
    metin_alani.insert(END, sifre_olustur,"style")


olustur_butonu= Button(frame_orta, text="Şifre Oluştur", command= sifre, activebackground="yellow")
olustur_butonu.pack(anchor=W)


master.mainloop()