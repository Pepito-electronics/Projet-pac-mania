import tkinter
import random
import pickle


class Obstacles(object):
    global level

    def __init__(self):
        pass

    def creation_plateau0(self):
        for r in rectangles0:
            rect.append(plato.create_rectangle(r[0], r[1], r[2], r[3], outline=ob_coul, fill=backG, width=3))

    def creation_plateau1(self):
        for r in rectangles1:
            rect.append(plato.create_rectangle(r[0], r[1], r[2], r[3], outline=ob_coul, fill=backG, width=3))

    def creation_plateau(self):
        if level == 0:
            Obstacles.creation_plateau0(self)
        elif level == 1:
            Obstacles.creation_plateau1(self)


class Gost(object):

    def __init__(self):
        # tkinter.Canvas.__init__(self)
        self.gt = plato.create_oval(cg0, cg1, cg2, cg3, fill=ob_coul)
        self.dpx = 30
        self.dpy = 0
        self.last_after = None
        """self.direction = 0
        self.direction = 0"""

    def dodge_obstacle(self):
        coord_gt = plato.bbox(self.gt)
        for r in rect:
            dpl = 'notOK'
            while dpl == 'notOK':
                cor = plato.bbox(r)
                cog = [coord_gt[0] + self.dpx, coord_gt[1] + self.dpy, coord_gt[2] + self.dpx, coord_gt[3] + self.dpy]
                if cor[0] < cog[0] < cor[2] and cor[1] < cog[1] < cor[3] or \
                                                cor[0] < cog[0] < cor[2] and cor[1] < cog[3] < cor[3] or \
                                                cor[0] < cog[2] < cor[2] and cor[1] < cog[1] < cor[3] or \
                                                cor[0] < cog[2] < cor[2] and cor[1] < cog[3] < cor[3] or \
                                cog[0] < 0 or cog[2] > wc or cog[1] < 0 or cog[3] > hc:
                    if not (random.randint(0, 8)):
                        self.dpx *= -1
                        self.dpy *= -1
                    else:
                        if random.randint(0, 1):
                            self.dpx, self.dpy = self.dpy, self.dpx
                        else:
                            self.dpx, self.dpy = -self.dpy, -self.dpx
                else:
                    dpl = 'OK'
        plato.move(self.gt, self.dpx, self.dpy)
        if flag == 1:
            if self.last_after == None:
                self.last_after = fen_j.after(dt, self.dodge_obstacle)
                last_after.append(self.last_after)
            else:
                last_after.remove(self.last_after)
                self.last_after = fen_j.after(dt, self.dodge_obstacle)
                last_after.append(self.last_after)

    def move_gost(self):
        self.dodge_obstacle()


