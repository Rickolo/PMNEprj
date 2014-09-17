# Ce fichier contient la classe Joueur utilisée pour le jeu Hanabi.

class Joueur :
  '''
     Elle représente un joueur qui est 
     caractérisé par son nom et son jeu.
  '''
  
  def __init__(self, nom, main=[]) :
    '''
       Joueur, str, list -> Joueur
       La main du joueur est une liste de cartes. 
    '''
    self.nom = nom
    self.main = main

  def ajouter(self, carte) :
    '''
       Joueur, Carte -> unit
       Ajoute une carte à la main du joueur.
    '''
    self.main.append(carte)

  def retirer(self, indice) :
    '''
       Joueur, int -> Carte
       Retire et retourne la carte de la main du joueur 
       à l'indice donné.
    '''
    return self.main.pop(indice)

  def afficher(self) :
    '''
       Joueur -> str
       Affiche le nom et la main du joueur.
       Elle utilise la méthode afficher() de la classe Carte.
    '''
    res = self.nom + " : ["

    for elt in self.main :
      res += elt.afficher() + ", "
    
    res = res[0:len(res)-2] + "]"
    # res += "]" ----> [elt, elt, elt, ]

    return res 

   
