from graphics import*
import pygame as pg


LARGEUR=1000
HAUTEUR=600

f=init_graphics(LARGEUR,HAUTEUR)



def main_niveau_1():
    #programme afichant les bases de l'interface du niveau 1
    fill_screen(vertclair,f)
    p1=(150,250)
    p2=(LARGEUR-150,350)
    draw_fill_rectangle(p1,p2,beige,f)
    m=0
    # programme créant les 10 question du niveau
    for i in range(10):
        p1=(150,250)
        p2=(LARGEUR-150,350)
        draw_fill_rectangle(p1,p2,beige,f)
        p3=(0,0)
        p4=(LARGEUR,150)
        draw_fill_rectangle(p3,p4,vertclair,f)
        p5=(50,100)
        p6=(135,100)
        p7=(155,95)
        o=i+1
        ecrire("Question",p5,20,blanc,f)
        ecrire_nombre(o,p6,20,blanc,f)
        ecrire(":",p7,25,blanc,f)
        # Partie créant les question
        p1=(300,280)
        p2=(360,280)
        p3=(420,280)
        p4=(480,280)
        p5=(540,280)
        p6=(LARGEUR-60,280)
        a=randint(1,9)
        b=randint(1,9)
        ecrire_nombre(a,p1,50,noir,f)
        ecrire("x",p2,50,noir,f)
        ecrire_nombre(b,p3,50,noir,f)
        ecrire("=",p4,50,noir,f)
        z1=a*b
        Pa=(LARGEUR-60,10)
        Pb=(LARGEUR-10,60)
        Pc=(LARGEUR-10,10)
        Pd=(LARGEUR-60,60)
        draw_rectangle(Pa,Pb,blanc,f)
        draw_line(Pa,Pb,blanc,f)
        draw_line(Pc,Pd,blanc,f)
        # programme permettant de permettre à l'utilisateur d'écrire dans la fenetre pygame
        font = pg.font.Font(None, 32)
        clock = pg.time.Clock()
        input_box = pg.Rect(510, 290, 140, 32)
        color_inactive = pg.Color('black')
        color_active = pg.Color('red')
        color = color_inactive
        active = False
        text = ''
        done = False
        point_exit=(LARGEUR-30,30)
        while not done:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    elif distance(point_exit,event.pos)<=25:
                        quit_graphics()
                    else:
                        active = False
                        ()
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type == pg.KEYDOWN:
                    if active:
                        if event.key == pg.K_RETURN:
                            text=int(text)
                            if text == z1:
                                valide()
                                m=m+1
                                print("score actuelle =",m,"/10")
                                attendre(1000)
                            else:
                                ()
                            text = ''
                            done= True
                        elif event.key == pg.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
            P1=(512,292)
            P2=(708,320)
            draw_fill_rectangle(P1,P2,beige,f)
            # Render the current text.
            txt_surface = font.render(text, True, black)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            # Blit the text.
            f.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            pg.draw.rect(f, black, input_box, 2)
            pg.display.flip()
            clock.tick(5)
    interface_finale(m)