class Pac(object):  # tkinter.Canvas):
    def __init__(self):
        # tkinter.Canvas.__init__(self)
        self.G = 0
        self.D = wc
        self.H = 0
        self.B = hc
        self.pacMan = plato.create_oval(cp0, cp1, cp2, cp3, fill="yellow")
        self.last_after = None

    def gagne(self):
        global flag, FANT1
        flag = 0
        plato.delete('all')
        FANT1 = tkinter.Canvas(fen_j, width=200, height=200, background="black", highlightcolor="black")
        FANT1.grid(row=4, column=2)
        FANT1.create_rectangle(20, 10, 180, 170, fill='Blue', outline='white')
        FANT1.create_rectangle(10, 170, 30, 190, fill='blue', outline='white')
        FANT1.create_rectangle(50, 170, 70, 190, fill='blue', outline='white')
        FANT1.create_rectangle(90, 170, 110, 190, fill='blue', outline='white')
        FANT1.create_rectangle(130, 170, 150, 190, fill='blue', outline='white')
        FANT1.create_rectangle(170, 170, 190, 190, fill='blue', outline='white')
        FANT1.create_rectangle(40, 20, 50, 40, fill='red', width=0)
        FANT1.create_rectangle(30, 25, 60, 35, fill='red', width=0)
        FANT1.create_rectangle(140, 20, 150, 40, fill='red', width=0)
        FANT1.create_rectangle(130, 25, 160, 35, fill='red', width=0)
        win = tkinter.Label(fen_j, text=("VOUS AVEZ GAGNEZ!!!!\n" + "BIEN JOUER!\n" + "Votre score est %i" % points),
                            font=("comic", 20))
        win.configure(bg='green', fg='white')
        win.grid(row=4, column=2)

    def perdu(self):
        global flag, FANT1, lose
        flag = 0
        plato.delete('all')
        FANT1 = tkinter.Canvas(fen_j, width=200, height=200, background="black", highlightcolor="black")
        FANT1.grid(row=4, column=2)
        FANT1.create_rectangle(20, 10, 180, 170, fill='Blue', outline='white')
        FANT1.create_rectangle(10, 170, 30, 190, fill='blue', outline='white')
        FANT1.create_rectangle(50, 170, 70, 190, fill='blue', outline='white')
        FANT1.create_rectangle(90, 170, 110, 190, fill='blue', outline='white')
        FANT1.create_rectangle(130, 170, 150, 190, fill='blue', outline='white')
        FANT1.create_rectangle(170, 170, 190, 190, fill='blue', outline='white')
        FANT1.create_rectangle(40, 20, 50, 40, fill='red', width=0)
        FANT1.create_rectangle(30, 25, 60, 35, fill='red', width=0)
        FANT1.create_rectangle(140, 20, 150, 40, fill='red', width=0)
        FANT1.create_rectangle(130, 25, 160, 35, fill='red', width=0)
        # FANT1.create_polygon(60,10,18,53,20,50,85,20, fill='green')
        lose = tkinter.Label(fen_j, text=("VOUS AVEZ PERDU HAHAHA"), font=("comic", 20))
        lose.configure(bg='green', fg='white')
        lose.grid(row=4, column=2)

    def move_pac(self):
        global flag, dx, dy, points, hs, vies
        if len(frofro) <= 227:
            self.gagne()
        else:
            coord_pac = plato.bbox(self.pacMan)
            col1 = plato.bbox(fantome1.gt)
            col2 = plato.bbox(fantome2.gt)
            col3 = plato.bbox(fantome3.gt)
            col4 = plato.bbox(fantome4.gt)
            col5 = plato.bbox(fantome5.gt)
            colf = [col1, col2, col3, col4, col5]
            for f in colf:
                if f[0] <= coord_pac[0] <= f[2] and f[1] <= coord_pac[1] <= f[3] or \
                                                f[0] <= coord_pac[0] <= f[2] and f[1] <= coord_pac[3] <= f[3] or \
                                                f[0] <= coord_pac[2] <= f[2] and f[1] <= coord_pac[1] <= f[3] or \
                                                f[0] <= coord_pac[2] <= f[2] and f[1] <= coord_pac[3] <= f[3]:
                    if vies < 1:
                        self.perdu()
                    else:
                        back_to_spawn()
                    vies -= 1

            for r in rect:
                cor = plato.bbox(r)
                cop = [coord_pac[0] + dx, coord_pac[1] + dy, coord_pac[2] + dx, coord_pac[3] + dy]
                if cor[0] < cop[0] < cor[2] and cor[1] < cop[1] < cor[3] or \
                                                cor[0] < cop[0] < cor[2] and cor[1] < cop[3] < cor[3] or \
                                                cor[0] < cop[2] < cor[2] and cor[1] < cop[1] < cor[3] or \
                                                cor[0] < cop[2] < cor[2] and cor[1] < cop[3] < cor[3] or \
                                cop[0] < 0 or cop[2] > wc or cop[1] < 0 or cop[3] > hc:
                    dx, dy = 0, 0
            for e in frofro:
                cof = plato.bbox(e)
                if coord_pac[0] < cof[0] < coord_pac[2] and coord_pac[1] < cof[1] < coord_pac[3] or \
                                                coord_pac[0] < cof[0] < coord_pac[2] and coord_pac[1] < cof[3] < \
                                coord_pac[3] or \
                                                coord_pac[0] < cof[2] < coord_pac[2] and coord_pac[1] < cof[1] < \
                                coord_pac[3] or \
                                                coord_pac[0] < cof[2] < coord_pac[2] and coord_pac[1] < cof[3] < \
                                coord_pac[3]:
                    plato.delete(e)
                    frofro.remove(e)
                    points += 100
                    score_player1.set("%i" % points)
            plato.move(self.pacMan, dx, dy)
            if flag == 1:
                if self.last_after == None:
                    self.last_after = fen_j.after(dt, self.move_pac)
                    last_after.append(self.last_after)
                else:
                    last_after.remove(self.last_after)
                    self.last_after = fen_j.after(dt, self.move_pac)
                    last_after.append(self.last_after)

                    # fen_j.after(dt, self.move_pac)


