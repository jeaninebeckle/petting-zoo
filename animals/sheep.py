from datetime import date
from movements.walking import Walking
from animals.animal import Animal

class Sheep(Animal, Walking):
	def __init__(self, name, species, shift, food, chip_number):
		Animal.__init__(self, name, species, food, chip_number)
		Walking.__init__(self)
		self.shift = shift
