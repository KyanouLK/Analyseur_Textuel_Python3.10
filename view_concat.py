import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog, ttk
import os
import concat

fenetre = tk.Tk()
fenetre.geometry("310x190")
fenetre.title("Concateneur")

tabFiles = []

def openAllFiles():
    name = filedialog.askopenfilenames(filetypes=[("Texte File", "*.txt")])
    global tabFiles
    tabFiles = name

def concatAll():
    try:
        global tabFiles
        concat.concatenation(tabFiles, nom_sortie.get())
        tkinter.messagebox.showinfo(
            'Succès',
            f'La concaténation a bien été réalisé'
        )
    except ValueError:
        tkinter.messagebox.showerror(
            'Erreur',
            f'Un ou plusieurs fichier(s) sélectionné(s) n\'est pas traitable.'
        )

tk.Button(text="Choix premier fichier", command=openAllFiles).grid(row=0, column=0)

tk.Label(text="Nom fichier sortie : ").grid(row=1, column=0)
nom_sortie = tk.Entry()
nom_sortie.insert(0,"Concatenation")
nom_sortie.grid(row=1, column=1)

tk.Button(text="Concatener", command=concatAll).grid(row=2, column=0)

fenetre.mainloop()