def fromages():
    xx = 15
    yy = 15
    while yy < 600:
        if xx < 600:
            frofro.append(plato.create_oval(xx, yy, xx, yy, outline=ob_coul, width=5))
            xx += 30
        elif xx > 600:
            yy += 30
            xx = 15


def key(event):
    global dx, dy, flag
    if event.keysym == 'Return':
        name()
    if event.keysym == 'Left':
        dx = -30
        dy = 0
    if event.keysym == 'Right':
        dx = 30
        dy = 0
    if event.keysym == 'Up':
        dx = 0
        dy = -30
    if event.keysym == 'Down':
        dx = 0
        dy = 30
    if event.keysym == 'space':
        dx = 0
        dy = 0
        if flag == 0:
            flag = 1
            texte05.configure(text='PRESS SPACE FOR PAUSE', font=("comic", 18))
            pac_man.move_pac()
            fantome1.move_gost()
            fantome2.move_gost()
            fantome3.move_gost()
            fantome4.move_gost()
            fantome5.move_gost()

        elif flag == 1:
            texte05.configure(text='PRESS SPACE FOR START/RESUME', font=("comic", 18))
            flag = 0


def helpMe():
    global aide, aide2
    aide2.grid(row=8, column=2)
    aide.grid(row=7, column=2, sticky='E')


def new_game():
    """question prof --> devient non type"""
    global pac_man, fantome1, fantome2, fantome3, fantome4, fantome5, flag, rect, frofro
    global rectangles, points, WIN, vies
    texte05.configure(text='PRESS SPACE FOR START/RESUME', font=("comic", 18))
    flag = 0
    points = 0
    score_player1.set("%i" % points)
    plato.delete('all')
    for la in last_after:
        fen_j.after_cancel(la)
    FANT1.destroy()
    lose.destroy()
    rect = []
    frofro = []
    vies = 2
    plato1_0 = Obstacles()
    fromages()
    fantome1 = Gost()
    fantome2 = Gost()
    fantome3 = Gost()
    fantome4 = Gost()
    fantome5 = Gost()
    Obstacles.creation_plateau(plato1_0)

    pac_man = Pac()

def back_to_spawn():
    global cp0,cp1,cp2,cp3
    global pac_man, flag
    flag = 0
    texte05.configure(text='PRESS SPACE FOR START/RESUME', font=("comic", 18))
    plato.delete(pac_man.pacMan)
    cp0 = (wc / 40) + (11 * wc / 20) - 10
    cp1 = (hc / 40) + (8 * hc / 20) - 10
    cp2 = (wc / 40) + (11 * wc / 20) + 10
    cp3 = (hc / 40) + (8 * hc / 20) + 10
    pac_man = Pac()
    pac_man.move_pac()

def revel():
    b3.grid(row=5, column=1, padx=10, sticky='E')
    b4.grid(row=5, column=2, padx=0)
    mb.grid(row=5, column=3, padx=0, sticky='W')
    b6.grid(row=6, column=3, padx=40, pady=30, sticky='W')


def cacher():
    b3.grid_forget()
    b4.grid_forget()
    mb.grid_forget()
    b6.grid_forget()
    aide.grid_forget()
    aide2.grid_forget()


