from graphics import*


Largeur=800
Hauteur=700

f=init_graphics(Largeur,Hauteur)



def matière_du_sol():
    #fait l'herbe et le goudron au sol
    fill_screen(vertclair,f)
    draw_fill_rectangle(p1,p2,gris_fonce,f)
    draw_fill_rectangle(p3,p4,gris_fonce,f)





def place_de_parking_gauche(longeur_de_la_place,largeur_de_la_place,x_coin_gauche,y_coin_gauche):
    #fait une place de parking avec le bord a gauche
    x=x_coin_gauche
    y=y_coin_gauche
    x2=x+longeur_de_la_place
    y2=y+largeur_de_la_place
    hg=(x,y)
    hd=(x2,y)
    bg=(x,y2)
    bd=(x2,y2)
    draw_fill_rectangle(hg,bd,gris_fonce,f)
    draw_line(hg,hd,blanc,f)
    draw_line(bg,bd,blanc,f)
    draw_line(hg,bg,blanc,f)


def place_de_parking_droite(longeur_de_la_place,largeur_de_la_place,x_coin_droit,y_coin_droit):
    #fait une place de parking avec le bord a droite
    x=x_coin_droit
    y=y_coin_droit
    x2=x-longeur_de_la_place
    y2=y+largeur_de_la_place
    hd=(x,y)
    hg=(x2,y)
    bd=(x,y2)
    bg=(x2,y2)
    draw_fill_rectangle(hg,bd,gris_fonce,f)
    draw_line(hg,hd,blanc,f)
    draw_line(bg,bd,blanc,f)
    draw_line(hd,bd,blanc,f)






def rangee_gauche(coordoneeX,coordoneeY,taille):
    #fait une rangé de places avec la foction place de parking gauche selon l'argument taille
    y=-largeur_de_la_place+coordoneeY
    for i in range(taille):
        y=y+largeur_de_la_place
        place_de_parking_gauche(longeur_de_la_place,largeur_de_la_place,coordoneeX,y)

def rangee_droite(coordoneeX,coordoneeY,taille):
    #fait une rangé de places avec la foction place de parking droite selon l'argument taille
    y=-largeur_de_la_place+coordoneeY
    for i in range(taille):
        y=y+largeur_de_la_place
        place_de_parking_droite(longeur_de_la_place,largeur_de_la_place,coordoneeX,y)







def base_barrière(x,y):
    #crée la base de la barrière
    x2=x-10
    y2=y+15
    p1=(x,y)
    p2=(x2,y2)
    draw_fill_rectangle(p1,p2,noir,f)




def barrière_A_fermee(couleur):
    #fait apparaitre la barrière A fermée
    base_barrière(Largeur-(largeur_de_la_place*2+10+distance_route_arrivé_bord),bas_du_parking)
    (x,y)=p3
    x2=x+largeur_de_la_place
    y2=y+3
    p1=(x,y)
    p2=(x2,y2)
    draw_fill_rectangle(p1,p2,couleur,f)

def barrière_A_ouverte(couleur):
    #fait apparaitre la barrière A ouverte
    barrière_A_fermee(gris_fonce)
    base_barrière(Largeur-(largeur_de_la_place*2+10+distance_route_arrivé_bord),bas_du_parking)
    (x,y)=p3
    x2=x+10
    y2=y+3
    p1=(x,y)
    p2=(x2,y2)
    draw_fill_rectangle(p1,p2,couleur,f)

def barrière_B_fermee(couleur):
    #fait apparaitre la barrière B fermée
    base_barrière(Largeur-distance_route_arrivé_bord+10,bas_du_parking)
    (x,y)=p5
    x2=x-largeur_de_la_place
    y2=y+3
    p1=(x,y)
    p2=(x2,y2)
    draw_fill_rectangle(p1,p2,couleur,f)

def barrière_B_ouverte(couleur):
    #fait apparaitre la barrière B ouverte
    barrière_B_fermee(gris_fonce)
    base_barrière(Largeur-(distance_route_arrivé_bord-10),bas_du_parking)
    (x,y)=p5
    x2=x-10
    y2=y+3
    p1=(x,y)
    p2=(x2,y2)
    draw_fill_rectangle(p1,p2,couleur,f)





