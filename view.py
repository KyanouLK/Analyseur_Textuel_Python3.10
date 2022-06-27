import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog, ttk
import new_nuage as nn

fenetre = tk.Tk()
fenetre.geometry("310x150")
fenetre.title("Analyseur de Texte")

def chooseFile():
    try:
        fileName = filedialog.askopenfilename(filetypes=[("Texte File", "*.txt")])
        print(fileName)

        firstpart = nn.first_part_file(fileName)
        lastpart = nn.last_part_file(fileName)

        traitement_fp = []
        traitement_lp = []

        match type_sortie.get():
            case 'Noms':
                traitement_fp = nn.return_nouns(firstpart)
                traitement_lp = nn.return_nouns(lastpart)
            case 'Verbes':
                traitement_fp = nn.return_verbs(firstpart)
                traitement_lp = nn.return_verbs(lastpart)
            case _:
                traitement_fp = nn.return_token(firstpart)
                traitement_lp = nn.return_token(lastpart)
            

        clean1_fp = nn.cleaner(traitement_fp, nn.stopWords)
        clean2_fp = nn.cleaner(clean1_fp, nn.stoppeur)
        clean3_fp = nn.cleaner(clean2_fp, nn.last_stopwords)

        clean1_lp = nn.cleaner(traitement_lp, nn.stopWords)
        clean2_lp = nn.cleaner(clean1_lp, nn.stoppeur)
        clean3_lp = nn.cleaner(clean2_lp, nn.last_stopwords)

        filefp = "Texte/firstpart.txt"
        filelp = "Texte/lastpart.txt"

        nn.writer(filefp, clean3_fp)
        nn.writer(filelp, clean3_lp)

        r1 = nn.reader(filefp)
        r2 = nn.reader(filelp)

        nn.cloud_creator(r1, r2, int(nb_mots.get()), format_nuage.get(), forme_mots.get())
    
    except ValueError:
        tkinter.messagebox.showerror(
            'Erreur',
            f'Il y a un erreur dans les paramètres'
        )

# fenetre.rowconfigure(0, weight=1)
# fenetre.columnconfigure(0, weight=1)

tk.Label(text="Choisissez vos paramètres ci-dessous").grid(row=0, columnspan=2)

tk.Label(text="Nombre de mots maximum : ").grid(row=1, column=0)
nb_mots = tk.Entry()
nb_mots.insert(0,100)
nb_mots.grid(row=1, column=1)

tk.Label(text="Type de sortie : ").grid(row=2, column=0)
liste_sortie = ["Tout", "Noms", "Verbes"]
type_sortie = ttk.Combobox(fenetre, values=liste_sortie)
type_sortie.current(0)
type_sortie.grid(row=2, column=1)

tk.Label(text="Forme du nuage : ").grid(row=3, column=0)
liste_nuage = ["None", "feuille", "heart", "Papillion", "twitter"]
format_nuage = ttk.Combobox(fenetre, values=liste_nuage)
format_nuage.current(0)
format_nuage.grid(row=3, column=1)

tk.Label(text="Format des mots : ").grid(row=4, column=0)
liste_text = ["None", "HeyComic"]
forme_mots = ttk.Combobox(fenetre, values=liste_text)
forme_mots.current(0)
forme_mots.grid(row=4, column=1)

tk.Button(text="Choisir votre fichier txt", command=chooseFile).grid(columnspan=2)

fenetre.mainloop()