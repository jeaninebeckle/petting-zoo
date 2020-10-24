from datetime import date

class Anaconda():
	def __init__(self, name, species, food, chip_number):
		self.name = name
		self.species = species
		self.date_added = date.today()
		self.slithering = True
		self.food = food
		self.__chip_number = chip_number
	
	@property
	def chip_number(self):
		return self.__chip_number

	@chip_number.setter
	def chip_number(self, number):
		pass

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

	# def __str__(self):
	# 	return (f'{self.name} is an {self.species} with chip number {self.chip_number}')