def changer_coul():
    global backG
    global num_coul
    global num_coul_ob
    global ob_coul
    if num_coul == 6:
        num_coul = 0
        num_coul_ob = 3
    elif num_coul == 2:
        num_coul += 1
        num_coul_ob = 0
    else:
        num_coul += 1
        num_coul_ob = 3
    backG = couleurs[num_coul]
    ob_coul = couleurs[num_coul_ob]
    fen_a.configure(bg=backG)
    texte1.configure(bg=backG)
    print(backG)
    print(ob_coul)


def name():
    global nom_j
    nom_j = entree1.get()


def setlvlsauv():
    f = open('file.txt', 'rb')
    p = pickle.load(f)
    f.close()
    print(p)


def setlvl0():
    global level, hc, cg0, cg1, cg2, cg3, cp0, cp1, cp2, cp3
    cg0 = (10 * wc / 20) + (wc / 40) - 10 + 30
    cg1 = (10 * hc / 20) + (hc / 40) - 10
    cg2 = (10 * wc / 20) + (wc / 40) + 10 + 30
    cg3 = (10 * hc / 20) + (hc / 40) + 10
    cp0 = (wc / 40) - 10
    cp1 = (hc / 40) - 10
    cp2 = (wc / 40) + 10
    cp3 = (hc / 40) + 10
    level = 0


def setlvl1():
    global level, hc, cg0, cg1, cg2, cg3, cp0, cp1, cp2, cp3
    hc = (9 * h) / 11
    cg0 = (10 * wc / 20) + (wc / 40) - 10 + 30
    cg1 = (15 * hc / 30) + (hc / 60) - 10
    cg2 = (10 * wc / 20) + (wc / 40) + 10 + 30
    cg3 = (15 * hc / 30) + (hc / 60) + 10
    cp0 = (wc / 40) - 10
    cp1 = (hc / 60) - 10
    cp2 = (wc / 40) + 10
    cp3 = (hc / 60) + 10
    level = 1


def setlvl2():
    global level
    level = 2


def quitter():
    global hs, points
    if points > hs:
        hs = points
        ms = open('m_s.txt', 'wb')
        pickle.dump(hs, ms)
        pickle.dump(nom_j, ms)
        ms.close()
        print(points, hs)
    # cs = plato.bbox(pac_man)
    cs = [15, 15, 15, 15]
    if len(frofro) > 0:
        f = open('file.txt', 'wb')
        pickle.dump(cs, f)
        f.close()
        fen_j.destroy()
    else:
        fen_j.destroy()


def meilleur():
    global hs, nom_mj
    ms = open('m_s.txt', 'rb')
    try:
        hss = pickle.load(ms)
    except EOFError:
        print('pas de hs')
    else:
        hs = hss
    try:
        nom_ms = pickle.load(ms)
    except EOFError:
        print('NoOne')
    else:
        nom_mj = nom_ms
    ms.close()


""" Variables """
vies = 2
w = 900
wc = (2 * w) / 3
h = (11 * w) / 9
hc = (6 * h) / 11
cg0 = (10 * wc / 20) + (wc / 40) - 10 + 30
cg1 = (10 * hc / 20) + (hc / 40) - 10
cg2 = (10 * wc / 20) + (wc / 40) + 10 + 30
cg3 = (10 * hc / 20) + (hc / 40) + 10
cp0 = (wc / 40) + (11 * wc / 20) - 10
cp1 = (hc / 40) + (8 * hc / 20) - 10
cp2 = (wc / 40) + (11 * wc / 20) + 10
cp3 = (hc / 40) + (8 * hc / 20) + 10
nom_j = 'Inconnu'
num_coul = 0
num_coul_ob = 3
points = 0
hs = 0
dx = 0
dy = 0
dt = 350
flag = 0
rect = []
frofro = []
last_after = []
level = 0

nom_mj = " "

couleurs = ['black', 'red', 'purple', 'blue', 'pink', 'brown', 'green']
backG = couleurs[num_coul]
ob_coul = couleurs[num_coul_ob]

meilleur()

"""on crée une fenetre-->fen_a et on lui donne une couleur"""
fen_a = tkinter.Tk()
fen_a.configure(bg=backG)

