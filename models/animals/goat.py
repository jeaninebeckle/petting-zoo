from datetime import date

class Goat():
	def __init__(self, name, species, shift):
		self.name = name
		self.species = species
		self.shift = shift
		self.date_added = date.today()
		self.walking = True

goat = Goat('Gandalf the Grey', 'goat', 'midday')

print(f'{goat.name} the {goat.species} is available to pet during the {goat.shift} shift.')
