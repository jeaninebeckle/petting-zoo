from datetime import date
from .animal import Animal
from movements import Walking, Swimming

class Mallard(Animal, Walking, Swimming):
	def __init__(self, name, species, food, chip_number):
		Animal.__init__(self, name, species, food, chip_number)
		Swimming.__init__(self)
		Walking.__init__(self)

