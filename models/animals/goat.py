from datetime import date

class Goat():
	def __init__(self, name, species, shift, food, chip_number):
		self.name = name
		self.species = species
		self.shift = shift
		self.date_added = date.today()
		self.walking = True
		self.food = food
		self.__chip_number = chip_number

	@property
	def chip_number(self):
		return self.__chip_number

	@chip_number.setter
	def chip_number(self, number):
		pass
