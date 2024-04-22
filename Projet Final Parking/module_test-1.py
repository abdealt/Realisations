from partie_A import*
from vehicules import*


Largeur=800
Hauteur=700


gris_fonce=(50,50,50)
distance_route_arrivé_bord=120
largeur_de_la_place=65
longeur_de_la_place=110
bas_du_parking=Hauteur-215
p8=(Largeur-distance_route_arrivé_bord,bas_du_parking-largeur_de_la_place*2)
p9=(40,bas_du_parking-30)

matière_du_sol()
rangee_gauche(10,10,5)
rangee_droite(Largeur-10,10,5)
rangee_droite(400,10,5)
rangee_gauche(400,10,5)
lignes_pointille_verticale((400-110-85,20),(400-110-85,bas_du_parking-(largeur_de_la_place*2)),50)
lignes_pointille_verticale((Largeur-110-95,20),(Largeur-110-95,bas_du_parking-(largeur_de_la_place*2)),50)
draw_fill_rectangle(p8,p9,gris_fonce,f)
lignes_pointille_horizontale((20,bas_du_parking-largeur_de_la_place),(Largeur,bas_du_parking-largeur_de_la_place),50)
draw_fill_rectangle(p6,p7,orange,f)

barrière_A_fermee(rouge)
barrière_B_fermee(rouge)


V1=Voiture()
V2=Voiture()
V3=Voiture()
V4=Voiture()
V5=Voiture()
V6=Voiture()
V7=Voiture()

V1.vehicule(place1_attente,1,0)
V2.vehicule(place2_attente,1,0)

V1.chemin_aller_place17()
V2.place2_attente_vers_place1_attente()
V3.nouvelle_vers_place2_attente()

V1.chemin_retour_place17()
V2.chemin_aller_place1()
V3.place2_attente_vers_place1_attente()
V4.nouvelle_vers_place2_attente()

V3.chemin_aller_place5()
V4.place2_attente_vers_place1_attente()
V5.nouvelle_vers_place2_attente()

V4.chemin_aller_place7()
V2.chemin_retour_place1()
V3.chemin_retour_place5()
V5.place2_attente_vers_place1_attente()
V6.nouvelle_vers_place2_attente()

V5.chemin_aller_place6()
V6.place2_attente_vers_place1_attente()
V7.nouvelle_vers_place2_attente()
V4.chemin_retour_place7()

V6.chemin_aller_place10()
V7.place2_attente_vers_place1_attente()
V7.chemin_aller_place19()



wait_escape(f)
quit_graphics()