"""décoration fen_a"""

canvas1 = tkinter.Canvas(fen_a, width=200, height=200, background="black", highlightcolor="black")
canvas2 = tkinter.Canvas(fen_a, width=200, height=200, background="black", highlightcolor="black")

pac1 = canvas1.create_oval(0, 0, 200, 200, fill='yellow', outline='white')
pac2 = canvas2.create_arc(0, 0, 200, 200, extent=300, start=20, fill='yellow', outline='white')

oeil1 = canvas1.create_oval(50, 50, 80, 80, fill='black')
oeil2 = canvas1.create_oval(120, 50, 150, 80, fill='black')
bouche1 = canvas1.create_arc(80, 90, 125, 160, extent=180, start=180, fill='blue')

oeuil3 = canvas2.create_oval(120, 50, 150, 80, fill='white')
eouil = canvas2.create_oval(130, 60, 150, 80, fill='black')
boule1 = canvas2.create_oval(160, 90, 200, 130, fill='pink')

"""
on va créer et placer les diférents boutons,labels (certains boutons sont
cachés et ne seront révéles que via la fonction revel qui sera appellée
par le bouton otpion)
"""

aide = tkinter.Label(fen_a, text=("Appuyer sur les fleches directionnelles (haut,bas,gauche,droite) pour faire bouger"
                                  " le pac man."), font=("comic", 10))
aide2 = tkinter.Label(fen_a, text="Appuyer sur espace pour mettre le jeu en pause ou reprendre la partie.",
                      font=("comic", 10))
aide.configure(bg='green', fg='white')
aide2.configure(bg='green', fg='white')

nom_joueur = tkinter.Label(fen_a, text=' NAME  : ', font=("comic", 14))
nom_joueur.configure(bg=backG, fg='white')
entree1 = tkinter.Entry(fen_a)
val_nom = tkinter.Button(fen_a, text='Enter', command=name, relief='raised', background='pink')

texte1 = tkinter.Label(fen_a, text='Pac \n'' Mania', font="Times 50 bold italic underline")
texte1.configure(bg=backG, fg='white')
b1 = tkinter.Button(fen_a, text='NEW GAME', font=("comic", 24), relief='raised',
                    background='yellow', command=fen_a.destroy)
b2 = tkinter.Button(fen_a, text='OPTIONS', command=revel)
b3 = tkinter.Button(fen_a, text='changer la couleur', command=changer_coul)
b4 = tkinter.Button(fen_a, text='AIDE', command=helpMe)
b6 = tkinter.Button(fen_a, text='VALIDER', command=cacher)

mb = tkinter.Menubutton(fen_a, text='niveaux', relief='raised')

mb.menu = tkinter.Menu(mb, tearoff=0)
mb['menu'] = mb.menu

mb.menu.add_checkbutton(label='lvl1', command=setlvl0)
mb.menu.add_checkbutton(label='lvl2', command=setlvl1)
mb.menu.add_checkbutton(label='lvl3', command=setlvl2)
mb.menu.add_checkbutton(label='sauvegarde', command=setlvlsauv)

texte1.grid(row=1, column=2, padx=0, pady=50)
nom_joueur.grid(row=2, column=1, sticky='E', pady=20)
val_nom.grid(row=2, column=3, sticky='W', padx=10)
entree1.grid(row=2, column=2)
b1.grid(row=3, column=2, pady=0)
b2.grid(row=4, column=2, pady=20)
b3.grid_forget()
b4.grid_forget()
mb.grid_forget()
b6.grid_forget()
canvas1.grid(row=1, column=1)
canvas2.grid(row=1, column=3)
aide.grid_forget()
aide2.grid_forget()

fen_a.bind('<Key>', key)

# on initialise
fen_a.mainloop()

'''On crée la fenetre qui contiendra le jeu --> fen_j'''

fen_j = tkinter.Tk()
fen_j.configure(bg=backG)

score_player1 = tkinter.StringVar()
affichescore = tkinter.Label(fen_j, textvariable=score_player1)


