from datetime import date

class Goldfish():
	def __init__(self, name, species, food):
		self.name = name
		self.species = species
		self.date_added = date.today()
		self.swimming = True
		self.food = food
