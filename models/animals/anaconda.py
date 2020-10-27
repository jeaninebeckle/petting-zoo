from datetime import date
from models.animals.animals import Animal

class Anaconda(Animal):
	def __init__(self, name, species, food, chip_number):
		super().__init__(name, species, food, chip_number)
		self.slithering = True
	
	@property
	def chip_number(self):
		return self.__chip_number

	@chip_number.setter
	def chip_number(self, number):
		pass

	def feed(self):
		print(f'{self.name} was fed {self.food} and almost ate the intern in the process.')


