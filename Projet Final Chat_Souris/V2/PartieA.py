from graphics import*
from pygame import mixer
import PartieB

Largeur=1000
Hauteur=800
Rayon=26
pygame.init()
f=pygame.display.set_mode((Largeur,Hauteur))
chat=pygame.image.load('tom.jpg')
chat.convert()
chat_blanc=pygame.image.load('tom_blanc.jpg')
chat_blanc.convert()
souris=pygame.image.load('jerry.jpg')
souris.convert()
souris_blanc=pygame.image.load('jerry_blanc.jpg')
souris_blanc.convert()
background = pygame.image.load('chat_souris.jpg')
background.convert()


def voisin(a):
    v=[]
    if a==F1:
        v=[S2,S4]
    elif a==F2:
        v=[S1,S4,S6,S9]
    elif a==F3:
        v=[S4,S7,S9]
    elif a==F4:
        v=[S1,S2,S3,S5]
    elif a==F5:
        v=[S4,S6,S7]
    elif a==F6:
        v=[S2,S5,S8]
    elif a==F7:
        v=[S3,S5,S8]
    elif a==F8:
        v=[S6,S7]
    return v



def fromage(point):
    jaune=(255,190,41)
    jaune1=(248,233,68)
    (x,y)=point
    xr1=x+(1*Largeur)//100
    yr1=y
    xr2=x-(1*Largeur)//100
    yr2=y-(1*Hauteur)//100
    xr3=x
    yr3=y+(1*Hauteur)//100
    r1=(xr1,yr1)
    r2=(xr2,yr2)
    r3=(xr3,yr3)
    x2=x+(2*Largeur)//100
    x=x-(2*Largeur)//100
    y2=y+(1.5*Hauteur)//100
    y=y-(1.5*Hauteur)//100
    p1=(x,y)
    p2=(x2,y2)
    p3=p1
    p4=p2
    for i in range(7):
        draw_fill_rectangle(p1,p2,jaune,f)
        (x,y)=p1
        (x2,y2)=p2
        x=x+2
        x2=x2+1
        y=y-1
        y2=y2-1
        p1=(x,y)
        p2=(x2,y2)
    draw_fill_rectangle(p3,p4,jaune1,f)
    draw_fill_circle(r1,3,jaune,f)
    draw_fill_circle(r2,3,jaune,f)
    draw_fill_circle(r3,3,jaune,f)


