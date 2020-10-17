from datetime import date

class Goat():
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
		return(f'{self.name} is a {self.species}')	

goat = Goat('Gandalf the Grey', 'goat', 'midday', 'goat chow')

print(f'{goat.name} the {goat.species} is available to pet during the {goat.shift} shift.')

print(goat)
