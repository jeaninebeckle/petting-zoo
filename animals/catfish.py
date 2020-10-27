from datetime import date
from movements.swimming import Swimming
from animals.animal import Animal

class Catfish(Animal, Swimming):
	def __init__(self, name, species, food, chip_number):
		Animal.__init__(self, name, species, food, chip_number)
		Swimming.__init__(self)
