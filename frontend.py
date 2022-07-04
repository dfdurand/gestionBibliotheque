from tkinter import *
from tkinter import ttk
import backend


def affichage():
    vue.delete(0, END)
    for row in backend.afficher():
        vue.insert(END, row)


def cherche():
    vue.delete(0, END)
    for row in backend.chercher(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        vue.insert(END, row)


def ajoute():
    vue.delete(0, END)
    backend.ajouter(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    vue.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


def supprime():
    pass


def ferme():
    pass


def modifie():
    pass


win = Tk()


win.title(" LIBRAIRIE ")
win.config(background="#869e9e")
style = ttk.Style()
style.theme_use("classic")
style.configure("TButton", foreground="green", font=("Helvetica", 10, "bold italic"))
style.configure("Tlabel", fg="blue")


#def show():
   # label.insert(END, vue.get())
    #vue.delete(0, END)

# 4 variables


title_text = StringVar()
author_text = StringVar()
year_text = StringVar()
isbn_text = StringVar()


# 6 boutons..


va = ttk.Button(win, text="Tout", width=15, command=affichage)
va.grid(row=2, column=3, pady=5)
se = ttk.Button(win, text="Chercher", width=15, command=cherche)
se.grid(row=3, column=3, pady=5)
ae = ttk.Button(win, text="Ajouter", width=15, command=ajoute)
ae.grid(row=4, column=3, pady=5)
us = ttk.Button(win, text="Modifier", width=15, command=modifie)
us.grid(row=5, column=3, pady=5)
ds = ttk.Button(win, text="Supprimer", width=15, command=supprime)
ds.grid(row=6, column=3, pady=5)
cls = ttk.Button(win, text="Fermer", width=15, command=ferme)
cls.grid(row=7, column=3, pady=5)


# 4 entrees

title = Entry(win, width=35, textvariable=title_text)
title.grid(row=0, column=1, pady=5)
autor = Entry(win, width=40, textvariable=author_text)
autor.grid(row=0, column=3, pady=5)
year = Entry(win, width=35, textvariable=year_text)
year.grid(row=1, column=1, pady=5)
isbn = Entry(win, width=40, textvariable=isbn_text)
isbn.grid(row=1, column=3, pady=5)

# 4 label..

label = ttk.Label(win, text="TITLE")
label.grid(row=0, column=0)
label1 = ttk.Label(win,  text="AUTHOR")
label1.grid(row=0, column=2)
label2 = ttk.Label(win,  text="YEAR")
label2.grid(row=1, column=0)
label3 = ttk.Label(win, text="ISBN  ")
label3.grid(row=1, column=2)

# liste

vue = Listbox(win, width=40, height=10)
vue.grid(row=2, column=0, columnspan=2, rowspan=6)

sb = Scrollbar(win)
sb.grid(row=3, column=2, rowspan=6)

vue.configure(yscrollcommand=sb.set)
sb.configure(command=vue.yview)

win.mainloop()