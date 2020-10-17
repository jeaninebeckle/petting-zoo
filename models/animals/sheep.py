from datetime import date

class Sheep():
	def __init__(self, name, species, shift):
		self.name = name
		self.species = species
		self.shift = shift
		self.date_added = date.today()
		self.walking = True
		
sheep = Sheep('Spongebob Squarepants', 'sheep', 'morning')

print(f'{sheep.name} the {sheep.species} is available to pet during the {sheep.shift} shift.')