def main_niveau_2():
    #programme afichant les bases de l'interface du niveau 2
    fill_screen(bleumarine,f)
    p1=(150,250)
    p2=(LARGEUR-150,350)
    draw_fill_rectangle(p1,p2,beige,f)
    m=0
    # programme créant les 10 question du niveau
    for i in range(10):
        p1=(150,250)
        p2=(LARGEUR-150,350)
        draw_fill_rectangle(p1,p2,beige,f)
        p3=(0,0)
        p4=(LARGEUR,150)
        draw_fill_rectangle(p3,p4,bleumarine,f)
        p5=(50,100)
        p6=(135,100)
        p7=(155,95)
        o=i+1
        ecrire("Question",p5,20,blanc,f)
        ecrire_nombre(o,p6,20,blanc,f)
        ecrire(":",p7,25,blanc,f)
        Pa=(LARGEUR-60,10)
        Pb=(LARGEUR-10,60)
        Pc=(LARGEUR-10,10)
        Pd=(LARGEUR-60,60)
        draw_rectangle(Pa,Pb,blanc,f)
        draw_line(Pa,Pb,blanc,f)
        draw_line(Pc,Pd,blanc,f)
        # Partie créant les question
        p1=(300,280)
        p2=(360,280)
        p3=(420,280)
        p4=(480,280)
        p5=(540,280)
        p6=(LARGEUR-60,280)
        a=randint(5,9)
        b=randint(5,9)
        c=randint(11,15)
        z=randint(1,5)
        if z>=2:
            b=c
        else:
            ()
        ecrire_nombre(a,p1,50,noir,f)
        ecrire("x",p2,50,noir,f)
        ecrire_nombre(b,p3,50,noir,f)
        ecrire("=",p4,50,noir,f)
        z1=a*b
        # programme permettant de permettre à l'utilisateur d'écrire dans la fenetre pygame
        font = pg.font.Font(None, 32)
        clock = pg.time.Clock()
        input_box = pg.Rect(510, 290, 140, 32)
        color_inactive = pg.Color('black')
        color_active = pg.Color('red')
        color = color_inactive
        active = False
        text = ''
        done = False
        point_exit=(LARGEUR-30,30)
        while not done:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    elif distance(point_exit,event.pos)<=25:
                        quit_graphics()
                    else:
                        active = False
                        ()
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type == pg.KEYDOWN:
                    if active:
                        if event.key == pg.K_RETURN:
                            text=int(text)
                            if text == z1:
                                valide()
                                m=m+1
                                print("score actuelle =",m,"/10")
                                attendre(1000)
                            else:
                                ()
                            text = ''
                            done= True
                        elif event.key == pg.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
            P1=(512,292)
            P2=(708,320)
            draw_fill_rectangle(P1,P2,beige,f)
            # Render the current text.
            txt_surface = font.render(text, True, black)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            # Blit the text.
            f.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            pg.draw.rect(f, black, input_box, 2)
            pg.display.flip()
            clock.tick(5)
    interface_finale(m)



def main_niveau_3():
    #programme afichant les bases de l'interface du niveau 3
    fill_screen(rouge,f)
    p1=(150,250)
    p2=(LARGEUR-150,350)
    draw_fill_rectangle(p1,p2,beige,f)
    m=0
    # programme créant les 10 question du niveau
    for i in range(10):
        p1=(150,250)
        p2=(LARGEUR-150,350)
        draw_fill_rectangle(p1,p2,beige,f)
        p3=(0,0)
        p4=(LARGEUR,150)
        draw_fill_rectangle(p3,p4,rouge,f)
        p5=(50,100)
        p6=(135,100)
        p7=(155,95)
        o=i+1
        ecrire("Question",p5,20,blanc,f)
        ecrire_nombre(o,p6,20,blanc,f)
        ecrire(":",p7,25,blanc,f)
        Pa=(LARGEUR-60,10)
        Pb=(LARGEUR-10,60)
        Pc=(LARGEUR-10,10)
        Pd=(LARGEUR-60,60)
        draw_rectangle(Pa,Pb,blanc,f)
        draw_line(Pa,Pb,blanc,f)
        draw_line(Pc,Pd,blanc,f)
        # Partie créant les question
        p1=(300,280)
        p2=(360,280)
        p3=(420,280)
        p4=(480,280)
        p5=(540,280)
        p6=(LARGEUR-60,280)
        a=randint(5,9)
        b=randint(5,9)
        c=randint(11,15)
        d=randint(15,19)
        z=randint(1,6)
        if z==2:
            b=c
        elif d>=3:
            b=d
        else:
            ()
        ecrire_nombre(a,p1,50,noir,f)
        ecrire("x",p2,50,noir,f)
        ecrire_nombre(b,p3,50,noir,f)
        ecrire("=",p4,50,noir,f)
        z1=a*b
        # programme permettant de permettre à l'utilisateur d'écrire dans la fenetre pygame
        font = pg.font.Font(None, 32)
        clock = pg.time.Clock()
        input_box = pg.Rect(510, 290, 140, 32)
        color_inactive = pg.Color('black')
        color_active = pg.Color('red')
        color = color_inactive
        active = False
        text = ''
        done = False
        point_exit=(LARGEUR-30,30)
        while not done:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    elif distance(point_exit,event.pos)<=25:
                        quit_graphics()
                    else:
                        active = False
                        ()
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type == pg.KEYDOWN:
                    if active:
                        if event.key == pg.K_RETURN:
                            text=int(text)
                            if text == z1:
                                valide()
                                m=m+1
                                print("score actuelle =",m,"/10")
                                attendre(1000)
                            else:
                                ()
                            text = ''
                            done= True
                        elif event.key == pg.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
            P1=(512,292)
            P2=(708,320)
            draw_fill_rectangle(P1,P2,beige,f)
            # Render the current text.
            txt_surface = font.render(text, True, black)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            # Blit the text.
            f.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            pg.draw.rect(f, black, input_box, 2)
            pg.display.flip()
            clock.tick(5)
    interface_finale(m)