def lignes_pointille_horizontale(p1,p2,taille_trait):
    #fait une ligne de pointillé horisontale entre p1 et p2 avec un espace "taille_trait" alterant la couleur du sol et orange
    (z,k)=p2
    a=distance(p1,p2)//taille_trait
    a=int(a)
    b=a//2
    if a==0:
        for i in range (a):
            (x,y)=p1
            x2=x+taille_trait
            y2=y
            p1=(x,y)
            p2=(x2,y2)
            draw_line(p1,p2,orange,f)
            (x,y)=p1
            x=x+taille_trait
            p1=(x,y)
            (x,y)=p1
            x2=x+taille_trait
            y2=y
            p1=(x,y)
            p2=(x2,y2)
            draw_line(p1,p2,noir,f)
            (x,y)=p1
            x=x+taille_trait
            p1=(x,y)
    else:
        for i in range (b):
            (x,y)=p1
            x2=x+taille_trait
            y2=y
            p1=(x,y)
            p2=(x2,y2)
            draw_line(p1,p2,orange,f)
            (x,y)=p1
            x=x+taille_trait
            p1=(x,y)
            (x,y)=p1
            x2=x+taille_trait
            y2=y
            p1=(x,y)
            p2=(x2,y2)
            draw_line(p1,p2,gris_fonce,f)
            (x,y)=p1
            x=x+taille_trait
            p1=(x,y)
        if b==0 or b==2 or b==4 or b==6 or b==8:
            ()
        else:
            (x,y)=p1
            x2=x+taille_trait
            y2=y
            p1=(x,y)
            p2=(x2,y2)
            draw_line(p1,p2,orange,f)
        (x,y)=p1
        x=x+a
        p1=(x,y)
        draw_line(p1,p2,orange,f)


def lignes_pointille_verticale(p1,p2,taille_trait):
    #fait une ligne de pointillé verticale entre p1 et p2 avec un espace "taille_trait" alternant la couleur du sol et orange
    (z,k)=p2
    a=distance(p1,p2)//taille_trait
    a=int(a)
    b=a//2
    if a==0:
        for i in range (a):
            (x,y)=p1
            x2=x
            y2=y+taille_trait
            p1=(x,y)
            p2=(x2,y2)
            draw_line(p1,p2,orange,f)
            (x,y)=p1
            x=x
            y=y+taille_trait
            p1=(x,y)
            (x,y)=p1
            x2=x
            y2=y+taille_trait
            p1=(x,y)
            p2=(x2,y2)
            draw_line(p1,p2,noir,f)
            (x,y)=p1
            x=x
            y=y+taille_trait
            p1=(x,y)
    else:
        for i in range (b):
            (x,y)=p1
            x2=x
            y2=y+taille_trait
            p1=(x,y)
            p2=(x2,y2)
            draw_line(p1,p2,orange,f)
            (x,y)=p1
            x=x
            y=y+taille_trait
            p1=(x,y)
            (x,y)=p1
            x2=x
            y2=y+taille_trait
            p1=(x,y)
            p2=(x2,y2)
            draw_line(p1,p2,gris_fonce,f)
            (x,y)=p1
            x=x
            y=y+taille_trait
            p1=(x,y)
        if b==0 or b==2 or b==4 or b==6 or b==8:
            ()
        else:
            (x,y)=p1
            x2=x
            y2=y+taille_trait
            p1=(x,y)
            p2=(x2,y2)
            draw_line(p1,p2,orange,f)
        (x,y)=p1
        y=y+a
        p1=(x,y)
        draw_line(p1,p2,orange,f)


#valeur:
gris_fonce=(50,50,50)#couleur du parking
distance_route_arrivé_bord=120#distance entre le coté droit de la route pour aceder au parking et le bord de la fenêtre
largeur_de_la_place=65
longeur_de_la_place=110
bas_du_parking=Hauteur-215#distance entre le bas du parking et le bord de la fenêtre sans prendre en compte la route pour arriver au parking
#point utilisé dans l'apellation des fonction
p1=(10,10)
p2=(Largeur-10,Hauteur-215)
p3=(Largeur-(largeur_de_la_place*2+10+distance_route_arrivé_bord),Hauteur-215)
p4=(Largeur-distance_route_arrivé_bord,Hauteur)
p5=(Largeur-distance_route_arrivé_bord,bas_du_parking)
p6=(Largeur-(distance_route_arrivé_bord+largeur_de_la_place+6),bas_du_parking)
p7=(Largeur-(distance_route_arrivé_bord+largeur_de_la_place+4),Hauteur)




#zone de test
"""
matière_du_sol()
rangee_gauche(10,10,5)
rangee_droite(Largeur-10,10,5)
rangee_droite(400,10,5)
rangee_gauche(400,10,5)

lignes_pointille_horizontale((20,bas_du_parking-largeur_de_la_place),(Largeur,bas_du_parking-largeur_de_la_place),50)
lignes_pointille_verticale((400-110-85,20),(400-110-85,bas_du_parking-(largeur_de_la_place*2)),50)
lignes_pointille_verticale((Largeur-110-95,20),(Largeur-110-95,bas_du_parking-(largeur_de_la_place*2)),50)
draw_fill_rectangle(p6,p7,orange,f)
barrière_A_fermee(rouge)
barrière_B_fermee(rouge)
attendre(2000)
barrière_A_fermee(gris_fonce)
barrière_B_fermee(gris_fonce)
barrière_A_ouverte(rouge)
barrière_B_ouverte(rouge)








wait_escape(f)
quit_graphics()"""