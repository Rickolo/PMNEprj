#rappel des couleurs et des valeurs disponibles
#couleur = ('bleu','rouge','blanc','vert','jaune','multi')
#valeur = ('1','2','3','4','5')

class Carte:
	"""
	Classe modélisant une carte 
	A une couleur et une valeur allant de 1 à 5
	"""
	def __init__ (self,valeur,couleur):
		"""
		Construction de la carte
		"""
		self.valeur=valeur
		self.couleur=couleur
	
	def getValeur(self):
		"""
		Affiche la valeur de la carte
		"""
		return self.valeur
	
	def getCouleur(self):
		"""
		Affiche la couleur de la carte
		"""
		return self.couleur
		
		
	def afficherCarte(self):
		"""
		Affiche la valeur et la couleur de la carte
		"""
		return "("+str(self.valeur)+","+str(self.couleur)+")"
		
	def peutEtrePlaceApres(self,carte):
		"""
		Verifie si self peut être placé après carte
		"""
		if (carte.couleur == self.couleur):
			val=self.valeur-1
			if (carte.getValeur() == val):
				return True
		return False