def main_niveau_4():
    #programme afichant les bases de l'interface du niveau 4
    fill_screen(noir,f)
    p1=(150,250)
    p2=(LARGEUR-150,350)
    draw_fill_rectangle(p1,p2,beige,f)
    m=0
    # programme créant les 10 question du niveau
    for i in range(10):
        p1=(150,250)
        p2=(LARGEUR-150,350)
        draw_fill_rectangle(p1,p2,beige,f)
        p3=(0,0)
        p4=(LARGEUR,150)
        draw_fill_rectangle(p3,p4,noir,f)
        p5=(50,100)
        p6=(135,100)
        p7=(155,95)
        o=i+1
        ecrire("Question",p5,20,blanc,f)
        ecrire_nombre(o,p6,20,blanc,f)
        ecrire(":",p7,25,blanc,f)
        Pa=(LARGEUR-60,10)
        Pb=(LARGEUR-10,60)
        Pc=(LARGEUR-10,10)
        Pd=(LARGEUR-60,60)
        draw_rectangle(Pa,Pb,blanc,f)
        draw_line(Pa,Pb,blanc,f)
        draw_line(Pc,Pd,blanc,f)
        # Partie créant les question
        p1=(300,280)
        p2=(360,280)
        p3=(420,280)
        p4=(480,280)
        p5=(540,280)
        p6=(LARGEUR-60,280)
        a=randint(5,9)
        b=randint(5,9)
        c=randint(9,15)
        d=randint(15,19)
        e=randint(21,29)
        z=randint(1,7)
        if z==2:
            b=c
        elif d==3:
            b=d
        elif e>=4:
            b=e
        else:
            ()
        ecrire_nombre(a,p1,50,noir,f)
        ecrire("x",p2,50,noir,f)
        ecrire_nombre(b,p3,50,noir,f)
        ecrire("=",p4,50,noir,f)
        z1=a*b
        # programme permettant de permettre à l'utilisateur d'écrire dans la fenetre pygame
        font = pg.font.Font(None, 32)
        clock = pg.time.Clock()
        input_box = pg.Rect(510, 290, 140, 32)
        color_inactive = pg.Color('black')
        color_active = pg.Color('red')
        color = color_inactive
        active = False
        text = ''
        done = False
        point_exit=(LARGEUR-30,30)
        while not done:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    elif distance(point_exit,event.pos)<=25:
                        quit_graphics()
                    else:
                        active = False
                        ()
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type == pg.KEYDOWN:
                    if active:
                        if event.key == pg.K_RETURN:
                            text=int(text)
                            if text == z1:
                                valide()
                                m=m+1
                                print("score actuelle =",m,"/10")
                                attendre(1000)
                            else:
                                ()
                            text = ''
                            done= True
                        elif event.key == pg.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
            P1=(512,292)
            P2=(708,320)
            draw_fill_rectangle(P1,P2,beige,f)
            # Render the current text.
            txt_surface = font.render(text, True, black)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            # Blit the text.
            f.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            pg.draw.rect(f, black, input_box, 2)
            pg.display.flip()
            clock.tick(5)
    interface_finale(m)








def valide():
    #programme graphique dessinant un symbole valide
    for i in range(100):
        pa=(720+(1/100)*i,300+(1/100)*i)
        pb=(730+(1/100)*i,310+(1/100)*i)
        pc=(750+(1/100)*i,280+(1/100)*i)
        draw_line(pa,pb,vertolive,f)
        draw_line(pb,pc,vertolive,f)


def carre_couleur(f):
    #Partie permettant de créé des carrés de couleurs en bas de l'écran
    a=900
    for i in range(4):
         p1=(LARGEUR-a,HAUTEUR-100)
         (x,y)=p1
         p2=(x+50,y+50)
         if a==650:
            coul=bleu
         elif a==400:
            coul=rouge
         elif a==150:
            coul=noir
         else:
            coul=vertclair
         draw_fill_rectangle(p1,p2,coul,f)
         (x,y)=p2
         p3=(x-32.5,y-40)
         ecrire_nombre(i+1,p3,30,blanc,f)
         a=a-250


