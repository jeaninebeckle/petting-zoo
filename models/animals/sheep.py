from datetime import date

class Sheep():
	def __init__(self, name, species, shift, food, chip_number):
		self.shift = shift
		self.walking = True

	@property
	def chip_number(self):
		return self.__chip_number

	@chip_number.setter
	def chip_number(self, number):
		pass
