from datetime import date

class Bass():
	def __init__(self, name, species, food, chip_number):
		self.name = name
		self.species = species
		self.date_added = date.today()
		self.swimming = True
		self.food = food
		self.__chip_number = chip_number

	@property
	def chip_number(self):
		return self.__chip_number

	@chip_number.setter
	def chip_number(self, number):
		pass