def croix_exit():
    # Dessin d'une croix rouge en haut de l'écran
    Pa=(LARGEUR-60,10)
    Pb=(LARGEUR-10,10)
    Pc=(LARGEUR-10,60)
    Pd=(LARGEUR-60,60)
    draw_line(Pa,Pb,rouge,f)
    draw_line(Pb,Pc,rouge,f)
    draw_line(Pc,Pd,rouge,f)
    draw_line(Pd,Pa,rouge,f)
    draw_line(Pa,Pc,rouge,f)
    draw_line(Pb,Pd,rouge,f)


def choix():
    # Partie permettant a l'utilisateur de choisir le niveau de jeux
    point_carré1=(875,HAUTEUR-75)
    point_carré2=(625,HAUTEUR-75)
    point_carré3=(375,HAUTEUR-75)
    point_carré4=(125,HAUTEUR-75)
    point_exit=(LARGEUR-35,35)
    Pa=(LARGEUR-60,10)
    Pb=(LARGEUR-10,10)
    Pc=(LARGEUR-10,60)
    Pd=(LARGEUR-60,60)
    draw_line(Pa,Pb,rouge,f)
    draw_line(Pb,Pc,rouge,f)
    draw_line(Pc,Pd,rouge,f)
    draw_line(Pd,Pa,rouge,f)
    draw_line(Pa,Pc,rouge,f)
    draw_line(Pb,Pd,rouge,f)
    P1=wait_clic()
    if distance(P1,point_carré1)<=25:
        fill_screen(noir,f)
        main_niveau_4()
    elif distance(P1,point_carré2)<=25:
        fill_screen(rouge,f)
        main_niveau_3()
    elif distance(P1,point_carré3)<=25:
        fill_screen(bleu,f)
        main_niveau_2()
    elif distance(P1,point_carré4)<=25:
        main_niveau_1()
    elif distance(P1,point_exit)<=25:
        quit_graphics()
    else:
        choix()


def interface_finale(a):
    # Programme dessinant la fin de la partie
    fill_screen(noir,f)
    p1=(280,200)
    p2=(460,300)
    p3=(550,300)
    p4=(300,500)
    p5=(350,550)
    p6=(600,500)
    p7=(650,550)
    p8=(360,510)
    p9=(660,510)
    point_rejouer=(325,515)
    point_sortie2=(625,515)
    ecrire("Tu a atteind un score de:",p1,40,blanc,f)
    ecrire_nombre(a,p2,40,blanc,f)
    ecrire("/10",p3,40,blanc,f)
    attendre(3000)
    ecrire("Rejouer",p8,30,vert,f)
    ecrire("Quitter",p9,30,rouge,f)
    draw_fill_rectangle(p4,p5,blanc,f)
    draw_fill_rectangle(p6,p7,blanc,f)
    C1=wait_clic()
    if distance(C1,point_rejouer)<=30:
        interface_de_choix()
    elif distance(C1,point_sortie2)<=30:
        quit_graphics()
    else:
        ()


def interface_de_choix():
    # interface du début permettant d'afficher l'accueil
    p=(HAUTEUR/3,LARGEUR/4.5)
    y=(HAUTEUR/2,LARGEUR/3.5)
    z=(20,570)
    Pa=(LARGEUR-60,10)
    Pb=(LARGEUR-10,60)
    Pc=(LARGEUR-10,10)
    Pd=(LARGEUR-60,60)
    draw_rectangle(Pa,Pb,noir,f)
    draw_line(Pa,Pb,rouge,f)
    draw_line(Pc,Pd,rouge,f)
    fill_screen(beige,f)
    ecrire("Bienvenue sur le jeu des tables de multiplication",p,30,noir,f)
    ecrire("Choisis un niveau de difficulté:",y,30,noir,f)
    ecrire("Dans la suite de ce jeux merci de n'entrer que des réponses sous formes de chiffres ou nombre sous peine de voir le programme s'arreter",z,16,noir,f)
    carre_couleur(f)
    choix()





interface_de_choix()




