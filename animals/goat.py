from datetime import date
from movements.walking import Walking
from animals.animal import Animal

class Goat(Animal, Walking):
	def __init__(self, name, species, shift, food, chip_number):
		Animal.__init__(self, name, species, food, chip_number)
		Walking.__init__(self)
		self.shift = shift

	def feed(self):
		print(f'{self.name} was fed his normal {self.food} even though all he wanted to eat was Lembas.')
