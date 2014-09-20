class Pile :
	'''Permet de créer des Piles d'éléments'''	
	def __init__ (self):
		'''Pile -> rien
		Construit une pile vide'''	
		self.lesElts=[]
		self.nb=0

	def empiler (self,elt):
		'''(inout)Pile, Objet -> rien
		Ajoute un élément au sommet de la pile'''		
		self.lesElts.append(elt)
		self.nb+=1

	def depiler (self):
		'''(inout)Pile -> Objet
		Retourne l'élément au sommet de la pile en l'enlevant'''		
		assert not self.estVide()
		elt=self.lesElts[self.nb-1]
		del self.lesElts[self.nb-1]
		self.nb-=1
		return elt

	def estVide (self):
		'''Pile -> bool
		Teste si la pile est vide'''		
		return self.nb==0

	def sommet (self):
		'''Pile -> Objet
		Retourne l'élément au sommet de la pile sans la modifier'''		
		assert not self.estVide()
		return self.lesElts[self.nb-1]
