from datetime import date
from movements.walking import Walking
from movements.swimming import Swimming
from animals.animal import Animal

class Swan(Animal, Swimming, Walking):
	def __init__(self, name, species, food, chip_number):
		Animal.__init__(self, name, species, food, chip_number)
		Swimming.__init__(self)
		Walking.__init__(self)


	def feed(self):
		print(f'{self.name} wasn\'t in the mood to eat {self.food} today.')

	def run(self):
		print(f'{self.name} waddles and paddles')
