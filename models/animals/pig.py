from datetime import date

class Pig():
	def __init__(self, name, species, shift, food):
		self.name = name
		self.species = species
		self.shift = shift
		self.date_added = date.today()
		self.walking = True
		self.food = food

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

	def __str__(self):
		return f"{self.name} is a {self.species}"

pig = Pig('Peter Pan', 'pig', 'afternoon', 'pig chow')

print(f'{pig.name} the {pig.species} is available to pet during the {pig.shift} shift.')

print(pig)
