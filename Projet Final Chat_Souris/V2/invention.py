from graphics import*
from pygame import mixer

"""
Largeur=1000
Hauteur=800
f=pygame.display.set_mode((Largeur,Hauteur))
pygame.init()


fill_screen(blanc,f)

wait_escape(f)
quit_graphics()
"""
Largeur=1000
Hauteur=800


a=(1,7)

a[1]=2


























"""
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
        if tps==0:
            ()
        elif tps>0 and tps<60:
            while tps!=0 and self.event==False:
                a=str(tps)
                ecrire(a,p1,50,noir,f)
                affiche_all()
                for i in range(100):
                    attendre(10)
                    events=pygame.event.get()
                    for event in events:
                        if event.type==pygame.KEYDOWN:
                            if A==1:
                                self.touche(1)
                            elif A==2:
                                self.touche(2)
                ecrire_nombre(a,p1,50,blanc,f)
                tps=tps-1
            if tps==0:
                ecrire("Plus 1 point de pénalité",p2,20,noir,f)
                affiche_all()
                if A==1:
                    self.choix_interaction(2)
                elif A==2:
                    self.choix_interaction(3)
                attendre(3000)
                ecrire("Plus 1 point de pénalité",p2,20,blanc,f)
                affiche_all()

        else:
            return("La valeur n'est pas valable.")






def touche(self,a):
        if a==1:
            if self.keys[pygame.K_a]:
                v=voisin("a")
                for i in range(len(v)):
                    if v[i]==self.keys[pygame.K_a]:
                        self.deplacement(self.pos_chat,a)
            elif self.keys[pygame.K_z]:
                v=voisin("z")
                for i in range(len(v)):
                    if v[i]==self.keys[pygame.K_z]:
                        self.deplacement(self.pos_chat,z)
            elif self.keys[pygame.K_e]:
                v=voisin("e")
                for i in range(len(v)):
                    if v[i]==self.keys[pygame.K_e]:
                        self.deplacement(self.pos_chat,e)
            elif self.keys[pygame.K_r]:
                v=voisin("r")
                for i in range(len(v)):
                    if v[i]==self.keys[pygame.K_r]:
                        self.deplacement(self.pos_chat,r)
            elif self.keys[pygame.K_t]:
                v=voisin("t")
                for i in range(len(v)):
                    if v[i]==self.keys[pygame.K_t]:
                        self.deplacement(self.pos_chat,t)
            elif self.keys[pygame.K_y]:
                v=voisin("y")
                for i in range(len(v)):
                    if v[i]==self.keys[pygame.K_y]:
                        self.deplacement(self.pos_chat,y)
            elif self.keys[pygame.K_u]:
                v=voisin("u")
                for i in range(len(v)):
                    if v[i]==self.keys[pygame.K_u]:
                        self.deplacement(self.pos_chat,u)
            elif self.keys[pygame.K_i]:
                v=voisin("i")
                for i in range(len(v)):
                    if v[i]==self.keys[pygame.K_i]:
                        self.deplacement(self.pos_chat,i)
        elif a==2:
            if event.key==pygame.K_a:
                v=voisin("a")
                for i in range(len(v)):
                    if v[i]==self.keys[pygame.K_a]:
                        self.deplacement(self.pos_souris,a)
            elif self.keys[pygame.K_z]:
                v=voisin("z")
                for i in range(len(v)):
                    if v[i]==self.keys[pygame.K_z]:
                        self.deplacement(self.pos_souris,z)
            elif self.keys[pygame.K_e]:
                v=voisin("e")
                for i in range(len(v)):
                    if v[i]==self.keys[pygame.K_e]:
                        self.deplacement(self.pos_souris,e)
            elif self.keys[pygame.K_r]:
                v=voisin("r")
                for i in range(len(v)):
                    if v[i]==self.keys[pygame.K_r]:
                        self.deplacement(self.pos_souris,r)
            elif self.keys[pygame.K_t]:
                v=voisin("t")
                for i in range(len(v)):
                    if v[i]==self.keys[pygame.K_t]:
                        self.deplacement(self.pos_souris,t)
            elif self.keys[pygame.K_y]:
                v=voisin("y")
                for i in range(len(v)):
                    if v[i]==self.keys[pygame.K_y]:
                        self.deplacement(self.pos_souris,y)
            elif self.keys[pygame.K_u]:
                v=voisin("u")
                for i in range(len(v)):
                    if v[i]==self.keys[pygame.K_u]:
                        self.deplacement(self.pos_souris,u)
            elif self.keys[pygame.K_i]:
                v=voisin("i")
                for i in range(len(v)):
                    if v[i]==self.keys[pygame.K_i]:
                        self.deplacement(self.pos_souris,i)
            elif self.keys[pygame.K_o]:
                v=voisin("o")
                for i in range(len(v)):
                    if v[i]==self.keys[pygame.K_o]:
                        self.deplacement(self.pos_souris,o)

        self.keys=[]"""