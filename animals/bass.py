from datetime import date
from animals.animal import Animal
from movements.swimming import Swimming

class Bass(Animal, Swimming):
	def __init__(self, name, species, food, chip_number):
		Animal.__init__(self, name, species, food, chip_number)
		Swimming.__init__(self)
