from tkinter import *

def fen_jeu():
    global fen1
    F1 = Toplevel()
    F1.geometry("450x450")
    F1.title("Fenetre Jeu")
    frameBgTop = Frame(F1, width=450, height=450).pack()
    topBg = PhotoImage(file="dbzBG.png")
    labeltop = Label(frameBgTop, image=topBg).pack()




# On crée une fenêtre, racine de notre interface
fen1 = Tk()
fen1.maxsize(width=720,height=720)
#fen1.geometry("500x500")


photo = PhotoImage(file='goku.png')
img = Label(fen1, image=photo)
file = open('scores.txt', "r")
lines = file.readlines()




champ_score = Label(fen1, text="SCORE")

champ_p1 = Label(fen1, text=lines[0])
champ_p2 = Label(fen1, text=lines[1])
champ_p3 = Label(fen1, text=lines[2])

saisie_player_name = StringVar()



# On affiche ce qu'on "pack" dans la fenetre
img.pack(side="left", expand=1, anchor="nw")
champ_score.pack()
#Top 3 joueurs
champ_p1.pack()
champ_p2.pack()
champ_p3.pack()

Label(fen1, text="Name : ", width=10, fg="blue").pack()
Entry(textvariable=saisie_player_name, width=10).pack()

Button(fen1, text='Play', command=fen_jeu).pack()

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fen1.mainloop()