def croix_exit():
    # Dessin d'une croix rouge en haut de l'écran
    Pa=((94*Largeur)//100,(1*Hauteur)//100)
    Pb=((99*Largeur)//100,(1*Hauteur)//100)
    Pc=((94*Largeur)//100,(6*Hauteur)//100)
    Pd=((99*Largeur)//100,(6*Hauteur)//100)
    draw_line(Pa,Pb,rouge,f)
    draw_line(Pb,Pc,rouge,f)
    draw_line(Pc,Pd,rouge,f)
    draw_line(Pd,Pa,rouge,f)
    draw_line(Pa,Pc,rouge,f)
    draw_line(Pb,Pd,rouge,f)

def cadre_cote():
    a=(80*Largeur)//100
    draw_fill_rectangle((a,0),(Largeur,Hauteur),gris,f)

def bandeau_bas(x):
    a=(70*Hauteur)//100
    b=(80*Largeur)//100
    c=(2*Largeur)//100
    d=(80*Hauteur)//100
    draw_fill_rectangle((0,a),(b,Hauteur),argent,f)
    if x==1:
        ecrire("Au tour du chat",(c,d),60,noir,f)
    elif x==2:
        ecrire("Au tour de la souris",(c,d),60,noir,f)
    else:
        pass



class graphe_graphics:

    def __init__(self,centre):
        self.rayon=Rayon
        self.centre=centre

    def sommet(self,coul,num):
        draw_fill_circle(self.centre,self.rayon,blanc,f)
        draw_circle(self.centre,self.rayon,coul,f)
        (x,y)=self.centre
        x=x-2
        y=y-6
        self.centre=(x,y)
        ecrire(num,self.centre,16,noir,f)

    def arrete(self,p1,p2,coul):
        draw_line(p1,p2,coul,f)


class evenement:
    def __init__(self):
        self.pos_chat=F2
        self.pos_souris=F7
        self.tour=0
        self.event=False
        self.fin=False
        self.pena_chat=0
        self.pena_souris=0
        self.run=True
        self.alpha=0


    def deplacement(self,pos1,pos2,a):
        if a==1:
            f.blit(chat_blanc,pos1[0])
            f.blit(chat,pos2[0])
            self.pos_chat[1]=0
            pos2[1]=1
            self.pos_chat=pos2
        elif a==2:
            f.blit(souris_blanc,pos1[0])
            f.blit(souris,pos2[0])
            self.pos_souris[1]=0
            pos2[1]=2
            self.pos_souris=pos2



    def compte_tour(self):
        affiche_auto_off()
        draw_fill_rectangle((80*Largeur//100,17*Hauteur//100),(Largeur,23*Hauteur//100),gris,f)
        p1=(82*Largeur//100,20*Hauteur//100)
        a=("Tour numéro:")
        b=str(self.tour)
        c=("/15")
        ecrire((a+b+c),p1,20,noir,f)
        affiche_all()

    def pénalité(self):
        affiche_auto_off()
        draw_fill_rectangle((80*Largeur//100,58*Hauteur//100),(Largeur,65*Hauteur//100),gris,f)
        a=("Pénalité de la souris:")
        b=("Pénalité du chat:")
        c=str(self.pena_chat)
        d=str(self.pena_souris)
        e=("/3")
        p1=(82*Largeur//100,60*Hauteur//100)
        p2=(82*Largeur//100,63*Hauteur//100)
        ecrire((a+d+e),p1,16,noir,f)
        ecrire((b+c+e),p2,16,noir,f)
        affiche_all()


    def timer(self,tps,A):
        blanc=(250,235,215)
        x1=(65*Largeur)//100
        y1=(80*Hauteur)//100
        p1=(x1,y1)
        x2=(58*Largeur)//100
        y2=(82*Hauteur)//100
        p2=(x2,y2)
        affiche_auto_off()
        draw_fill_rectangle(((55*Largeur)//100,(77*Hauteur)//100),((77*Largeur)//100,(90*Hauteur)//100),blanc,f)
        croix_exit()
        self.run=True
        if self.tour==15:
            self.souris_victoire()
            self.fin=True
            self.run=False
        while self.run:
            a=str(tps)
            ecrire(a,p1,50,noir,f)
            affiche_all()
            pressed=()
            pressed=pygame.key.get_pressed
            attendre(1000)
            tps=tps-1
            ecrire_nombre(a,p1,50,blanc,f)
            if tps==-1:
                ecrire("+1 point de pénalité",p2,20,noir,f)
                affiche_all()
                pressed=()
                self.timer==False
                if A==1:
                    self.choix_interaction(2)
                elif A==2:
                    self.choix_interaction(3)
                attendre(2000)
                ecrire("+1 point de pénalité",p2,20,blanc,f)
                affiche_all()
                self.run=False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.mixer.music.pause()
                    quit_graphics()
                elif event.type ==pygame.MOUSEBUTTONDOWN:
                    ecrire("        Quitter",(((91*Largeur)//100,(7*Hauteur)//100)),11,noir,f)
                    p=wait_clic()
                    x,y=p
                    if (94*Largeur)//100<=x<=(99*Largeur)//100 and (1*Hauteur)//100<=y<=(6*Hauteur)//100:
                        self.run=False
                        A=0
                        pygame.mixer.music.pause()
                        quit_graphics()
                elif A==1:
                    v=voisin(self.pos_chat)
                    if event.type == pygame.KEYDOWN or pressed==pygame.KEYDOWN:
                        if event.key == pygame.K_F1 or pressed==pygame.K_F1:
                            for i in range(len(v)):
                                if v[i]==S1:
                                    valeur=F1[1]
                                    if valeur==1 or valeur==3:
                                        pass
                                    elif valeur==2:
                                        self.deplacement(self.pos_chat,F1,1)
                                        self.chat_victoire()
                                        self.run = False
                                        affiche_all()
                                    else:
                                        self.deplacement(self.pos_chat,F1,1)
                                        F1[1]=1
                                        self.run = False
                                        affiche_all()
                        elif event.key == pygame.K_F2 or pressed==pygame.K_F2:
                            for i in range(len(v)):
                                if v[i]==S2:
                                    valeur=F2[1]
                                    if valeur==1 or valeur==3:
                                        pass
                                    elif valeur==2:
                                        self.deplacement(self.pos_chat,F2,1)
                                        self.chat_victoire()
                                        self.run = False
                                        affiche_all()
                                    else:
                                        self.deplacement(self.pos_chat,F2,1)
                                        F2[1]=1
                                        self.run = False
                                        affiche_all()
                        elif event.key == pygame.K_F3 or pressed==pygame.K_F3:
                            for i in range(len(v)):
                                if v[i]==S3:
                                    valeur=F3[1]
                                    if valeur==1 or valeur==3:
                                        pass
                                    elif valeur==2:
                                        self.deplacement(self.pos_chat,F3,1)
                                        self.chat_victoire()
                                        self.run = False
                                        affiche_all()
                                    else:
                                        print("d")
                                        self.deplacement(self.pos_chat,F3,1)
                                        F3[1]=1
                                        self.run = False
                                        affiche_all()
                        elif event.key == pygame.K_F4 or pressed==pygame.K_F4:
                            for i in range(len(v)):
                                if v[i]==S4:
                                    valeur=F4[1]
                                    if valeur==1 or valeur==3:
                                        pass
                                    elif valeur==2:
                                        self.deplacement(self.pos_chat,F4,1)
                                        self.chat_victoire()
                                        self.run = False
                                        affiche_all()
                                    else:
                                        self.deplacement(self.pos_chat,F4,1)
                                        F4[1]=1
                                        self.run = False
                                        affiche_all()
                        elif event.key == pygame.K_F5 or pressed==pygame.K_F5:
                            for i in range(len(v)):
                                if v[i]==S5:
                                    valeur=F5[1]
                                    if valeur==1 or valeur==3:
                                        pass
                                    elif valeur==2:
                                        self.deplacement(self.pos_chat,F5,1)
                                        self.chat_victoire()
                                        self.run = False
                                        affiche_all()
                                    else:
                                        self.deplacement(self.pos_chat,F5,1)
                                        F5[1]=1
                                        self.run = False
                                        affiche_all()
                        elif event.key == pygame.K_F6 or pressed==pygame.K_F6:
                            for i in range(len(v)):
                                if v[i]==S6:
                                    valeur=F6[1]
                                    if valeur==1 or valeur==3:
                                        pass
                                    elif valeur==2:
                                        self.deplacement(self.pos_chat,F6,1)
                                        self.chat_victoire()
                                        self.run = False
                                        affiche_all()
                                    else:
                                        self.deplacement(self.pos_chat,F6,1)
                                        F6[1]=1
                                        self.run = False
                                        affiche_all()
                        elif event.key == pygame.K_F7 or pressed==pygame.K_F7:
                            for i in range(len(v)):
                                if v[i]==S7:
                                    valeur=F7[1]
                                    if valeur==1 or valeur==3:
                                        pass
                                    elif valeur==2:
                                        self.deplacement(self.pos_chat,F7,1)
                                        self.fin==True
                                        self.chat_victoire()
                                        self.run = False
                                        affiche_all()
                                    else:
                                        self.deplacement(self.pos_chat,F7,1)
                                        F7[1]=1
                                        self.run = False
                                        affiche_all()
                        elif event.key == pygame.K_F8 or pressed==pygame.K_F8:
                            for i in range(len(v)):
                                if v[i]==S8:
                                    valeur=F8[1]
                                    if valeur==1 or valeur==3:
                                        pass
                                    elif valeur==2:
                                        self.deplacement(self.pos_chat,F8,1)
                                        self.chat_victoire()
                                        self.run = False
                                        affiche_all()
                                    else:
                                        self.deplacement(self.pos_chat,F8,1)
                                        F8[1]=1
                                        self.run = False
                                        affiche_all()
                elif A==2:
                    v=voisin(self.pos_souris)
                    if event.type == pygame.KEYDOWN or pressed==pygame.KEYDOWN:
                        if event.key == pygame.K_F1 or pressed==pygame.K_F1:
                            for i in range(len(v)):
                                if v[i]==S1:
                                    valeur=F1[1]
                                    if valeur==1 or valeur==2 or valeur==3:
                                        pass
                                    else:
                                        self.deplacement(self.pos_souris,F1,2)
                                        F1[1]=2
                                        self.run = False
                                        affiche_all()
                        elif event.key == pygame.K_F2 or pressed==pygame.K_F2:
                            for i in range(len(v)):
                                if v[i]==S2:
                                    valeur=F2[1]
                                    if valeur==1 or valeur==2 or valeur==3:
                                        pass
                                    else:
                                        self.deplacement(self.pos_souris,F2,2)
                                        F2[1]=2
                                        self.run = False
                                        affiche_all()
                        elif event.key == pygame.K_F3 or pressed==pygame.K_F3:
                            for i in range(len(v)):
                                if v[i]==S3:
                                    valeur=F3[1]
                                    if valeur==1 or valeur==2 or valeur==3:
                                        pass
                                    else:
                                        self.deplacement(self.pos_souris,F3,2)
                                        F3[1]=2
                                        self.run = False
                                        affiche_all()
                        elif event.key == pygame.K_F4 or pressed==pygame.K_F4:
                            for i in range(len(v)):
                                if v[i]==S4:
                                    valeur=F4[1]
                                    if valeur==1 or valeur==2 or valeur==3:
                                        pass
                                    else:
                                        self.deplacement(self.pos_souris,F4,2)
                                        F4[1]=2
                                        self.run = False
                                        affiche_all()
                        elif event.key == pygame.K_F5 or pressed==pygame.K_F5:
                            for i in range(len(v)):
                                if v[i]==S5:
                                    valeur=F5[1]
                                    if valeur==1 or valeur==2 or valeur==3:
                                        pass
                                    else:
                                        self.deplacement(self.pos_souris,F5,2)
                                        F5[1]=2
                                        self.run = False
                                        affiche_all()
                        elif event.key == pygame.K_F6 or pressed==pygame.K_F6:
                            for i in range(len(v)):
                                if v[i]==S6:
                                    valeur=F6[1]
                                    if valeur==1 or valeur==2 or valeur==3:
                                        pass
                                    else:
                                        self.deplacement(self.pos_souris,F6,2)
                                        F6[1]=2
                                        self.run = False
                                        affiche_all()
                        elif event.key == pygame.K_F7 or pressed==pygame.K_F7:
                            for i in range(len(v)):
                                if v[i]==S7:
                                    valeur=F7[1]
                                    if valeur==1 or valeur==2 or valeur==3:
                                        pass
                                    else:
                                        self.deplacement(self.pos_souris,F7,2)
                                        F7[1]=2
                                        self.run = False
                                        affiche_all()
                        elif event.key == pygame.K_F8 or pressed==pygame.K_F8:
                            for i in range(len(v)):
                                if v[i]==S8:
                                    valeur=F8[1]
                                    if valeur==1 or valeur==2 or valeur==3:
                                        pass
                                    else:
                                        self.deplacement(self.pos_souris,F8,2)
                                        F8[1]=2
                                        self.run = False
                                        affiche_all()
                        elif event.key == pygame.K_F9 or pressed==pygame.K_F9:
                            for i in range(len(v)):
                                if v[i]==S9:
                                    valeur=F9[1]
                                    if valeur==1 or valeur==2:
                                        pass
                                    else:
                                        self.deplacement(self.pos_souris,F9,2)
                                        F9[1]=2
                                        self.souris_victoire()
                                        self.run = False
                                        affiche_all()



    def chat_victoire(self):
        self.run=False
        self.fin=True
        fill_screen(blanc,f)
        s = pygame.image.load('chat_victoire2.jpg')
        s.convert()
        f.blit(s, (0,0))
        ecrire("Rejouer",(220,460),24,noir,f)
        p1=(270,490)
        p2=(240,510)
        draw_fill_rectangle(p1,p2,vert,f)
        ecrire("Menu",(490,460),24,noir,f)
        p1=(510,490)
        p2=(540,510)
        draw_fill_rectangle(p1,p2,rouge,f)
        ecrire("Le chat à gagné !!!",(270,65),24,bleu,f)
        pygame.mixer.music.pause()
        mixer.music.load("win.ogg")
        mixer.music.play()
        p=wait_clic()
        (x,y)=p
        if 240<=x<=270 and 490<=y<=510:
            PartieB.main()
        if 510<=x<=540 and 490<=y<=510:
            PartieB.Menu()
        pygame.mixer.music.pause()

    def souris_victoire(self):
        self.run=False
        self.fin=True
        fill_screen(blanc,f)
        s = pygame.image.load('souris_victoire.jpg')
        s.convert()
        f.blit(s, (0,0))
        ecrire("Rejouer",(220,460),24,noir,f)
        p1=(270,490)
        p2=(240,510)
        draw_fill_rectangle(p1,p2,vert,f)
        ecrire("Menu",(490,460),24,noir,f)
        p1=(510,490)
        p2=(540,510)
        draw_fill_rectangle(p1,p2,rouge,f)
        ecrire("La souris à gagné !!!",(470,65),24,bleu,f)
        pygame.mixer.music.pause()
        mixer.music.load("win.ogg")
        mixer.music.play()
        p=wait_clic()
        (x,y)=p
        if 240<=x<=270 and 490<=y<=510:
            PartieB.main()
        if 510<=x<=540 and 490<=y<=510:
            PartieB.Menu()
        pygame.mixer.music.pause()

    def suivant(self):
        self.compte_tour()
        bandeau_bas(2)
        self.pénalité()
        self.timer(15,2)
        bandeau_bas(1)
        self.pénalité()
        self.timer(15,1)
        self.tour=self.tour+1



    def choix_interaction(self,A):
        if A==0:
            self.chat_victoire()
            self.fin=True
        elif A==1:
            self.souris_victoire()
            self.fin=True
        elif A==2:
            if self.pena_chat<2:
                self.pena_chat=self.pena_chat+1
            else:
                self.souris_victoire()
                self.fin=True
        elif A==3:
            if self.pena_souris<2:
                self.pena_souris=self.pena_souris+1
            else:
                self.chat_victoire()
                self.fin=True
        else:
            ()



S1=graphe_graphics((25*Largeur//100,13*Hauteur//100))
S2=graphe_graphics((64*Largeur//100,18*Hauteur//100))
S3=graphe_graphics((6*Largeur//100,27*Hauteur//100))
S4=graphe_graphics((40*Largeur//100,26*Hauteur//100))
S5=graphe_graphics((24*Largeur//100,39*Hauteur//100))
S6=graphe_graphics((68*Largeur//100,40*Hauteur//100))
S7=graphe_graphics((16*Largeur//100,56*Hauteur//100))
S8=graphe_graphics((43*Largeur//100,54*Hauteur//100))
S9=graphe_graphics((75*Largeur//100,9*Hauteur//100))
F1=[(28*Largeur//100,5*Hauteur//100),0]
F2=[(60*Largeur//100,6*Hauteur//100),1]
F3=[(3*Largeur//100,16*Hauteur//100),0]
F4=[(37*Largeur//100,16*Hauteur//100),0]
F5=[(21*Largeur//100,28*Hauteur//100),0]
F6=[(68*Largeur//100,29*Hauteur//100),0]
F7=[(21*Largeur//100,47*Hauteur//100),2]
F8=[(35*Largeur//100,45*Hauteur//100),0]
F9=[(75*Largeur//100,9*Hauteur//100),3]