texte02 = tkinter.Label(fen_j, text='High Score')
texte02.configure(bg='black', fg='white')
texte03 = tkinter.Label(fen_j, text="%s --> %d" % (nom_mj, hs))
texte03.configure(bg='black', fg='red')
nom_joueur_actuel = tkinter.Label(fen_j, text=nom_j, font=("comic", 22))
nom_joueur_actuel.configure(bg='black', fg='white')
texte05 = tkinter.Label(fen_j, text='PRESS SPACE FOR START', font=("comic", 18))
texte05.configure(bg='black', fg='white')
b01 = tkinter.Button(fen_j, text='NEW GAME', font=("comic", 18), command=new_game)
b02 = tkinter.Button(fen_j, text='QUIT', font=("comic", 18), command=quitter)
plato = tkinter.Canvas(fen_j, width=wc, height=hc, bg=backG)

affichescore.grid(row=3, column=2)

texte02.grid(row=1, column=1)
texte03.grid(row=2, column=1)
nom_joueur_actuel.grid(row=2, column=2)
texte05.grid(row=5, column=2)
b01.grid(row=4, column=3, sticky='N', padx=20, pady=40)
b02.grid(row=4, column=3, sticky='S', padx=20, pady=40)
plato.grid(row=4, column=2, padx=10, pady=10)

"""QUESTION PROF"""

rectangles0 = [(wc / 20, hc / 20, 5 * wc / 20, 3 * hc / 20),
               (6 * wc / 20, 0, 9 * wc / 20, 4 * hc / 20),
               (10 * wc / 20, hc / 20, 13 * wc / 20, 3 * hc / 20),
               (14 * wc / 20, 0, 19 * wc / 20, 2 * hc / 20),
               (0, 4 * hc / 20, 5 * wc / 20, 7 * hc / 20),
               (6 * wc / 20, 5 * hc / 20, 9 * wc / 20, 8 * hc / 20),
               (10 * wc / 20, 4 * hc / 20, 13 * wc / 20, 7 * hc / 20),
               (14 * wc / 20, 3 * hc / 20, 19 * wc / 20, 6 * hc / 20),
               (wc / 20, 8 * hc / 20, 5 * wc / 20, 12 * hc / 20),
               (5 * wc / 20, 9 * hc / 20, 10 * wc / 20, 12 * hc / 20),
               (11 * wc / 20, 8 * hc / 20, 14 * wc / 20, 12 * hc / 20),
               (16 * wc / 20, 7 * hc / 20, 20 * wc / 20, 10 * hc / 20),
               (0, 13 * hc / 20, 4 * wc / 20, 16 * hc / 20),
               (5 * wc / 20, 13 * hc / 20, 9 * wc / 20, 16 * hc / 20),
               (10 * wc / 20, 13 * hc / 20, 14 * wc / 20, 16 * hc / 20),
               (15 * wc / 20, 11 * hc / 20, 19 * wc / 20, 14 * hc / 20),
               (wc / 20, 17 * hc / 20, 7 * wc / 20, 19 * hc / 20),
               (8 * wc / 20, 17 * hc / 20, 16 * wc / 20, 19 * hc / 20),
               (16 * wc / 20, 15 * hc / 20, 19 * wc / 20, 19 * hc / 20)]

