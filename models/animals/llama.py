from datetime import date

class Llama():
	def __init__(self, name, species, shift, food):
		self.name = name
		self.species = species
		self.shift = shift
		self.date_added = date.today()
		self.walking = True
		self.food = food
