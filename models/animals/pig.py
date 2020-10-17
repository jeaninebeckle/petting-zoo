from datetime import date

class Pig():
	def __init__(self, name, species, shift):
		self.name = name
		self.species = species
		self.shift = shift
		self.date_added = date.today()
		self.walking = True

pig = Pig('Peter Pan', 'pig', 'afternoon')

print(f'{pig.name} the {pig.species} is available to pet during the {pig.shift} shift.')