rectangles1 = [(wc / 20, hc / 30, 3 * wc / 20, 3 * hc / 30),
               (4 * wc / 20, 0, 4 * wc / 20, 2 * hc / 30),
               (5 * wc / 20, hc / 30, 6 * wc / 20, 3 * hc / 30),
               (6 * wc / 20, 2 * hc / 30, 8 * wc / 20, 3 * hc / 30),
               (7 * wc / 20, 0, 8 * wc / 20, hc / 30),
               (9 * wc / 20, 0, 10 * wc / 20, 4 * hc / 30),
               (11 * wc / 20, 0, 13 * wc / 20, 2 * hc / 30),
               (11 * wc / 20, 3 * hc / 30, 18 * wc / 20, 4 * hc / 30),
               (14 * wc / 20, hc / 30, 15 * wc / 20, 3 * hc / 30),
               (16 * wc / 20, hc / 30, 19 * wc / 20, 2 * hc / 30),
               (19 * wc / 20, 3 * hc / 30, 20 * wc / 20, 4 * hc / 30),
               (0, 4 * hc / 30, 5 * wc / 20, 6 * hc / 30),
               (6 * wc / 20, 4 * hc / 30, 7 * wc / 20, 7 * hc / 30),
               (7 * wc / 20, 5 * hc / 30, 10 * wc / 20, 6 * hc / 30),
               (11 * wc / 20, 5 * hc / 30, 15 * wc / 20, 7 * hc / 30),
               (17 * wc / 20, 5 * hc / 30, 20 * wc / 20, 6 * hc / 30),
               (wc / 20, 7 * hc / 30, 5 * wc / 20, 10 * hc / 30),
               (8 * wc / 20, 7 * hc / 30, 10 * wc / 20, 8 * hc / 30),
               (6 * wc / 20, 8 * hc / 30, 11 * wc / 20, 11 * hc / 30),
               (13 * wc / 20, 8 * hc / 30, 19 * wc / 20, 12 * hc / 30),
               (17 * wc / 20, 7 * hc / 30, 19 * wc / 20, 8 * hc / 30),
               (0, 11 * hc / 30, 4 * wc / 20, 14 * hc / 30),
               (5 * wc / 20, 12 * hc / 30, 8 * wc / 20, 13 * hc / 30),
               (9 * wc / 20, 12 * hc / 30, 12 * wc / 20, 13 * hc / 30),
               (6 * wc / 20, 14 * hc / 30, 8 * wc / 20, 15 * hc / 30),
               (wc / 20, 15 * hc / 30, 8 * wc / 20, 17 * hc / 30),
               (9 * wc / 20, 14 * hc / 30, 11 * wc / 20, 16 * hc / 30),
               (12 * wc / 20, 14 * hc / 30, 13 * wc / 20, 15 * hc / 30),
               (13 * wc / 20, 13 * hc / 30, 17 * wc / 20, 16 * hc / 30),
               (18 * wc / 20, 13 * hc / 30, 20 * wc / 20, 16 * hc / 30),
               (wc / 20, 18 * hc / 30, 6 * wc / 20, 20 * hc / 30),
               (7 * wc / 20, 18 * hc / 30, 9 * wc / 20, 20 * hc / 30),
               (9 * wc / 20, 17 * hc / 30, 15 * wc / 20, 20 * hc / 30),
               (16 * wc / 20, 17 * hc / 30, 19 * wc / 20, 19 * hc / 30),
               (0, 21 * hc / 30, wc / 20, 24 * hc / 30),
               (2 * wc / 20, 21 * hc / 30, 8 * wc / 20, 24 * hc / 30),
               (9 * wc / 20, 21 * hc / 30, 15 * wc / 20, 23 * hc / 30),
               (16 * wc / 20, 20 * hc / 30, 20 * wc / 20, 25 * hc / 30),
               (wc / 20, 25 * hc / 30, 9 * wc / 20, 27 * hc / 30),
               (10 * wc / 20, 24 * hc / 30, 15 * wc / 20, 26 * hc / 30),
               (wc / 20, 28 * hc / 30, 4 * wc / 20, 29 * hc / 30),
               (5 * wc / 20, 28 * hc / 30, 9 * wc / 20, 29 * hc / 30),
               (10 * wc / 20, 27 * hc / 30, 12 * wc / 20, 30 * hc / 30),
               (13 * wc / 20, 27 * hc / 30, 26 * wc / 20, 29 * hc / 30),
               (26 * wc / 20, 25 * hc / 30, 29 * wc / 20, 29 * hc / 30)]

plato1_0 = Obstacles

fantome1 = Gost()
fantome2 = Gost()
fantome3 = Gost()
fantome4 = Gost()
fantome5 = Gost()

fromages()

Obstacles.creation_plateau(plato1_0)

pac_man = Pac()

"""teste = plato.bbox(Pac.pac_man)
print(teste)"""

fen_j.bind('<Key>', key)

fen_j.mainloop()