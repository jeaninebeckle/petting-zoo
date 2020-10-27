from datetime import date
from movements.slithering import Slithering
from animals.animal import Animal

class Copperhead(Animal, Slithering):
	def __init__(self, name, species, food, chip_number):
		Animal.__init__(self, name, species, food, chip_number)
		Slithering.__init__(self)
