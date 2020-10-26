from datetime import date
from models.animals.animals import Animal

class Swan(Animal):
	def __init__(self, name, species, food, chip_number):
		super().__init__(name, species, food, chip_number)
		self.swimming = True
