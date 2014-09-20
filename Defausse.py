from Carte import *

class Defausse:
	def __init__ (self):
		'''Defausse -> rien
		Construit une Defausse vide'''	
		self.defausse=[]
	
	def afficherDefausse(self):
		'''Defausse -> str
		Affiche les cartes de la defausse'''
		aff=""
		for c in self.defausse:
			aff+=c.afficherCarte()
		return aff	
	
	def ajouter(self, carte):
		'''Defausse, Carte -> rien 
		Ajoute une carte à la défausse'''
		self.defausse.append(carte)
		
