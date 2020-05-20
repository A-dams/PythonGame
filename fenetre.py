from tkinter import *
import tkinter as tk


def affiche(i):
    F1 = Toplevel()
    logo = Label(F1, image=i)
    logo.pack()
    Button(F1)

# On crée une fenêtre, racine de notre interface
fen1 = Tk()
fen_photo = tk.Tk()

photo = tk.PhotoImage(file='spongebob.png')
img = tk.Label(fen_photo, image=photo)


# On crée un label (ligne de texte) souhaitant la bienvenue
champ_score = Label(fen1, text="SCORE")
champ_p1 = Label(fen1, text="Player 1")
champ_p2 = Label(fen1, text="Player 2")
champ_p3 = Label(fen1, text="Player 3")


Button(fen1, text='Quitter', command=fen1.destroy).pack()

#fen1.maxsize(width=500,height=500)

# On affiche ce qu'on "pack" dans la fenetre
champ_score.pack()
champ_p1.pack()
champ_p2.pack()
champ_p3.pack()
img.pack()



# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fen1.mainloop()
