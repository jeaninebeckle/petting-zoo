from datetime import date

class Copperhead():
	def __init__(self, name, species, food):
		self.name = name
		self.species = species
		self.date_added = date.today()
		self.slithering = True
		self.food = food

