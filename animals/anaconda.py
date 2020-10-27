from movements.slithering import Slithering
from animals.animal import Animal
from datetime import date


class Anaconda(Animal, Slithering):
	def __init__(self, name, species, food, chip_number):
		Animal.__init__(self, name, species, food, chip_number)
		Slithering.__init__(self)

	def feed(self):
		print(f'{self.name} was fed {self.food} and almost ate the intern in the process.')
