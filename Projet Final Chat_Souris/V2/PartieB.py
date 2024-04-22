from graphics import *
from pygame import mixer
from PartieA import*


pygame.init()
pygame.display.set_caption("le jeu du Chat et de la Souris")


def Credit():
    f.blit(background, (0,0))

    p1=(22,22)
    p2=(258,248)
    draw_fill_rectangle(p1,p2,noir,f)
    p1=(25,25)
    p2=(255,245)
    draw_fill_rectangle(p1,p2,gris,f)

    p1=(32,50)
    ecrire("Ce jeu a été créer par :",p1,22,noir,f)

    p1=(45,115)
    p2=(217,232)
    draw_fill_rectangle(p1,p2,noir,f)
    p1=(47,117)
    p2=(215,230)
    draw_fill_rectangle(p1,p2,blanchedalmond,f)
    p2=(50,120)
    ecrire("Julien Petitbon",p2,18,noir,f)
    p3=(50,160)
    ecrire("Ambre Matha",p3,18 ,noir,f)
    p3=(50,200)
    ecrire("Abdelslam Allaouat",p3,18,noir,f)
    wait_clic()
    Menu()

def Comment_jouer():
    f.blit(background, (0,0))
    p1=(20,20)
    p2=(545,500)
    draw_fill_rectangle(p1,p2,noir,f)
    p1=(25,25)
    p2=(540,495)
    draw_fill_rectangle(p1,p2,gris,f)

    p2=(190,30)
    ecrire("Comment jouer ?",p2,22,noir,f)


    p2=(30,65)
    ecrire("Concept du jeu :",p2,19,blanchedalmond,f)
    p2=(30,105)
    ecrire("Il y a un total de 8 cases ainsi qu'une case frômage.",p2,17,blanc,f)
    p2=(30,135)
    ecrire("Le chat commence sur la case 2, la souris sur la case 7.",p2,17,blanc,f)
    p2=(30,165)
    ecrire("La souris est la première à jouer, c'est ensuite au tour du chat",p2,17,blanc,f)
    p2=(30,195)
    ecrire("et ainsi de suite jusqu'à la fin du jeu.",p2,17,blanc,f)
    p2=(30,235)
    ecrire("Déplacement :",p2,19,blanchedalmond,f)
    p2=(30,265)
    ecrire("Pour pouvoir se déplacer sur une case il suffit de cliquer sur ",p2,17,blanc,f)
    p2=(30,295)
    ecrire("les touches correspondante au clavier, par exemple pour se déplacer ",p2,17,blanc,f)
    p2=(30,325)
    ecrire("à la case 1, il faut cliquer sur F1 (etc..).",p2,17,blanc,f)
    p2=(30,365)
    ecrire("Le but du jeu est :",p2,19,blanchedalmond,f)
    p2=(30,395)
    ecrire("    - Si on est la souris, d'arriver jusqu'au frômage ou de faire",p2,17,blanc,f)
    p2=(30,415)
    ecrire("15 déplacement sans se faire attraper.",p2,17,blanc,f)
    p2=(30,445)
    ecrire("    - Si on est le chat, d'attraper la souris avant les 15 déplacments. ",p2,17,blanc,f)

    wait_clic()
    Menu()

def Menu():
    fill_screen(blanc,f)
    f.blit(background, (0,0))
    mixer.music.load("chill.ogg")
    mixer.music.play()

    p1=(45,45)
    p2=(255,105)
    draw_fill_rectangle(p1,p2,orange,f)
    p1=(46,46)
    p2=(254,104)
    draw_fill_rectangle(p1,p2,noir,f)
    p1=(49,49)
    p2=(251,101)
    draw_fill_rectangle(p1,p2,orange,f)
    p1=(50,50)
    p2=(250,100)
    draw_fill_rectangle(p1,p2,noir,f)
    p1=(65,60)
    ecrire("Commencer à jouer",p1,20,blanc,f)

    p3=(45,118)
    p4=(255,170)
    draw_fill_rectangle(p3,p4,orange,f)
    p3=(46,119)
    p4=(254,169)
    draw_fill_rectangle(p3,p4,noir,f)
    p3=(49,121)
    p4=(251,166)
    draw_fill_rectangle(p3,p4,orange,f)
    p3=(50,122)
    p4=(250,165)
    draw_fill_rectangle(p3,p4,noir,f)
    p2=(85,130)
    ecrire("Comment jouer",p2,20,blanc,f)

    p1=(46,181)
    p2=(255,235)
    draw_fill_rectangle(p1,p2,orange,f)
    p1=(47,182)
    p2=(254,234)
    draw_fill_rectangle(p1,p2,noir,f)
    p1=(49,185)
    p2=(251,231)
    draw_fill_rectangle(p1,p2,orange,f)
    p1=(50,186)
    p2=(250,230)
    draw_fill_rectangle(p1,p2,noir,f)
    p1=(125,195)
    ecrire("Crédit",p1,20,blanc,f)

    p1=(46,251)
    p2=(255,305)
    draw_fill_rectangle(p1,p2,orange,f)
    p1=(47,252)
    p2=(254,304)
    draw_fill_rectangle(p1,p2,noir,f)
    p1=(49,255)
    p2=(251,301)
    draw_fill_rectangle(p1,p2,orange,f)
    p1=(50,256)
    p2=(250,300)
    draw_fill_rectangle(p1,p2,noir,f)
    p1=(125,265)
    ecrire("Quitter",p1,20,blanc,f)
    run=True
    while run==True:
        p=wait_clic()
        choix=Analyse_clic(p)
        if choix==3:
            Credit()
            run=False
        if choix==2:
            Comment_jouer()
            run=False
        if choix==1:
            main()
            run=False


def Analyse_clic(p):
    x,y=p
    if 45<=x<=255 and 45<=y<=105:
        return 1

    if 45<=x<=255 and 118<=y<=170:
        return 2

    if 46<=x<=255 and 181<=y<=235:
        return 3

    if 46<=x<=255 and 251<=y<=305:
        pygame.mixer.music.pause()
        quit_graphics()
        pygame.quit()
    else:
        return 0

f = pygame.display.set_mode((1000,800))

background = pygame.image.load('chat_souris.jpg')
background.convert()

def main():
    fill_screen(blanc,f)
    mixer.music.load("game.ogg")
    mixer.music.play()
    cadre_cote()
    bandeau_bas(2)
    S1.arrete(S1.centre,S2.centre,noir)
    S1.arrete(S1.centre,S4.centre,noir)
    S1.arrete(S2.centre,S4.centre,noir)
    S1.arrete(S2.centre,S6.centre,noir)
    S1.arrete(S3.centre,S4.centre,noir)
    S1.arrete(S3.centre,S7.centre,noir)
    S1.arrete(S4.centre,S5.centre,noir)
    S1.arrete(S5.centre,S7.centre,noir)
    S1.arrete(S5.centre,S6.centre,noir)
    S1.arrete(S6.centre,S8.centre,noir)
    S1.arrete(S7.centre,S8.centre,noir)
    S1.arrete(S2.centre,S9.centre,noir)
    S1.sommet(noir,"1")
    S2.sommet(noir,"2")
    S3.sommet(noir,"3")
    S4.sommet(noir,"4")
    S5.sommet(noir,"5")
    S6.sommet(noir,"6")
    S7.sommet(noir,"7")
    S8.sommet(noir,"8")
    S9.sommet(blanc,None)
    fromage((75*Largeur//100,9*Hauteur//100))
    f.blit(chat,F2[0])
    f.blit(souris,F7[0])
    E0=evenement()
    while E0.fin!=True:
        E0.suivant()









