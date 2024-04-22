# Créé par Eleve, le 29/12/2021 en Python 3.7
from graphics import*
import random

class Elts():
    def  __init__(self,val,suiv):
        self.val=val
        self.suiv=suiv

class file_affichée:
#le seul probléme c'est que je dois relier cette file avec l'autre file,
#faire en sorte que cette file prenne des voitures depuis l'autre file
#mais apart ça, cette file fonction trés bien

    def __init__(self, max_taille, taille=0, tete=0, queue=0):
        self.file = [[] for i in range(5)]
        # le 5 c'est le nombre de voiture max que la file puisse acceuir, au-dela ça fait une erreur
        self.max_taille = max_taille
        self.taille = taille
        self.tete = tete
        self.queue = queue



    def ajouter(self, donnee):
        if not self.est_pleins():
            self.file[self.queue] = donnee
            self.queue = int((self.queue + 1) % self.max_taille)
            self.taille += 1
            print(f"la voiture {donnee} est arrivée dans la file affichée")
        else:
            print("File_affichée est pleine")

    def retirer(self):
        if not self.est_vide():
            print(f"la voiture {self.file[self.tete]} est entrée dans le parking")
            self.tete = int((self.tete + 1) % self.max_taille)
            self.taille -= 1
        else:
            print("File_affichée est vide")

    def est_vide(self):
        return self.taille == 0


    def est_pleins(self):
        return self.taille == self.max_taille

    def affiche(self):
        if self.est_vide():
            print("la file_affichée est vide")
        else:
            print ("File_affichée contient :")
            for i in range(self.taille):
                print (f"la voiture {self.file[int((i+self.tete)% self.max_taille)]}")


class File_non_affichée():
    def __init__(self):
        self.tete=None
        self.queue=None

    def est_vide(self):
            if self.tete==None:
                return True
            return False

    def ajouter(self,v):
            elt=Elts(v,None)
            if self.est_vide():
                self.tete=elt
            else:
                self.queue.suiv=elt
            self.queue=elt
            print(f"la voiture {v} vient d'arriver dans la file non affichée")

    def retirer(self):
        if self.est_vide():
            print("la file_non_affichée est vide !")
            return None
        else:
            v = self.tete.val
            if self.tete==self.queue:
                self.queue=None
            self.tete=self.tete.suiv
            print(f"la voiture {v} se déplace vers la file affichée")
            v=v-1
            return v

    def afficher(self):
        if self.est_vide():
            print("La file_non_affichée est vide")
        else:
            print("la file_non_affichée contient : ")
            x=self.tete
            print("la voiture",x.val)
            while x.suiv!=None:
                x=x.suiv
                print("la voiture",x.val)
            print()

#---------------------------------------- Test ------------------------------------------

f=File_non_affichée()
F=file_affichée(2)  # le 2 c'est pour indiquer le nombre max de voiture qu'on veut dans la file, c'est un chiffre entre 0 et 5

plaques = {"AB3":1,"GH6":2,"ZP4":3,"PD6":4,"TA1":5,"CV2":6,"BG8":7,"PO0":8,"QS7":9,"AQ2":10,"DF3":11,"CR7":12,"LM0":13,"NR9":14,"RP9":15,"SO6":16,"QS4":17,"RS4":18,"XX2":19,"KB9":20}
r=randint(0,20)
print()
def deplacemnt_de_file_en_file():
    credits = 0
    global r
    global plaques
    global d
    a=1
    attendre(1500)
    print(f"aujourd'hui on a eu {r} vehicules")
    attendre(2000)
    print()
    if r==0:
        print("Aucune voiture n'est venue, c'est dommage... ")
    elif r==1:
        f.afficher()
        print()
        attendre(2000)
        f.ajouter(a)
        print()
        f.afficher()
        print()
        attendre(2000)
        b=f.retirer()
        attendre(2000)
        F.ajouter(b+1)
        print()
        print(f"1 Tickets vendus à la voiture {b+1} credits = +3,75€ ")
        credits=credits+3.75
        d = random.choice(list(plaques.keys()))
        print(f"la plaque d'imatriculation de la voiture {b+1} est : {d} ")
        del plaques[d]
        attendre(2000)
        print()
        f.afficher()
        print()
        F.retirer()
    else:
        for a in range (a,r+1,1):
            f.afficher()
            print()
            attendre(500)
            f.ajouter(a)
            attendre(500)
            print()
            f.afficher()
            print()
            attendre(500)
            b=f.retirer()
            attendre(500)
            F.ajouter(b+1)
            print()
            print(f"1 Tickets vendus à la voiture {b+1} = +3,75€ ")
            credits=credits+3.75
            d = random.choice(list(plaques.keys()))
            print(f"la plaque d'imatriculation de la voiture {b+1} est : {d} ")
            del plaques[d]
            print()
            f.afficher()
            print()
            F.retirer()
            attendre(500)
            print()
            attendre(500)
            F.retirer()
        print()
    print("Débrif de la journée : ")
    if r==1:
        print()
        print(f"{r} place a était prise !")
    elif r==20:
        print("Le parking est remplie !!! c'est une bonne journée :) ")
        print()
        print(f"{r} places ont étaient prisent !")
    else:
        print()
        print(f"{r} places ont étaient prisent !")
    print()
    print(f"Et on a fait un total de : {credits} €")
    print()
    attendre(2200)
    F.affiche()
    print()
    attendre(2200)
    f.afficher()
    #print(f"le nombres de plaques restantes sont : {plaques}")
deplacemnt_de_file_en_file()


#----------------------------------------------------------------------------------------
#########################  DEUXIEME PARTIE #########################
