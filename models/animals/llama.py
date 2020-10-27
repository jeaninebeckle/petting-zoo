from datetime import date
from models.animals.animals import Animal

class Llama(Animal):
	def __init__(self, name, species, shift, food, chip_number):
		super().__init__(name, species, food, chip_number)
		self.shift = shift
		self.walking = True

	@property
	def chip_number(self):
		return self.__chip_number

	@chip_number.setter
	def chip_number(self, number):
		pass

	
