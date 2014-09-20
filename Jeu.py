# -*- coding:utf-8 -*-

from random import *
from tkinter import *
from Pile import *
from Carte import *
from Pioche import *
from Defausse import *
from Joueur import *

import os

###########################
###### Classe du Jeu ######
###########################

class Jeu :
    "Classe du jeu Hanabi"

    def __init__(self):
        ''' -> Jeu
        '''
        self.pioche=Pioche()
        self.defausse=Defausse()
        self.lesJoueurs=[]
        self.plateauJeu=[]     
        self.score=None
        self.joueurCourant=None
        self.nbJetonsRouge=None
        self.nbJetonsBleu=None

    def getDerniereCarte(self,indSuite):

        if not(self.plateauJeu[indSuite].estVide()):
            return self.plateauJeu[indSuite].sommet()

    def suiteEstCommence(self,indSuite):

        return not(self.plateauJeu[indSuite].estVide())

    def couleurPasUtilisee(self,couleur):

        for i in range(0,6):
            if self.suiteEstCommence(i):
                if self.getDerniereCarte(i).getCouleur()==couleur:
                    return False
        return True

    def peutPoser(self,indSuite,carte):
        
        if self.suiteEstCommence(indSuite):
            
            derCarte=self.getDerniereCarte(indSuite)
            if carte.peutEtrePlaceApres(derCarte):
                return True

        else :

            if((carte.getValeur()==1)and(self.couleurPasUtilisee(carte.getCouleur()))):
                return True
            
        return False

    def poser(self,indSuite,carte):

        self.plateauJeu[indSuite].empiler(carte)

    def suiteEstFinie(self,indSuite):

        return self.getDerniereCarte(indSuite).getValeur()==5

    def plateauJeuComplet(self):

        for i in range(0,6):
            if not(self.suiteEstFinie(i)):
                return False
        return True

    def finDePartie(self):

        if((self.nbJetonsRouge==3)or(self.pioche.estVide())or(self.plateauJeuComplet())):
            return True
        return False

    def affRegles(self):
      
      # infos pour la modification du fichier texte rgls :
      # chaque ligne doit faire maxi 80 caracts (taille en largeur du term)
      # sinon il y a un décalage dans la lecture du fichier et c'est plus trop
      # lisible. Pour les sauts de lignes, il ne faut pas qu'il y est des espaces
      # dans les lignes vide sinon même problème.

      print()

      obj = open('rgls.txt', 'r')
      lig = obj.read(80)
      print(lig, end="")

      while (lig != "") :
        lig = obj.read(80)
        print(lig, end="")

      obj.close()
        

    def affCommand(self):

        print()
        print("Tapez show pour voir le plateau de jeu, c'est à dire les cartes de vos coéquipiers,\n",
              "le nombre de jetons bleu et rouge, les cartes de la défausse, votre score, ...")
        print()
        print("Tapez move inform <joueurN> <info> <position1> [<position2> ...]")
        print("      <joueurN> : Le numéro du joueur auquel vous voulez donner l'information")
        print("      <info> : Le type de l'information à donner, une couleur (bleu, blanc, rouge,\n",
              "      jaune, vert, muliticolore) ou une valeur (de 1 à 5)")
        print("      <positionN> : numéro de la position de la carte dans la main du coéquipier\n",
              "      (pensez à donner les positions de toutes les cartes concernées par \n",
              "      l'information)")

    def show(self):

        print("Score : " + str(self.score))
        print("Jetons Bleus : " + str(self.nbJetonsBleu))
        print("Jetons Rouges : " + str(self.nbJetonsRouge))
        print()
        print(self.joueur2.afficher())
        
    def move(self,liste):

        if liste[0]=="play" :
            if len(liste)>2:
                print("Vous ne pouvez jouer qu'une seule carte.")
                return False
            elif len(liste)==1:
                print("Vous devez désigner une carte.")
                return False
            elif (int(liste[1])<0 or int(liste[1])>4):
                print("Postion de carte non valable. Veuillez taper un chiffre entre 0 et 4.")
                return False
            else:
                carte = self.lesJoueurs[self.joueurCourant].retirer(int(liste[1]))
                print("Vous jouez la carte" + carte.afficherCarte())
                self.lesJoueurs[self.joueurCourant].ajouter(self.pioche.piocher())
                for i in range(0,6):
                    if self.peutPoser(i,carte):
                        print("Bien joué")
                        self.poser(i,carte)
                        self.score+=1
                        return True
                self.nbJetonsRouge+=1
                print("Dommage !")
            return True
            
        elif liste[0]=="defausse":
            if len(liste)>2:
            	print("Vous ne pouvez défausser qu'une seule carte.")
            	return False
            elif len(liste)==1:
            	print("Vous devez désigner une carte.")
            	return False
            elif (int(liste[1])<0 or int(liste[1])>4):
            	print("Postion de carte non valable. Veuillez taper un chiffre entre 0 et 4.")
            	return False
            elif self.nbJetonsBleu == 8:
            	print("Vous avez 8 jetons bleu. Vous ne pouvez donc pas défausser")
            	return False
            else:
            	carte = self.lesJoueurs[self.joueurCourant].retirer(int(liste[1]))
            	print("Vous défausser la carte" + carte.afficherCarte())
            	self.defausse.ajouter(carte)
            	self.nbJetonsBleu+=1
            return True
            
        elif liste[0]=="info":
        	print()
            
                
                
    def jouer(self):
        ''' '''
        print("Hanabi Version 1.0")
        print("Paul Cieslar, Marc-Alexis Beauchemin, Eric Hewusz, Nicolas Vittu")
        print()
        print("Une petite partie de Hanabi ?")
        print()
        print("Tapez aide pour obtenir de l'aide sur les commandes.")
        choix=input("> ")
        while choix == "aide":
            print("Mode solo : Tapez solo pour jouer une partie seul (contre l'ordinateur).")
            print()
            print("Mode arbitre : Tapez arbiter pour arbitrer un match.")
            print()
            print("Mode reseau : Tapez reseau pour commencer une partie en réseau.")
            print()
            print("Aide : Tapez aide pour afficher cette page")
            print()
            choix=input("> ")
        if choix == "solo":
            self.solo()
        elif choix == "exit":
            exit()

    def solo(self):
    
        self.lesJoueurs.append(Joueur("0"))
        self.lesJoueurs.append(Joueur("1"))


        for i in range(0,4):
            self.lesJoueurs[0].ajouter(self.pioche.piocher())
            self.lesJoueurs[1].ajouter(self.pioche.piocher())

        for i in range (0,6):
            self.plateauJeu.append(Pile())
        self.score=0
        self.joueurCourant=0
        self.nbJetonsRouge=0
        self.nbJetonsBleu=8
        print("Bienvenue dans le mode solo")
        print("Tapez regles pour afficher les règles du jeu et aide pour les commandes utiles à son utilisation")
        while True :#not(self.finDePartie()):
            print("Joueur " + str(self.joueurCourant) + " > ",end='')
            choix=input().split()
            if choix[0] == "regles" :
                self.affRegles()
            elif choix[0] == "aide" :
                self.affCommand()
            elif choix[0] == "move" :
                self.move(choix[1:])
            elif choix[0] == "show" :
                self.show()
            elif choix[0] == "exit" :
                self.jouer()
            
#if "__name__" == "__main__" :
jeu = Jeu()
jeu.jouer()

